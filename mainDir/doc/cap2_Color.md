# Color

## Panoramica

Il sistema di controllo del colore permette di generare comandi Visca per regolare vari parametri relativi al bilanciamento del bianco, alla saturazione, alla matrice cromatica e ai guadagni dei colori. Questi comandi sono fondamentali per adattare le impostazioni della telecamera alle diverse condizioni di illuminazione e alle esigenze di ripresa.

Per facilitare l'utilizzo, valori comuni come **auto**, **manual**, o specifici intervalli numerici sono stati organizzati in enumerazioni contenute nel file `enumerations.py`. Ad esempio:
- `WhiteBalanceModeEnum` per le modalità di bilanciamento del bianco.
- `ChromaSuppressionEnum` per la soppressione cromatica.
- `MatrixSelectEnum` per le modalità della matrice cromatica.

---

## **Bilanciamento del Bianco**

### **setWhiteBalanceMode**

Restituisce il comando Visca per impostare la modalità di bilanciamento del bianco. Le modalità disponibili sono definite nell'enumerazione `WhiteBalanceModeEnum`:
```python
camera = CameraObject()
print(camera.color.setWhiteBalanceMode(WhiteBalanceModeEnum.AUTO1))
# Output: 04 35 pp
```

- **AUTO1**: Regola automaticamente il colore per avvicinarlo all'immagine visualizzata.
- **AUTO2**: Regola automaticamente il bilanciamento del bianco eliminando le influenze della luce ambientale.
- **INDOOR**: Fissa il bilanciamento per una temperatura colore di **3200 K**.
- **OUTDOOR**: Fissa il bilanciamento per una temperatura colore di **5800 K**.
- **ONE PUSH**: Regola il bilanciamento del bianco durante la pressione di un tasto specifico.
- **MANUAL**: Permette una regolazione manuale tramite i comandi di guadagno R/B.

---

### **getWhiteBalanceMode**

```python
camera = CameraObject()
print(camera.color.getWhiteBalanceMode())
# Output: Stato attuale del bilanciamento del bianco.
```

Recupera la modalità attuale di bilanciamento del bianco.

---

### **onePushTrigger**

```python
camera = CameraObject()
print(camera.color.onePushTrigger())
# Output: 04 10 05
```

Esegue il comando One Push WB Trigger per bilanciare il bianco in modo rapido.

---

### **setWBSpeed**

```python
camera = CameraObject()
print(camera.color.setWBSpeed(5))
# Output: Comando per impostare la velocità del bilanciamento.
```

Imposta la velocità di convergenza del bilanciamento del bianco. Valori disponibili:
- **1**: Lento.
- **5**: Veloce.
Valido solo per le modalità **AUTO1** e **AUTO2**.

---

## **Guadagni del Colore**

### **setRGain**

```python
camera = CameraObject()
print(camera.color.setRGain(10))
# Output: Comando per impostare il Red Gain.
```

Imposta manualmente il valore del guadagno rosso. Valori disponibili:
- Da **-128** a **127**.

---


### **setBGainUp**

```python
camera = CameraObject()
print(camera.color.setBGainUp())
# Output: Comando per aumentare il guadagno blu.
```

Restituisce il comando Visca per aumentare di un punto il valore del guadagno blu.

---

### **setBGainDown**

```python
camera = CameraObject()
print(camera.color.setBGainDown())
# Output: Comando per diminuire il guadagno blu.
```

Restituisce il comando Visca per diminuire di un punto il valore del guadagno blu.

---

### **setBGain**

```python
camera = CameraObject()
print(camera.color.setBGain(-10))
# Output: Comando per impostare il Blue Gain.
```

Imposta manualmente il valore del Blue Gain (B GAIN).

Valori disponibili:
- Da **-128** a **+127**.

Valido solo per la modalità MANUAL.

:param value: Valore per il Blue Gain.
:return: Visca Command.

---

### **getBGain**

```python
camera = CameraObject()
print(camera.color.getBGain())
# Output: Comando per ottenere il guadagno blu.
```
Restituisce il comando Visca per ottenere il valore del guadagno blu.

---


## **Matrice Cromatica**

Rispetto a vari manuali Sony consultati, si sa poco o niente circa la matrice cromatica. È noto che è possibile selezionare una matrice preimpostata per il calcolo dei colori. Le modalità disponibili sono definite nell'enumerazione MatrixSelectEnum.

Le modalità includono:

STD, HIGH SAT, FL LIGHT, MOVIE, CINEMA, ITU709, B/W.

Tuttavia, il manuale non fornisce dettagli approfonditi su come utilizzare al meglio queste impostazioni o su come ottimizzarle. Rimane un tema aperto per gli operatori esperti che desiderano personalizzare la resa cromatica delle loro immagini.

La Matrice Cromatica è uno strumento fondamentale per ottenere un equilibrio cromatico e per personalizzare i colori durante la fase di ripresa, consentendo di avvicinarsi il più possibile al risultato finale desiderato senza dover ricorrere esclusivamente alla post-produzione.

E' anche utile notare che salvando il file si effettua una compressione del colore e avere una matrice cromatica corretta può aiutare a mantenere la qualità del colore durante la compressione.

Ecco alcune riflessioni:

Per cominciare a sperimentare con questi parametri occorre un vettorscopio e una chart Macbeth o ColorRite per verificare i cambiamenti cromatici e mantenerli coerenti.

Questo sistema consente di regolare le relazioni tra i colori primari (RGB) e i loro complementari per modificare la saturazione e il tono. Ad esempio, agendo sui parametri RG, RB, GR, ecc., è possibile aumentare o diminuire la saturazione di determinati colori in modo da garantire che la resa cromatica sia uniforme e coerente.

Strumenti di Supporto: L'uso di un vettorscopio insieme a una chart Macbeth e un monitor di alta qualità è essenziale per identificare con precisione le modifiche cromatiche. Questi strumenti ti aiutano a verificare i cambiamenti cromatici e a mantenerli coerenti.

Workflow Graduale: Una strategia efficace è partire dalla regolazione generale della matrice utente per ottenere la base cromatica desiderata, per poi affinare i dettagli specifici con la MultiMatrix o in post-produzione.

Effetti sulle Riprese: Le modifiche cromatiche possono enfatizzare o attenuare determinati colori per ottenere effetti visivi specifici. Ad esempio:
RG –99: Desatura il verde e il magenta, rendendo il verde più caldo.
GB +99: Aumenta la saturazione di verde e magenta, con effetti minimi sui colori rimanenti.

Simulazione di Look Cinematici: Con una tabella di valori della matrice, è possibile simulare l'aspetto di pellicole fotografiche, come i colori Technicolor. Questa pratica apre molte possibilità creative, specialmente quando combinata con strumenti di grading avanzati.

### **setMatrixMode**

```python
camera = CameraObject()
print(camera.color.setMatrixMode(MatrixSelectEnum.OFF))
# Output: Comando per selezionare la modalità della matrice.
```

Seleziona una matrice preimpostata per il calcolo dei colori.

**Modalità disponibili:**
- **MatrixSelectEnum.STD**: Matrice standard.
- **MatrixSelectEnum.OFF**: Matrice disattivata.
- **MatrixSelectEnum.HIGH_SAT**: Matrice ad alta saturazione.
- **MatrixSelectEnum.FL_LIGHT**: Matrice per luce fluorescente.
- **MatrixSelectEnum.MOVIE**: Matrice per film.
- **MatrixSelectEnum.STILL**: Matrice per foto.
- **MatrixSelectEnum.CINEMA**: Matrice per cinema.
- **MatrixSelectEnum.PRO**: Matrice professionale.
- **MatrixSelectEnum.ITU709**: Matrice ITU709.
- **MatrixSelectEnum.B_W**: Matrice bianco e nero.

:return: Comando Visca.

---

### **getMatrixMode**

```python
camera = CameraObject()
print(camera.color.getMatrixMode())
# Output: Matrice cromatica attuale.
```

Recupera la modalità corrente della matrice cromatica.

:return: Matrice cromatica attuale.

---
### **setLevelReset**

```python
camera = CameraObject()
print(camera.color.setLevelReset())
# Output: Comando per reimpostare il livello di colore.
```

Reimposta il livello di saturazione al valore predefinito (4).

:return: Visca Command.

---

### **setLevelUp**

```python
camera = CameraObject()
print(camera.color.setLevelUp())
# Output: Comando per incrementare il livello di colore.
```

Incrementa il livello di saturazione.

:return: Visca Command.

---

### **setLevelDown**

```python
camera = CameraObject()
print(camera.color.setLevelDown())
# Output: Comando per decrementare il livello di colore.
```

Decrementa il livello di saturazione.

:return: Visca Command.

---

### **setLevel**

```python
camera = CameraObject()
print(camera.color.setLevel(10))
# Output: Comando per regolare la densità del colore.
```

Regola la densità della saturazione nell'immagine.

Valori disponibili:
- **0**: Colori meno densi.
- **14**: Colori più densi.

Non valido se MATRIX è impostato su OFF.

:param value: Livello di densità del colore (0-14).
:return: Visca Command.

---

### **getLevel**

```python
camera = CameraObject()
print(camera.color.getLevel())
# Output: Livello attuale di densità del colore.
```

Recupera il livello attuale di densità del colore.

:return: Livello attuale (0-14).

---

## **Soppressione Cromatica**

### **setChromaSuppressMode**

```python
camera = CameraObject()
print(camera.color.setChromaSuppressMode(ChromaSuppressionEnum.HIGH))
# Output: Comando per impostare la modalità di soppressione cromatica.
```

Imposta la modalità di soppressione cromatica.

**Modalità disponibili:**
- **OFF**: Soppressione cromatica disattivata.
- **WEAK**: Soppressione cromatica leggera.
- **MID**: Soppressione cromatica moderata.
- **STRONG**: Soppressione cromatica intensa.

:param mode: Modalità di soppressione cromatica (ChromaSuppressionEnum).
:return: Comando Visca.

---

### **getChromaSuppressMode**

```python
camera = CameraObject()
print(camera.color.getChromaSuppressMode())
# Output: Modalità attuale di soppressione cromatica.
```

Recupera la modalità attuale di soppressione cromatica.

:return: Modalità attuale (ChromaSuppressionEnum).

---




### **setPhaseReset**

```python
camera = CameraObject()
print(camera.color.setPhaseReset())
# Output: Comando per reimpostare la fase al valore predefinito.
```

Reimposta la fase al valore predefinito.

:return: Visca Command.

---

### **setPhaseUp**

```python
camera = CameraObject()
print(camera.color.setPhaseUp())
# Output: Comando per incrementare la fase.
```
Incrementa la fase.

:return: Visca Command.

---

### **setPhaseDown**

```python
camera = CameraObject()
print(camera.color.setPhaseDown())
# Output: Comando per decrementare la fase.
```
Decrementa la fase.

:return: Visca Command.

---

### **setPhase**

```python
camera = CameraObject()
print(camera.color.setPhase(-5))
# Output: Comando per regolare la fase.
```

Regola la tonalità generale del colore dell'immagine.

Valori disponibili:
- Da **-7** a **+7**.

Non valido se MATRIX è impostato su OFF.

:param value: Valore della fase (-7 a +7).
:return: Visca Command.
---

### **getPhase**

```python
camera = CameraObject()
print(camera.color.getPhase())
# Output: Comando Visca per ottenere il valore attuale della fase.
```

Recupera il Comando Visca per ottenere il valore attuale della fase.

:return: Valore della fase (-7 a +7).

---

### **setRG**

```python
camera = CameraObject()
print(camera.color.setRG(50))
# Output: Comando per impostare il coefficiente R-G.
```

Imposta il coefficiente per la combinazione R-G.

Valori disponibili:
- Da -99 a +99

Non valido se MATRIX è impostato su OFF.

:param value: Valore del coefficiente (0-255).

:return: Visca Command.

---

### **getRG**

```python
camera = CameraObject()
print(camera.color.getRG())
# Output: Comando Visca per ottenere il valore attuale del coefficiente R-G.
```

Recupera il Comando Visca per ottenere il valore attuale del coefficiente R-G.

---

### **setRB**

```python
camera = CameraObject()
print(camera.color.setRB(120))
# Output: Comando per impostare il coefficiente R-B.
```

Imposta il coefficiente per la combinazione R-B.

Valori disponibili:
- Da 0-255

Non valido se MATRIX è impostato su OFF.

:param value: Valore del coefficiente
:return: Visca Command.

---

### **getRB**

```python
camera = CameraObject()
print(camera.color.getRB())
# Output: Comando Visca per ottenere il valore attuale del coefficiente R-B.
```

Recupera il Comando Visca per ottenere il valore attuale del coefficiente R-B.

---

### **setGR**

```python
camera = CameraObject()
print(camera.color.setGR(-30))
# Output: Comando per impostare il coefficiente G-R.
```

Imposta il coefficiente per la combinazione G-R.

Valori disponibili:
- Da -99 a +99

Non valido se MATRIX è impostato su OFF.

:param value: Valore del coefficiente
:return: Visca Command.

---

### **getGR**

```python
camera = CameraObject()
print(camera.color.getGR())
# Output: Comando Visca per ottenere il valore attuale del coefficiente G-R.
```

Recupera il Comando Visca per ottenere il valore attuale del coefficiente G-R.

---

### **setGB**

```python
camera = CameraObject()
print(camera.color.setGB(-50))
# Output: Comando per impostare il coefficiente G-B.
```

Imposta il coefficiente per la combinazione G-B.

Valori disponibili:
- Da -99 a +99

Non valido se MATRIX è impostato su OFF.

:param value: Valore del coefficiente
:return: Visca Command.

---

### **getGB**

```python
camera = CameraObject()
print(camera.color.getGB())
# Output: Comando Visca per ottenere il valore attuale del coefficiente G-B.
```

Recupera il Comando Visca per ottenere il valore attuale del coefficiente G-B.

---

### **setBR**

```python
camera = CameraObject()
print(camera.color.setBR(25))
# Output: Comando per impostare il coefficiente B-R.
```

Imposta il coefficiente per la combinazione B-R.

Valori disponibili:
- Da -99 a +99

Non valido se MATRIX è impostato su OFF.

:param value: Valore del coefficiente
:return: Visca Command.

---

### **getBR**

```python
camera = CameraObject()
print(camera.color.getBR())
# Output: Comando Visca per ottenere il valore attuale del coefficiente B-R.
```
Recupera il Comando Visca per ottenere il valore attuale del coefficiente B-R.

---

### **setBG**

```python
camera = CameraObject()
print(camera.color.setBG(-10))
# Output: Comando per impostare il coefficiente B-G.
```

Imposta il coefficiente per la combinazione B-G.

Valori disponibili:
- Da -99 a +99

Non valido se MATRIX è impostato su OFF.

:param value: Valore del coefficiente
:return: Visca Command.



---

### **getBG**

```python
camera = CameraObject()
print(camera.color.getBG())
# Output: Comando Visca per ottenere il valore attuale del coefficiente B-G.
```

Recupera il Comando Visca per ottenere il valore attuale del coefficiente B-G.



---






