# Documentazione dei Comandi Generics

## Panoramica

Il menu GENERICS offre una serie di funzioni avanzate per ottimizzare la qualità delle immagini, tra cui riduzione del rumore, stabilizzatore d'immagine e gestione del filtro IR. Queste impostazioni possono essere regolate per adattarsi a diverse condizioni di ripresa e preferenze estetiche.

---

### **Picture Profile**

#### **setPictureProfile**

```python
camera = CameraObject()
print(camera.generics.setPictureProfile(PictureProfileEnum.PP1))
# Output: Comando per impostare il profilo immagine.
```

**Descrizione:** Imposta il profilo immagine della telecamera.

**Valori disponibili:**
Il valore deve essere specificato utilizzando l'enumerazione `PictureProfileEnum`, che include le seguenti opzioni:
- **PictureProfileEnum.PP1**
- **PictureProfileEnum.PP2**
- **PictureProfileEnum.PP3**
- **PictureProfileEnum.PP4**
- **PictureProfileEnum.PP5**
- **PictureProfileEnum.PP6**

:return: Comando Visca.

---

#### **getPictureProfile**

```python
camera = CameraObject()
print(camera.generics.getPictureProfile())
# Output: Profilo immagine attuale.
```

**Descrizione:** Recupera il profilo immagine attualmente impostato.

:return: Profilo immagine attuale.

---

### **Defog**

#### **setDefog**

```python
camera = CameraObject()
print(camera.generics.setDefog(EnableStateEnum.ON, 2))
# Output: Comando per attivare la modalità Defog con livello specifico.
```

**Descrizione:** Attiva o disattiva la modalità Defog e ne regola il livello.

**Valori disponibili:**
- **EnableStateEnum.ON**: Modalità attiva.
- **EnableStateEnum.OFF**: Modalità disattiva.
- **Livello**: Valore tra 0 e 2.

**Note:**
- I livelli fuori range generano un errore.

:return: Comando Visca.

---

#### **getDefog**

```python
camera = CameraObject()
print(camera.generics.getDefog())
# Output: Stato e livello della modalità Defog.
```

**Descrizione:** Recupera lo stato attuale della modalità Defog e il suo livello.

:return: Stato e livello della modalità Defog.

---

### **Noise Reduction**

#### **setNoiseReductionLevel**

```python
camera = CameraObject()
print(camera.generics.setNoiseReductionLevel(NoiseReductionLevel.STRONG))
# Output: Comando per impostare il livello di riduzione del rumore.
```

**Descrizione:** Imposta il livello di riduzione del rumore.

**Valori disponibili:**
Il valore deve essere specificato utilizzando l'enumerazione `NoiseReductionLevel`, che include le seguenti opzioni:
- **NoiseReductionLevel.OFF**
- **NoiseReductionLevel.WEAK**
- **NoiseReductionLevel.NR_2**
- **NoiseReductionLevel.NR_3**
- **NoiseReductionLevel.NR_4**
- **NoiseReductionLevel.STRONG**
- **NoiseReductionLevel.ENABLE_2D_3D_NR**

:return: Comando Visca.

---

#### **getNoiseReductionLevel**

```python
camera = CameraObject()
print(camera.generics.getNoiseReductionLevel())
# Output: Livello attuale di riduzione del rumore.
```

**Descrizione:** Recupera il livello attuale di riduzione del rumore.

:return: Livello di riduzione del rumore attuale.

---

#### **set2D3DNoiseReduction**

```python
camera = CameraObject()
print(camera.generics.set2D3DNoiseReduction(NoiseReduction2DEnum.WEAK, NoiseReduction3DEnum.STRONG))
# Output: Comando per impostare i livelli di riduzione del rumore 2D e 3D.
```

**Descrizione:** Regola i livelli di riduzione del rumore per 2D e 3D.

**Valori disponibili:**
- **NoiseReduction2DEnum**: Include valori da OFF a STRONG.
- **NoiseReduction3DEnum**: Include valori da OFF a STRONG.

:return: Comando Visca.

---

#### **get2D3DNoiseReduction**

```python
camera = CameraObject()
print(camera.generics.get2D3DNoiseReduction())
# Output: Livelli attuali di riduzione del rumore 2D e 3D.
```

**Descrizione:** Recupera i livelli attuali di riduzione del rumore per 2D e 3D.

:return: Livelli di riduzione del rumore 2D e 3D.

---

### **Picture Effect**

#### **setPictureEffect**

```python
camera = CameraObject()
print(camera.generics.setPictureEffect(PictureEffectEnum.SEPIA))
# Output: Comando per impostare l'effetto immagine.
```

**Descrizione:** Imposta l'effetto immagine desiderato.

**Valori disponibili:**
Il valore deve essere specificato utilizzando l'enumerazione `PictureEffectEnum`.

:return: Comando Visca.

---

#### **getPictureEffect**

```python
camera = CameraObject()
print(camera.generics.getPictureEffect())
# Output: Effetto immagine attuale.
```

**Descrizione:** Recupera l'effetto immagine attualmente impostato.

:return: Effetto immagine attuale.

---

### **Color Bar**

#### **setColorBar**

```python
camera = CameraObject()
print(camera.generics.setColorBar(EnableStateEnum.ON))
# Output: Comando per attivare/disattivare la barra colore.
```

**Descrizione:** Attiva o disattiva la barra colore per i test video.

**Valori disponibili:**
- **EnableStateEnum.ON**: Barra colore attivata.
- **EnableStateEnum.OFF**: Barra colore disattivata.

:return: Comando Visca.

---

#### **getColorBar**

```python
camera = CameraObject()
print(camera.generics.getColorBar())
# Output: Stato attuale della barra colore.
```

**Descrizione:** Recupera lo stato attuale della barra colore.

:return: Stato della barra colore.

---

