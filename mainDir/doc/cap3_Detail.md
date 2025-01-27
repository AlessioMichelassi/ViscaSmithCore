# Documentazione dei Comandi

## Panoramica

Il menu DETAIL consente di regolare la funzione di miglioramento dell'immagine. Questo comando permette di controllare nitidezza, contrasto e contorni per ottimizzare la qualità visiva dell'immagine. Può essere configurato sia tramite il menu della telecamera che attraverso il protocollo VISCA.

---

### **setDetailMode**

```python
camera = CameraObject()
print(camera.detail.setDetailMode(mode))
# Output: Comando per impostare la modalità del dettaglio.
```

**Descrizione:** Utilizzando la modalità automatica [AUTO], la telecamera regola automaticamente il livello di dettaglio in base alla scena. In questa modalità è disponibile solo il comando `setDetailLevel`.

**Opzioni disponibili:**
- **AUTO**: La telecamera regola automaticamente il segnale di correzione del contorno.
- **MANUAL**: Permette di regolare manualmente i parametri del dettaglio.

:return: Comando Visca.

---

### **getDetailMode**

```python
camera = CameraObject()
print(camera.detail.getDetailMode())
# Output: Comando Visca per ottenere la modalità del dettaglio.
```

**Descrizione:** Recupera la modalità attuale del dettaglio.

:return: Comando Visca.

---

### **resetDetailLevel**

```python
camera = CameraObject()
print(camera.detail.resetDetailLevel())
# Output: Comando per resettare il livello di dettaglio.
```

**Descrizione:** Reimposta il livello di dettaglio al valore predefinito (0).

:return: Comando Visca.

---

### **setDetailLevel**

```python
camera = CameraObject()
print(camera.detail.setDetailLevel(value))
# Output: Comando per impostare il livello di dettaglio.
```

**Descrizione:** Imposta il volume del segnale di correzione del contorno.

**Valori disponibili:**
- Da **-7** a **+8**.

:return: Comando Visca.

---

### **getDetailLevel**

```python
camera = CameraObject()
print(camera.detail.getDetailLevel())
# Output: Comando per ottenere il livello di dettaglio.
```

**Descrizione:** Recupera il livello attuale del dettaglio.

:return: Comando Visca.

---

### **setDetailBandwidth**

```python
camera = CameraObject()
print(camera.detail.setDetailBandwidth(value))
# Output: Comando per impostare la larghezza di banda del dettaglio.
```

**Descrizione:** Imposta l'ampiezza di banda per i segnali di correzione del contorno.

**Opzioni disponibili:**
- **DEFAULT**, **LOW**, **MIDDLE**, **HIGH**, **WIDE**.

:return: Comando Visca.

---

### **getDetailBandwidth**

```python
camera = CameraObject()
print(camera.detail.getDetailBandwidth())
# Output: Larghezza di banda del dettaglio.
```

**Descrizione:** Recupera la larghezza di banda attuale del dettaglio.

:return: Comando Visca.

---

### **setDetailCrispening**

```python
camera = CameraObject()
print(camera.detail.setDetailCrispening(value))
# Output: Comando per impostare il valore di crispening del dettaglio.
```

**Descrizione:** Regola la finezza degli oggetti a cui vengono aggiunti segnali di correzione del contorno.

**Valori disponibili:**
- Da **0** a **7**.

:return: Comando Visca.

---

### **getDetailCrispening**

```python
camera = CameraObject()
print(camera.detail.getDetailCrispening())
# Output: Valore di crispening del dettaglio.
```

**Descrizione:** Recupera il valore attuale di crispening del dettaglio.

:return: Comando Visca.

---

### **setDetailHVBalance**

```python
camera = CameraObject()
print(camera.detail.setDetailHVBalance(value))
# Output: Comando per impostare il bilanciamento orizzontale e verticale del dettaglio.
```

**Descrizione:** Regola il rapporto tra gli elementi di correzione del contorno orizzontali e verticali.

**Valori disponibili:**
- Da **-2** a **+2**.

:return: Comando Visca.

---

### **getDetailHVBalance**

```python
camera = CameraObject()
print(camera.detail.getDetailHVBalance())
# Output: Bilanciamento orizzontale e verticale del dettaglio.
```

**Descrizione:** Recupera il bilanciamento attuale tra elementi di correzione orizzontali e verticali.

:return: Comando Visca.

---

### **setDetailBWBalance**

```python
camera = CameraObject()
print(camera.detail.setDetailBWBalance(value))
# Output: Comando per impostare il bilanciamento bianco e nero del dettaglio.
```

**Descrizione:** Regola il bilanciamento tra contorni in nero e bianco.

**Valori disponibili:**
- **TYPE0** (nero) a **TYPE4** (bianco).

:return: Comando Visca.

---

### **getDetailBWBalance**

```python
camera = CameraObject()
print(camera.detail.getDetailBWBalance())
# Output: Valore attuale del bilanciamento bianco e nero.
```

**Descrizione:** Recupera il valore attuale del bilanciamento bianco e nero.

:return: Comando Visca.

---

### **setDetailLimit**

```python
camera = CameraObject()
print(camera.detail.setDetailLimit(value))
# Output: Comando per impostare il limite del dettaglio.
```

**Descrizione:** Imposta il valore massimo per la quantità di enfasi del contorno.

**Valori disponibili:**
- Da **0** a **7**.

:return: Comando Visca.

---

### **getDetailLimit**

```python
camera = CameraObject()
print(camera.detail.getDetailLimit())
# Output: Limite del dettaglio.
```

**Descrizione:** Recupera il valore limite attuale del dettaglio.

:return: Comando Visca.

---

### **setDetailHighlight**

```python
camera = CameraObject()
print(camera.detail.setDetailHighlight(value))
# Output: Comando per impostare il livello di evidenziazione del dettaglio.
```

**Descrizione:** Regola il livello di contorno aggiunto ai soggetti molto luminosi.

**Valori disponibili:**
- Da **0** a **4**.

:return: Comando Visca.

---

### **getDetailHighlight**

```python
camera = CameraObject()
print(camera.detail.getDetailHighlight())
# Output: Valore attuale dell'evidenziazione del dettaglio.
```

**Descrizione:** Recupera il livello attuale di evidenziazione del dettaglio.

:return: Comando Visca.

---

### **setDetailSuperLow**

```python
camera = CameraObject()
print(camera.detail.setDetailSuperLow(value))
# Output: Comando per impostare il valore Super Low del dettaglio.
```

**Descrizione:** Enfatizza i contorni nell'intervallo super basso.

**Valori disponibili:**
- Da **0** a **7**.

:return: Comando Visca.

---

### **getDetailSuperLow**

```python
camera = CameraObject()
print(camera.detail.getDetailSuperLow())
# Output: Modalità Super Low del dettaglio.
```

**Descrizione:** Recupera il valore attuale dell'enfasi super bassa.

:return: Comando Visca.

---

