# Documentazione per il Client VISCA over IP

## Descrizione
La classe `ClientObject` implementa un controller **VISCA over IP** per comunicare con una telecamera (o un emulatore di telecamera) tramite il protocollo VISCA esteso su UDP.

### Obiettivi della classe
1. **Inviare comandi** (Set, Inquire, ecc.) verso un server VISCA.
2. **Gestire i sequence number** per correlare i comandi inviati alle risposte (ACK, Completion, Error, Inquire Reply).
3. **Supportare ritrasmissioni** in caso di timeout, compensando l'affidabilità non garantita del protocollo UDP.

---

## Struttura principale

### Dichiarazione della classe
```python
class ClientObject(QObject):
    info_SIGNAL = pyqtSignal(str)
    error_SIGNAL = pyqtSignal(str)
    serverMessage = pyqtSignal(str)

    def __init__(self, _camera, parent=None):
        ...
```

### Dettagli
1. **Eredita da `QObject`** (PyQt) per utilizzare segnali e timer.
2. Riceve un riferimento a `_camera` (istanza di `CameraObject`), che:
   - Mantiene la memoria lato client.
   - Fornisce metodi come `handleSet()` per gestire i parametri locali della telecamera.
3. Inizializza:
   - Un socket UDP (`QUdpSocket`) per la comunicazione di rete.
   - Una coda di comandi (`self.queue`, tipo `deque`) per inviare i comandi uno alla volta.
   - `self.current_command` per tenere traccia del comando in elaborazione.
   - `self.sequence_counter` per assegnare un sequence number crescente a ogni comando.
   - Un timer (`QTimer`) che periodicamente chiama `processQueue()` per gestire eventuali timeout e inviare/rinviare i comandi.

---

## Metodi principali

### **connectToServer(self, host, port)**
- Imposta l'indirizzo e la porta del server.
- Chiama `sendHandshake()` per iniziare la comunicazione VISCA over IP.

---

### **sendHandshake(self)**
- Invia un pacchetto di handshake al server, necessario per alcune implementazioni VISCA over IP.
- Emette il segnale `info_SIGNAL` per il logging.

---

### **enqueueViscaString(self, command_str: str)**
- Riceve una stringa di comando (es. "01 04 39 03") in formato esadecimale.
- Usa `MessagePacker.build_command(command_str)` per incapsularla con l'header (tipo di messaggio, lunghezza, sequence number, terminatore).
- Incrementa `self.sequence_counter` e crea un `ViscaCommand`.
- Inserisce il comando nella coda (`self.queue`).

---

### **processQueue(self)**
- Funzione periodica (50ms) chiamata dal `QTimer`.
- Se non c'è un comando in corso (`self.current_command` è `None`) e la coda non è vuota, preleva il prossimo comando (`popleft()`) e lo invia con `sendCommand(...)`.
- Se c'è un comando in corso:
  - Controlla se è scaduto il timeout (1 secondo di esempio).
  - Se scaduto, incrementa `retries`. Se supera 5 tentativi, dichiara il comando **FAILED**. Altrimenti, tenta di ritrasmettere con `sendCommand(...)`.
  - Se il comando è in stato **DONE** o **FAILED**, lo rilascia per passare al successivo (imposta `current_command = None`).

---

### **sendCommand(self, cmd: ViscaCommand)**
- Invia fisicamente i byte del comando via UDP (`self.socket.writeDatagram(...)`).
- Aggiorna `cmd.last_send_time` con `time.time()`.
- Emette il segnale `info_SIGNAL` per loggare l'invio.

---

### **handleReadyRead(self)**
- Slot chiamato quando il socket ha datagrammi in arrivo.
- Cicla con `while self.socket.hasPendingDatagrams()` per leggere i pacchetti.
- Ogni datagramma viene passato a `parseIncomingPacket(...)`.

---

### **parseIncomingPacket(self, packet: bytes)**
- Usa `self.messageUnpacker.unpack_message(packet)` per ottenere `msg_type`, `seq_num`, e altre info.
- In base a `msg_type`, aggiorna lo stato del comando in corso:
  - **ACK:** Se c'è un comando in **WAITING_ACK** con lo stesso `seq_num`, passa a **WAITING_COMPLETION**.
  - **Completion:** Se c'è un comando in **WAITING_COMPLETION**, lo imposta a **DONE**.
  - **Error:** Imposta lo stato del comando a **FAILED**.
  - **Inquire Reply:** Aggiorna le memorie lato client (chiamando `cameraObject.handleSet(...)`) e imposta lo stato del comando a **DONE**.
- Se il `seq_num` non corrisponde a nessun comando, lo ignora o logga l'evento.

---

## Classi correlate

### **ViscaCommand**
- Semplice contenitore di dati (`bytes`, `sequence_number`, stato, timestamp).

### **MessagePacker**
- Costruisce il pacchetto finale (header + payload + terminatore) da una stringa esadecimale di comando.

### **MessageUnpacker**
- Effettua il parsing dei pacchetti in arrivo per identificare **ACK**, **Completion**, **Error**, **Inquire Reply**, e recupera il sequence number.

---

## Flusso di utilizzo

### Creazione del client
```python
camera = CameraObject()
client = ClientObject(camera)
client.connectToServer("127.0.0.1", 52381)
```

### Invio di un comando "Set"
```python
cmd_str = camera.exposure.setExposureMode(ExposureModeEnum.MANUAL)
client.enqueueViscaString(cmd_str)
```

### Invio di un comando "Inquire"
```python
inquire_str = camera.exposure.getExposureMode()
client.enqueueViscaString(inquire_str)
```

### Gestione di timeout e ritrasmissioni
- Se dopo 1 secondo non arriva la risposta attesa, il client ritrasmette fino a 5 volte.
- Se ancora nulla, il comando è segnato come **FAILED**.

---

## Segnali PyQt
- **info_SIGNAL(str):** Usato per loggare messaggi di debug (comandi inviati, handshake, ecc.).
- **error_SIGNAL(str):** Usato per notificare errori (timeout superato, pacchetto errato, ecc.).
- **serverMessage(str):** Segnale per notificare messaggi provenienti dal server (ad esempio, "inquire_reply" o log di un set eseguito).

---

## Esempio di utilizzo (main)
```python
if __name__ == "__main__":
    app = QApplication([])

    camera = CameraObject()
    client = ClientObject(camera)
    client.connectToServer("127.0.0.1", 52381)

    exp_mode_cmd = camera.exposure.setExposureMode(ExposureModeEnum.MANUAL)
    QTimer.singleShot(1000, lambda: client.enqueueViscaString(exp_mode_cmd))

    inquire_exp_cmd = camera.exposure.getExposureMode()
    QTimer.singleShot(2000, lambda: client.enqueueViscaString(inquire_exp_cmd))

    app.exec()
```

---

## Best Practice
1. **Usare una coda FIFO:** Inviare un comando alla volta per evitare di sovraccaricare il server VISCA.
2. **Gestire ACK e Completion:** Per i comandi di tipo Set, attendere un flusso ACK → Completion. In caso di timeout, ritrasmettere.
3. **Aggiornare la memoria locale:** Per i comandi di tipo Inquire, usare la "inquire_reply" per sincronizzare la memoria lato client.
4. **Timeout:** Gestire i pacchetti persi o la latenza con un timeout per garantire che il client non rimanga bloccato.

---

## Conclusione
`ClientObject` fornisce un metodo robusto per comunicare con una telecamera VISCA over IP, rispettando la logica di ACK/Completion, i sequence number, e i timeout, estendendo il protocollo pensato per RS-232/RS-422 per adattarsi a UDP.

