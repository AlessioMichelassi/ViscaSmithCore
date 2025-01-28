# Documentazione dei Comandi Zoom

## Panoramica
La classe `ZoomInterface` fornisce un set completo di comandi per controllare le funzionalità di zoom di una telecamera compatibile con il protocollo VISCA. Ogni comando è progettato per gestire operazioni di zoom, dalla regolazione della velocità alle modalità digitali e ottiche.

---

### **stopZoom**

```python
camera = CameraObject()
print(camera.zoom.stopZoom())
# Output: Comando per interrompere lo zoom.
```

**Descrizione:** Arresta l'operazione di zoom corrente.

:return: Comando VISCA.

---

### **zoomTeleStandard**

```python
camera = CameraObject()
print(camera.zoom.zoomTeleStandard())
# Output: Comando per eseguire uno zoom in avanti standard.
```

**Descrizione:** Attiva uno zoom in avanti a velocità standard.

:return: Comando VISCA.

---

### **zoomWideStandard**

```python
camera = CameraObject()
print(camera.zoom.zoomWideStandard())
# Output: Comando per eseguire uno zoom indietro standard.
```

**Descrizione:** Attiva uno zoom indietro a velocità standard.

:return: Comando VISCA.

---

### **zoomTeleVariable**

```python
camera = CameraObject()
print(camera.zoom.zoomTeleVariable(speed=5))
# Output: Comando per uno zoom in avanti con velocità variabile.
```

**Descrizione:** Esegue uno zoom in avanti a una velocità specificata.

**Parametri:**
- **speed**: Velocità di zoom, da **0** (lento) a **7** (veloce).

:return: Comando VISCA.

---

### **zoomWideVariable**

```python
camera = CameraObject()
print(camera.zoom.zoomWideVariable(speed=3))
# Output: Comando per uno zoom indietro con velocità variabile.
```

**Descrizione:** Esegue uno zoom indietro a una velocità specificata.

**Parametri:**
- **speed**: Velocità di zoom, da **0** (lento) a **7** (veloce).

:return: Comando VISCA.

---

### **setZoomValue**

```python
camera = CameraObject()
print(camera.zoom.setZoomValue(position=5000))
# Output: Comando per impostare il valore assoluto dello zoom.
```

**Descrizione:** Imposta la posizione assoluta dello zoom.

**Parametri:**
- **position**: Valore dello zoom, compreso tra **0** e **16384**.

:return: Comando VISCA.

---

### **getZoomDirect**

```python
camera = CameraObject()
print(camera.zoom.getZoomDirect())
# Output: Valore attuale dello zoom diretto.
```

**Descrizione:** Recupera il valore attuale dello zoom diretto.

:return: Valore attuale dello zoom.

---

### **setZoomMode**

```python
camera = CameraObject()
print(camera.zoom.setZoomMode(ZoomModeEnum.OPTICAL))
# Output: Comando per impostare la modalità dello zoom.
```

**Descrizione:** Imposta la modalità dello zoom.

**Parametri:**
- **mode**: Modalità di zoom, definita nell'enumerazione `ZoomModeEnum`.

:return: Comando VISCA.

---

### **getZoomMode**

```python
camera = CameraObject()
print(camera.zoom.getZoomMode())
# Output: Modalità attuale dello zoom.
```

**Descrizione:** Recupera la modalità attuale dello zoom.

:return: Modalità attuale dello zoom.

---

### **setTeleConvert**

```python
camera = CameraObject()
print(camera.zoom.setTeleConvert(EnableStateEnum.ON))
# Output: Comando per abilitare la funzione Tele Convert.
```

**Descrizione:** Abilita o disabilita la funzione Tele Convert.

**Parametri:**
- **state**: Stato della funzione, definito in `EnableStateEnum`.

:return: Comando VISCA.

---

### **getTeleConvert**

```python
camera = CameraObject()
print(camera.zoom.getTeleConvert())
# Output: Stato attuale della funzione Tele Convert.
```

**Descrizione:** Recupera lo stato attuale della funzione Tele Convert.

:return: Stato attuale.

---

### **digitalZoomOn**

```python
camera = CameraObject()
print(camera.zoom.digitalZoomOn())
# Output: Comando per abilitare lo zoom digitale.
```

**Descrizione:** Abilita la funzione di zoom digitale.

:return: Comando VISCA.

---

### **digitalZoomOff**

```python
camera = CameraObject()
print(camera.zoom.digitalZoomOff())
# Output: Comando per disabilitare lo zoom digitale.
```

**Descrizione:** Disabilita la funzione di zoom digitale.

:return: Comando VISCA.

---

### **clearImageZoomOn**

```python
camera = CameraObject()
print(camera.zoom.clearImageZoomOn())
# Output: Comando per abilitare il Clear Image Zoom.
```

**Descrizione:** Abilita la funzione di Clear Image Zoom.

:return: Comando VISCA.

---

### **clearImageZoomOff**

```python
camera = CameraObject()
print(camera.zoom.clearImageZoomOff())
# Output: Comando per disabilitare il Clear Image Zoom.
```

**Descrizione:** Disabilita la funzione di Clear Image Zoom.

:return: Comando VISCA.

---

