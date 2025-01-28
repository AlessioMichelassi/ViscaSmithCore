# Documentazione dei Comandi Pan-Tilt

## Panoramica

La classe `PanTiltInterface` gestisce i comandi relativi al controllo del movimento Pan-Tilt. Questa interfaccia consente di controllare velocità, posizione e limiti dei movimenti Pan-Tilt della telecamera, offrendo un controllo preciso e personalizzabile.

---

### **panTiltDriveUp**

```python
camera = CameraObject()
camera.panTilt.panTiltDriveUp(pan_speed, tilt_speed)
```

**Descrizione:** Muove la telecamera verso l'alto con la velocità specificata.

**Parametri:**
- `pan_speed`: Velocità Pan (1-18).
- `tilt_speed`: Velocità Tilt (1-17).

**Eccezioni:**
- Solleva un `ValueError` se i valori di velocità non sono validi.

---

### **panTiltDriveDown**

```python
camera = CameraObject()
camera.panTilt.panTiltDriveDown(pan_speed, tilt_speed)
```

**Descrizione:** Muove la telecamera verso il basso con la velocità specificata.

**Parametri:**
- `pan_speed`: Velocità Pan (1-18).
- `tilt_speed`: Velocità Tilt (1-17).

---

### **panTiltDriveLeft**

```python
camera = CameraObject()
camera.panTilt.panTiltDriveLeft(pan_speed, tilt_speed)
```

**Descrizione:** Muove la telecamera verso sinistra con la velocità specificata.

**Parametri:**
- `pan_speed`: Velocità Pan (1-18).
- `tilt_speed`: Velocità Tilt (1-17).

---

### **panTiltDriveRight**

```python
camera = CameraObject()
camera.panTilt.panTiltDriveRight(pan_speed, tilt_speed)
```

**Descrizione:** Muove la telecamera verso destra con la velocità specificata.

**Parametri:**
- `pan_speed`: Velocità Pan (1-18).
- `tilt_speed`: Velocità Tilt (1-17).

---

### **panTiltDriveStop**

```python
camera = CameraObject()
camera.panTilt.panTiltDriveStop()
```

**Descrizione:** Arresta il movimento Pan-Tilt.

---

### **panTiltAbsolutePosition**

```python
camera = CameraObject()
camera.panTilt.panTiltAbsolutePosition(pan_speed, tilt_speed, pan_position, tilt_position)
```

**Descrizione:** Muove la telecamera a una posizione assoluta specificata.

**Parametri:**
- `pan_speed`: Velocità Pan (1-18).
- `tilt_speed`: Velocità Tilt (1-17).
- `pan_position`: Posizione Pan (0x0000-0xFFFF).
- `tilt_position`: Posizione Tilt (0x0000-0xFFFF).

**Eccezioni:**
- Solleva un `ValueError` se i valori di posizione o velocità non sono validi.

---

### **panTiltRelativePosition**

```python
camera = CameraObject()
camera.panTilt.panTiltRelativePosition(pan_speed, tilt_speed, pan_position, tilt_position)
```

**Descrizione:** Muove la telecamera di una quantità relativa specificata.

**Parametri:**
- `pan_speed`: Velocità Pan (1-18).
- `tilt_speed`: Velocità Tilt (1-17).
- `pan_position`: Posizione Pan relativa (0x0000-0xFFFF).
- `tilt_position`: Posizione Tilt relativa (0x0000-0xFFFF).

---

### **panTiltHome**

```python
camera = CameraObject()
camera.panTilt.panTiltHome()
```

**Descrizione:** Riporta la telecamera alla posizione iniziale (Home).

---

### **panTiltReset**

```python
camera = CameraObject()
camera.panTilt.panTiltReset()
```

**Descrizione:** Esegue un reset del sistema Pan-Tilt.

---

### **panTiltRampCurve**

```python
camera = CameraObject()
camera.panTilt.panTiltRampCurve(value)
```

**Descrizione:** Imposta la curva di accelerazione/decelerazione per il movimento Pan-Tilt.

**Parametri:**
- `value`: Valore della curva (vedi documentazione della telecamera per i valori consentiti).

**Eccezioni:**
- Solleva un `ValueError` se il valore non è valido.

---

### **panTiltSlow**

```python
camera = CameraObject()
camera.panTilt.panTiltSlow(mode)
```

**Descrizione:** Attiva o disattiva la modalità lenta per i movimenti Pan-Tilt.

**Parametri:**
- `mode`: Modalità di abilitazione (`EnableStateEnum.ON` o `EnableStateEnum.OFF`).

---

### **panTiltLimitSet**

```python
camera = CameraObject()
camera.panTilt.panTiltLimitSet(position, pan_position, tilt_position)
```

**Descrizione:** Imposta i limiti per il movimento Pan-Tilt.

**Parametri:**
- `position`: Posizione del limite.
- `pan_position`: Posizione Pan (0x0000-0xFFFF).
- `tilt_position`: Posizione Tilt (0x0000-0xFFFF).

**Eccezioni:**
- Solleva un `ValueError` se i valori non sono validi.

---

### **panTiltLimitClear**

```python
camera = CameraObject()
camera.panTilt.panTiltLimitClear(position)
```

**Descrizione:** Cancella i limiti impostati per il movimento Pan-Tilt.

**Parametri:**
- `position`: Posizione del limite da cancellare.

**Eccezioni:**
- Solleva un `ValueError` se il valore non è valido.

---

## Note Tecniche

- **Validazione:** La classe implementa una validazione interna per i valori di velocità e posizione, sollevando eccezioni in caso di errori.
- **Range:**
  - Velocità Pan: 1-18.
  - Velocità Tilt: 1-17.
  - Posizioni Pan e Tilt: 0x0000-0xFFFF.

Questa documentazione fornisce una panoramica completa per sfruttare tutte le funzionalità della classe `PanTiltInterface`.

