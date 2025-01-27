# Introduzione a VISCA SMITH

**VISCA SMITH** è un progetto ideato per semplificare l'uso del protocollo VISCA per controllare camere ptz sia nella sfera consumer, prosumer che professional. 
Visca è un sistema di controllo creato da Sony per gestire telecamere tramite connessioni seriali RS-232 che nel corso del tempo, è stato adattato per funzionare anche su reti Ethernet, rendendolo uno standard versatile e largamente adottato nel settore audiovisivo.

Sony fornisce nei suoi manuali tabelle dettagliate che descrivono la maggior parte dei comandi disponibili per le telecamere. Tuttavia, diversi produttori che implementano il protocollo VISCA nei propri dispositivi spesso aggiungono comandi personalizzati per sfruttare al meglio le funzionalità uniche delle loro telecamere.

VISCA utilizza una combinazione di comandi fissi e variabili per eseguire operazioni come:
- Controllo di esposizione
- Bilanciamento del bianco
- Zoom
- Movimento PTZ (Pan, Tilt, Zoom)

I comandi seguono un formato standardizzato, rendendoli prevedibili e relativamente semplici da implementare.

---

## Esempio di utilizzo
La struttura consente di accedere ai comandi tramite un namespace chiaro: 

    exposure.comando, color.comando, ptz.comando, ecc. 

Questo approccio riduce la complessità dell'accesso ai metodi, quindi l'unica operazione richiesta per usare la liberia è creare un cameraObject.

```python
if __name__ == '__main__':
    camera = CameraObject()
    print(camera.exposure.setExposureMode(ExposureModeEnum.MANUAL))
    print(camera.exposure.getExposureMode())
```

### Output
```
01 04 39 03
09 04 39
```

- Il primo comando è quello da inviare alla telecamera per impostare la modalità di esposizione, che può essere:
  - Full Auto
  - Manual
  - Shutter Priority
  - Iris Priority

- Ogni modalità corrisponde a un valore numerico specifico:
  - 0: Full Auto
  - 3: Manual
  - 10: Shutter Priority
  - 11: Iris Priority

Per semplificare l'uso, è stata creata una serie di enumerazioni che permettono di passare alla funzione il valore corretto senza dover consultare continuamente le tabelle Sony. Tutte le enumerazioni sono nel file `enumerations.py` nella cartella 'dictionary'.

---

# Struttura di un comando VISCA
Un comando VISCA è composto da tre parti principali:

### **Header**  - **Payload** -  **Terminator**

Header è la parte del comando include:
- Indirizzo della telecamera (es. `0x81`)
- Lunghezza del messaggio
- Numero sequenziale per identificare il messaggio
- un prefisso che identifica se il comando è una domanda o un'affermazione.

Payload invece è la parte descritta nei dizionari.
- Dettagli dell'operazione
- Parametri da impostare, come:
  - Modalità di esposizione, Livello del guadagno (gain), Velocità dello zoom

### **Terminator**
Un byte fisso (`0xFF`) che indica la fine del comando.

Esempio:
```
HEADER                                     PAYLOAD    TERMINATOR
\x01\x00\x00\x06\x00\x00\x00\x04\x81\x01\  x049\x03    \xff
```

### Evoluzione della Struttura
L’idea di base è stata quella di creare più dizionari e in base a questi dizionari creare una struttura dinamica senza scrivere nemmeno una classe. Ho rapidamente abbandonato l'idea perchè ci sono varie circostanze in python come ad esempio i for loop, non permettono di avere un risultato chiaro e immediato senza inserire una logica di controllo.

Quindi ogni funzione ha u nome identificativo e corrisponde a un payload con il segnaposto o placeholder per le variabili, e il payload per generare la domanda.
Sony non utilizza un sistema univoco per rappresentare le variabili. Alcuni esempi:
  - `0p`: Valori compresi tra 0 e 9.
  - `pp`: Variabili che possono assumere un valore più ampio.
  - `2p` o `3p`: Indicano valori complessi, come 23 per il valore 3.
  - Combinazioni multiple: `pp`, `qq`, `vv`, `ww` per più variabili.

Per questo motivo, nel dizionario è stato inserito un doppio controllo, fornendo una lista di placeholder e il tipo di variabile. Questo approccio migliora l’affidabilità nella gestione dei comandi. Ma in modo più onesto posso dire che pur essendo un protocollo relativamente semplice, il numero di variabili e comandi aumenta il rischio di errori. Durante lo sviluppo sono emersi problemi come confusione tra `camelCase` e `snake_case` o a placeholder errati (es. `0p` invece di `pp`).

Per mitigare questi problemi, sono stati introdotti placeholder nei dizionari come strumento di doppio controllo. Questo approccio ha permesso di:
- Individuare refusi nei comandi.
- Correggerli rapidamente.

Sebbene inizialmente fosse una soluzione temporanea, alla fine è rimasta nel design definitivo.

---
### Separazione dei Comandi e delle Variabili in VISCA SMITH


La progettazione di VISCA SMITH utilizza una separazione chiara tra la logica dei comandi e la gestione delle variabili, implementata rispettivamente nelle classi di interfaccia e nelle classi di memoria.
Perché separare i comandi dalle variabili?

### Organizzazione del codice:

Le classi di interfaccia (ColorInterface, ExposureInterface, ecc.) contengono i metodi per interagire con i comandi VISCA, mappando ogni funzione a un comando specifico.

Le classi di memoria (ColorMemories, ExposureMemories, ecc.) archiviano lo stato corrente delle variabili, come il bilanciamento del bianco, il guadagno o la saturazione.

#### Modularità:
        
Ogni classe di interfaccia è dedicata a una specifica categoria di comandi (es. colore, esposizione, movimento PTZ). Questo mantiene ogni classe sotto le 200 righe di codice (intendo senza i tips e i commenti), semplificando la lettura e la manutenzione.
Le variabili di stato sono isolate in classi di memoria, evitando l'interazione diretta con più classi.


Gestione delle risposte e delle memorie

#### Risposte ai comandi VISCA:
Quando un comando viene inviato, VISCA risponde con un messaggio di completamento (completion) se l'operazione ha avuto successo. Qualsiasi altra risposta indica che il comando non è stato ricevuto correttamente.

Inizialmente, era stato progettato un sistema per memorizzare i valori solo se la risposta era valida. Tuttavia, questa complessità aumentava inutilmente il codice.

Ora, le variabili vengono aggiornate in modo semplice e diretto nelle classi di memoria, rendendo il sistema più leggibile. Questo significa che a un certo punto i dati nelle memorie potrebbero non corrispondere ai dati
nella telecamera, ma questo è un compromesso accettabile per mantenere il codice semplice e leggibile.

## Considerazioni Finali
Il design attuale prevede un insieme di classi statiche che implementano i comandi VISCA e usano i dizionari per generare i payload.
Questo semplifica varie cose, fra le principali, se in un determinato modello, il comando da 04 39 diventa 04 40, per modificarlo è sufficiente andare nel dizionario e modificare il valore.

Ho preferito non avere un sistema dinamico perchè non avere fisicamente scritta la classe che appartiene a un certo dizionario a volta crea complicazioni e confusione in fase di debug. Per ampliare quindi i comandi attuali è necessario scrivere una classe che implementi i comandi e i metodi necessari.

Nonostante questo, il sistema è stato progettato per essere flessibile e facilmente estendibile, con la possibilità di aggiungere nuovi comandi e funzionalità senza dover modificare il codice esistente.