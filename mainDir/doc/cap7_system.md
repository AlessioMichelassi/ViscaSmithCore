# Documentazione dei Comandi - System Interface

## **Panoramica**
La classe `SystemInterface` permette di gestire varie configurazioni del sistema della telecamera tramite comandi VISCA. Offre metodi per configurare parametri fondamentali come lo stato di alimentazione, il filtro IR, la modalità menu, e molti altri. Qui sotto trovi la documentazione dettagliata dei comandi disponibili.

---

### **IR Receive**

```python
camera = CameraObject()
print(camera.system.setIRReceive(EnableStateEnum.ON))
# Output: Comando per abilitare la ricezione IR.
```

**Descrizione:** Abilita o disabilita la ricezione dei segnali IR.

**Valori disponibili:**
- **EnableStateEnum.ON**: Ricezione IR abilitata.
- **EnableStateEnum.OFF**: Ricezione IR disabilitata.

---

### **H Phase Up**

```python
camera = CameraObject()
print(camera.system.hPhaseUp())
# Output: Incrementa il valore di H Phase.
```

**Descrizione:** Incrementa il valore di `H Phase` di 1, fino al massimo consentito (959).

---

### **H Phase Down**

```python
camera = CameraObject()
print(camera.system.hPhaseDown())
# Output: Decrementa il valore di H Phase.
```

**Descrizione:** Decrementa il valore di `H Phase` di 1, fino al minimo consentito (0).

---

### **Set H Phase Value**

```python
camera = CameraObject()
print(camera.system.setHPhaseValue(500))
# Output: Comando per impostare il valore di H Phase.
```

**Descrizione:** Imposta manualmente il valore di `H Phase`.

**Valori disponibili:**
- Da **0** a **959**.

---

### **Image Flip**

```python
camera = CameraObject()
print(camera.system.setImageFlip(EnableStateEnum.ON))
# Output: Comando per abilitare l'immagine capovolta.
```

**Descrizione:** Attiva o disattiva la funzione di capovolgimento immagine.

**Valori disponibili:**
- **EnableStateEnum.ON**: Capovolgimento immagine abilitato.
- **EnableStateEnum.OFF**: Capovolgimento immagine disabilitato.

---

### **Set Camera ID**

```python
camera = CameraObject()
print(camera.system.setCameraID(0x1234))
# Output: Comando per impostare l'ID della telecamera.
```

**Descrizione:** Imposta l'ID della telecamera.

**Valori disponibili:**
- Da **0x0000** a **0xFFFF**.

---

### **Menu Mode**

```python
camera = CameraObject()
print(camera.system.setMenuMode(EnableStateEnum.ON))
# Output: Comando per abilitare la modalità menu.
```

**Descrizione:** Attiva o disattiva la modalità menu.

**Valori disponibili:**
- **EnableStateEnum.ON**: Modalità menu abilitata.
- **EnableStateEnum.OFF**: Modalità menu disabilitata.

---

### **Menu Enter**

```python
camera = CameraObject()
print(camera.system.menuEnter())
# Output: Comando per accedere al menu.
```

**Descrizione:** Invia il comando per entrare nel menu della telecamera.

---

### **IR Cut Filter**

```python
camera = CameraObject()
print(camera.system.setIRCutFilter(EnableStateEnum.NIGHT))
# Output: Comando per impostare il filtro IR.
```

**Descrizione:** Imposta il filtro IR per modalità giorno/notte.

**Valori disponibili:**
- **EnableStateEnum.DAY**: Modalità giorno.
- **EnableStateEnum.NIGHT**: Modalità notte.
- **EnableStateEnum.AUTO**: Modalità automatica.

---

### **Tally Mode**

```python
camera = CameraObject()
print(camera.system.setTallyMode(EnableStateEnum.ON))
# Output: Comando per abilitare il Tally Mode.
```

**Descrizione:** Attiva o disattiva la modalità Tally.

**Valori disponibili:**
- **EnableStateEnum.ON**: Tally Mode abilitato.
- **EnableStateEnum.OFF**: Tally Mode disabilitato.

---

### **Set Tally Level**

```python
camera = CameraObject()
print(camera.system.setTallyLevel(TallyLevel.HIGH))
# Output: Comando per impostare il livello di Tally.
```

**Descrizione:** Imposta il livello di Tally.

**Valori disponibili:**
- **TallyLevel.HIGH**: Livello alto.
- **TallyLevel.LOW**: Livello basso.

---

### **HDMI Color Space**

```python
camera = CameraObject()
print(camera.system.setHDMIColorSpace(HdmiColorFormatEnum.RGB))
# Output: Comando per impostare il colore HDMI.
```

**Descrizione:** Imposta il formato colore HDMI.

**Valori disponibili:**
- **HdmiColorFormatEnum.RGB**: Spazio colore RGB.
- **HdmiColorFormatEnum.YUV422**: Spazio colore YUV422.

---

### **Power State**

```python
camera = CameraObject()
print(camera.system.setPowerState(EnableStateEnum.ON))
# Output: Comando per accendere la telecamera.
```

**Descrizione:** Accende o spegne la telecamera.

**Valori disponibili:**
- **EnableStateEnum.ON**: Accensione.
- **EnableStateEnum.STANDBY**: Modalità standby.

---

### **Inquire Camera Generation**

```python
camera = CameraObject()
print(camera.system.inquireCameraGeneration())
# Output: Informazioni sulla generazione della telecamera.
```

**Descrizione:** Recupera la generazione della telecamera.

---

### **Inquire Software Version**

```python
camera = CameraObject()
print(camera.system.inquireSoftwareVersion())
# Output: Versione del software della telecamera.
```

**Descrizione:** Recupera la versione del software attualmente installata.

---

