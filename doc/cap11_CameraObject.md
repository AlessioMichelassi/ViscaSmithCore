# CameraObject: Documentazione

## Panoramica
`CameraObject` rappresenta una telecamera e fornisce un'interfaccia strutturata per gestire i vari parametri e le impostazioni tramite il protocollo **VISCA**.

## Struttura Generale
`CameraObject` è suddiviso in due macro-sezioni:
1. **Memorie (Memories)**: Conservano lo stato attuale della camera.
2. **Interfacce (Interfaces)**: Consentono di inviare e ricevere comandi tramite VISCA.

---

## 1. Memorie della Camera
Le memorie conservano i parametri attuali della camera.

### **Memorie disponibili:**
- **ExposureMemories** → Esposizione (modalità, guadagno, iris, shutter)
- **ColorMemories** → Colore (bilanciamento del bianco, saturazione, offset)
- **DetailMemories** → Dettagli dell'immagine (nitidezza)
- **KneeMemories** → Controllo knee
- **GammaMemories** → Regolazioni gamma
- **GenericsMemories** → Impostazioni generiche
- **FocusMemories** → Messa a fuoco
- **ZoomMemories** → Zoom
- **PanTiltMemories** → Movimento della camera
- **SystemMemories** → Impostazioni di sistema
- **CustomMemories** → Impostazioni personalizzate

---

## 2. Interfacce della Camera
Ogni memoria ha un'interfaccia corrispondente per inviare comandi alla camera.

### **Interfacce disponibili:**
- **ExposureInterface** → Gestisce l'esposizione
- **ColorInterface** → Gestisce il colore e il bilanciamento del bianco
- **DetailInterface** → Controlla la nitidezza
- **KneeInterface** → Gestisce il knee
- **GammaInterface** → Controlla la curva di gamma
- **GenericsInterface** → Impostazioni generiche
- **FocusInterface** → Controlla la messa a fuoco
- **ZoomInterface** → Gestisce lo zoom
- **PanTiltInterface** → Controlla il movimento della camera
- **SystemInterface** → Controlla le impostazioni di sistema
- **PresetInterface** → Gestisce i preset di posizione

---

## Funzionamento

### **Inizializzazione della Camera**
Quando viene creata un'istanza di `CameraObject`, vengono inizializzate sia le memorie che le interfacce:

```python
 def __init__(self):
    self.defaultDictionary = VISCADICTIONARY
    self.initMemories()
    self.initInterfaces()
```
- `self.initMemories()`: Inizializza gli oggetti che memorizzano i parametri attuali.
- `self.initInterfaces()`: Collega le memorie alle rispettive interfacce.

---

### **Invio di Comandi**
I comandi vengono inviati alla camera tramite le interfacce. Ad esempio, per impostare la modalità di esposizione:

```python
self.exposure.set("exposureMode", ExposureModeEnum.MANUAL.value)
```
Questo comando imposta la modalità di esposizione in manuale, aggiornando la memoria e inviando il comando alla camera.

---

### **Gestione dei Comandi ricevuti**
Se la camera invia una risposta o un aggiornamento, `handleSet()` si occupa di interpretare il comando:

```python
def handleSet(self, payload) -> bool:
    command_payload = payload[:3]  # Prendo i primi 3 byte
    for category, commands in self.defaultDictionary.items():
        for command_name, details in commands.items():
            if command_payload.startswith(bytes.fromhex(details["cmd"].split("pp")[0].replace(" ", ""))):
                return self.setMemories(category, command_name, value)
```
Il metodo cerca il comando nel dizionario e aggiorna la memoria corrispondente.

---

## **Riassunto Rapido**
- `CameraObject` rappresenta la camera e gestisce il protocollo **VISCA**.
- **Memorie** → Mantengono lo stato corrente delle impostazioni.
- **Interfacce** → Gestiscono i comandi e la comunicazione con la camera.
- I comandi vengono gestiti attraverso il **ViscaDictionary** e aggiornano le memorie della camera.

