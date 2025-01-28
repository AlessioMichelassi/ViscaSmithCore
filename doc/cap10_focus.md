# Documentazione dei Comandi Focus

## Panoramica
La classe `FocusInterface` offre comandi per gestire le funzionalità di messa a fuoco di una telecamera compatibile con il protocollo VISCA.
Include la gestione della messa a fuoco automatica, manuale e variabile, nonché comandi per la regolazione precisa delle impostazioni di messa a fuoco.

---

### **setFocusMode**

```python
camera = CameraObject()
print(camera.focus.setFocusMode(FocusModeEnum.AUTO))
# Output: Comando per impostare la modalità di messa a fuoco.
```

**Descrizione:** Imposta la modalità di messa a fuoco.

**Valori disponibili:**
- **FocusModeEnum.AUTO**: Messa a fuoco automatica.
- **FocusModeEnum.MANUAL**: Messa a fuoco manuale.
- **FocusModeEnum.TOGGLE**: Alterna tra auto e manuale.

:return: Comando VISCA.

---

### **getFocusMode**

```python
camera = CameraObject()
print(camera.focus.getFocusMode())
# Output: Modalità attuale di messa a fuoco.
```

**Descrizione:** Recupera la modalità attuale di messa a fuoco.

:return: Modalità attuale (FocusModeEnum).

---

### **focusStop**

```python
camera = CameraObject()
print(camera.focus.focusStop())
# Output: Comando per fermare la messa a fuoco.
```

**Descrizione:** Arresta qualsiasi movimento di messa a fuoco in corso.

:return: Comando VISCA.

---

### **focusFarStandard**

```python
camera = CameraObject()
print(camera.focus.focusFarStandard())
# Output: Comando per spostare la messa a fuoco verso lontano a velocità standard.
```

**Descrizione:** Muove la messa a fuoco verso lontano a velocità standard.

:return: Comando VISCA.

---

### **focusNearStandard**

```python
camera = CameraObject()
print(camera.focus.focusNearStandard())
# Output: Comando per spostare la messa a fuoco verso vicino a velocità standard.
```

**Descrizione:** Muove la messa a fuoco verso vicino a velocità standard.

:return: Comando VISCA.

---

### **setFocusFarVariable**

```python
camera = CameraObject()
print(camera.focus.setFocusFarVariable(speed=5))
# Output: Comando per messa a fuoco variabile verso lontano.
```

**Descrizione:** Muove la messa a fuoco verso lontano con velocità variabile.

**Parametri:**
- **speed**: Velocità di messa a fuoco, da **0** (lento) a **7** (veloce).

:return: Comando VISCA.

---

### **setFocusNearVariable**

```python
camera = CameraObject()
print(camera.focus.setFocusNearVariable(speed=3))
# Output: Comando per messa a fuoco variabile verso vicino.
```

**Descrizione:** Muove la messa a fuoco verso vicino con velocità variabile.

**Parametri:**
- **speed**: Velocità di messa a fuoco, da **0** (lento) a **7** (veloce).

:return: Comando VISCA.

---

### **setFocusValue**

```python
camera = CameraObject()
print(camera.focus.setFocusValue(focus_value=12345))
# Output: Comando per impostare il valore assoluto di messa a fuoco.
```

**Descrizione:** Imposta direttamente la posizione della messa a fuoco.

**Parametri:**
- **focus_value**: Valore della messa a fuoco, compreso tra **0x0000** e **0xFFFF**.

:return: Comando VISCA.

---

### **getFocusValue**

```python
camera = CameraObject()
print(camera.focus.getFocusValue())
# Output: Valore attuale della messa a fuoco.
```

**Descrizione:** Recupera il valore attuale della messa a fuoco.

:return: Valore attuale della messa a fuoco.

---

### **focusOnePushTrigger**

```python
camera = CameraObject()
print(camera.focus.focusOnePushTrigger())
# Output: Comando per attivare il trigger AF One Push.
```

**Descrizione:** Attiva il trigger per la messa a fuoco automatica One Push.

:return: Comando VISCA.

---

### **focusInfinity**

```python
camera = CameraObject()
print(camera.focus.focusInfinity())
# Output: Comando per impostare la messa a fuoco all'infinito.
```

**Descrizione:** Imposta la messa a fuoco all'infinito.

:return: Comando VISCA.

---

### **setNearFocusLimit**

```python
camera = CameraObject()
print(camera.focus.setNearFocusLimit(focus_limit=4000))
# Output: Comando per impostare il limite di messa a fuoco vicino.
```

**Descrizione:** Imposta il limite più vicino per la messa a fuoco.

**Parametri:**
- **focus_limit**: Valore del limite, compreso tra **0x0000** e **0xFFFF**.

:return: Comando VISCA.

---

### **setAfMode**

```python
camera = CameraObject()
print(camera.focus.setAfMode(AutoFocusModeEnum.NORMAL))
# Output: Comando per impostare la modalità di messa a fuoco automatica.
```

**Descrizione:** Imposta la modalità di messa a fuoco automatica (AF).

**Valori disponibili:**
- **AutoFocusModeEnum.NORMAL**: Modalità AF normale.
- **AutoFocusModeEnum.INTERVAL**: Modalità AF con intervallo.
- **AutoFocusModeEnum.ZOOM_TRIGGER**: Modalità AF attivata dallo zoom.

:return: Comando VISCA.

---

### **getAfMode**

```python
camera = CameraObject()
print(camera.focus.getAfMode())
# Output: Modalità attuale di messa a fuoco automatica.
```

**Descrizione:** Recupera la modalità attuale di messa a fuoco automatica.

:return: Modalità attuale (AutoFocusModeEnum).

---

### **setAfSensitivity**

```python
camera = CameraObject()
print(camera.focus.setAfSensitivity(AutoFocusSensitivityEnum.LOW))
# Output: Comando per impostare la sensibilità dell'AF.
```

**Descrizione:** Imposta la sensibilità della messa a fuoco automatica.

**Valori disponibili:**
- **AutoFocusSensitivityEnum.LOW**: Sensibilità bassa.
- **AutoFocusSensitivityEnum.NORMAL**: Sensibilità normale.
- **AutoFocusSensitivityEnum.HIGH**: Sensibilità alta.

:return: Comando VISCA.

---

### **getAfSensitivity**

```python
camera = CameraObject()
print(camera.focus.getAfSensitivity())
# Output: Sensibilità attuale della messa a fuoco automatica.
```

**Descrizione:** Recupera la sensibilità attuale della messa a fuoco automatica.

:return: Sensibilità attuale (AutoFocusSensitivityEnum).

---

### **setIrCorrection**

```python
camera = CameraObject()
print(camera.focus.setIrCorrection(IRCorrectionEnum.STANDARD))
# Output: Comando per impostare la correzione IR.
```

**Descrizione:** Imposta la correzione IR.

**Valori disponibili:**
- **IRCorrectionEnum.STANDARD**: Correzione standard.
- **IRCorrectionEnum.IR_LIGHT**: Correzione per luce IR.

:return: Comando VISCA.

---

### **getIrCorrection**

```python
camera = CameraObject()
print(camera.focus.getIrCorrection())
# Output: Correzione IR attuale.
```

**Descrizione:** Recupera la correzione IR attuale.

:return: Correzione IR attuale (IRCorrectionEnum).

---

