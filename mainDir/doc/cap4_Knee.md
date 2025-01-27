# Documentazione dei Comandi

## Panoramica

Il menu KNEE consente di regolare la funzione di compressione della gamma dinamica nelle alte luci, migliorando la qualità dell'immagine in condizioni di forte contrasto. È possibile configurare queste impostazioni manualmente o automaticamente, in base alle esigenze operative.

---

### **setKneeSetting**

```python
camera = CameraObject()
print(camera.knee.setKneeSetting(EnableStateEnum.ON))
# Output: Comando per attivare o disattivare l'impostazione del KNEE.
```

**Descrizione:** Abilita o disabilita la funzione KNEE. Quando è impostato su `True`, vengono visualizzate ulteriori opzioni di configurazione come `KNEE MODE`, `KNEE SLOPE` e `KNEE POINT`.

**Valori disponibili:**
- **EnableStateEnum.ON**: Abilita la funzione KNEE.
- **EnableStateEnum.OFF**: Disabilita la funzione KNEE.

:return: Comando Visca.

---

### **setKneeMode**

```python
camera = CameraObject()
print(camera.knee.setKneeMode(KneeEnum.AUTO))
# Output: Comando per impostare la modalità del KNEE.
```

**Descrizione:** Seleziona la modalità operativa del KNEE.

**Opzioni disponibili:**
- **KneeEnum.AUTO**: Il livello KNEE viene calcolato automaticamente in base al livello di luminosità.
- **KneeEnum.MANUAL**: Permette di regolare manualmente il livello KNEE.

:return: Comando Visca.

**N.b.:** La differenza fra KneeEnum e EnumMode è che nel manuale Visca auto è 0 in entrambi i  casi mentre la modalità manuale è 1 in EnumMode e 4 in KneeEnum. Per evitare confusione ho creato un enum specifico.

---

### **getKneeMode**

```python
camera = CameraObject()
print(camera.knee.getKneeMode())
# Output: Modalità attuale del KNEE.
```

**Descrizione:** Recupera la modalità attuale del KNEE.

:return: Modalità attuale.

---

### **setKneeSlope**

```python
camera = CameraObject()
print(camera.knee.setKneeSlope(-3))
# Output: Comando per impostare la pendenza del KNEE.
```

**Descrizione:** Regola il gradiente della pendenza del KNEE. Questo parametro controlla il tasso di compressione delle alte luci.

**Valori disponibili:**
- Da **-7** a **+7**.

**Nota:** Disponibile solo quando `KNEE MODE` è impostato su **MANUAL**.

:return: Comando Visca.

---

### **getKneeSlope**

```python
camera = CameraObject()
print(camera.knee.getKneeSlope())
# Output: Valore attuale della pendenza del KNEE.
```

**Descrizione:** Recupera il valore attuale della pendenza del KNEE.

:return: Valore della pendenza.

---

### **setKneePoint**

```python
camera = CameraObject()
print(camera.knee.setKneePoint(8))
# Output: Comando per impostare il punto del KNEE.
```

**Descrizione:** Regola il punto di inizio della compressione del KNEE.

**Valori disponibili:**
- Da **0** a **12**.

**Nota:** Disponibile solo quando `KNEE MODE` è impostato su **MANUAL**.

:return: Comando Visca.

---

### **getKneePoint**

```python
camera = CameraObject()
print(camera.knee.getKneePoint())
# Output: Valore attuale del punto del KNEE.
```

**Descrizione:** Recupera il valore attuale del punto del KNEE.

:return: Valore del punto.

---