# Documentazione dei Comandi

## Panoramica

Il menu GAMMA consente di regolare la curva di gamma, inclusi il tipo di curva, i livelli di compensazione e le regolazioni specifiche per il nero. Queste impostazioni permettono di ottimizzare la qualità dell'immagine per diverse condizioni di ripresa.

---

### **Gamma Select**

#### **setGammaSelect**

```python
camera = CameraObject()
print(camera.gamma.setGammaSelect(GammaLevelEnum.STD))
# Output: Comando per impostare il tipo di curva gamma.
```

**Descrizione:** Permette di scegliere il tipo di curva gamma.

**Opzioni disponibili:**
- **GammaLevelEnum.STD**: Impostazione standard per video.
- **GammaLevelEnum.STRAIGHT**: Curva gamma diritta.
- **GammaLevelEnum.PATTERN**: Usa uno dei 512 pattern di gamma disponibili.
- **GammaLevelEnum.MOVIE**: Curva ottimizzata per filmati.
- **GammaLevelEnum.STILL**: Curva per immagini statiche.
- **GammaLevelEnum.CINE1, CINE2, CINE3, CINE4**: Diverse configurazioni per tonalità e contrasto.
- **GammaLevelEnum.ITU709**: Curva conforme allo standard ITU-709.

:return: Comando Visca.

---

#### **getGammaSelect**

```python
camera = CameraObject()
print(camera.gamma.getGammaSelect())
# Output: Tipo di curva gamma attualmente impostato.
```

**Descrizione:** Recupera il tipo di curva gamma attualmente in uso.

:return: Comando Visca per ottenere il Tipo di curva gamma.

---

### **Gamma Pattern**

#### **setGammaPatternValue**

```python
camera = CameraObject()
print(camera.gamma.setGammaPatternValue(25))
# Output: Comando per impostare un pattern specifico di gamma.
```

**Descrizione:** Permette di selezionare un pattern di gamma.

**Valori disponibili:**
- **PATTERN**: Da **0** a **51** (intervallo valido per PATTERN).
- **PATTERN FINE**: Da **0** a **9**, con restrizioni basate su PATTERN.

:return: Comando Visca.

---

#### **getGammaPatternValue**

```python
camera = CameraObject()
print(camera.gamma.getGammaPatternValue())
# Output: Pattern attualmente selezionato.
```

**Descrizione:** Recupera il pattern attualmente selezionato.

:return: Comando Visca per ottenere il Pattern gamma attuale.

---

### **Gamma Offset**

#### **setGammaOffsetValue**

```python
camera = CameraObject()
print(camera.gamma.setGammaOffsetValue(-32))
# Output: Comando per impostare il valore di compensazione della gamma.
```

**Descrizione:** Regola l'offset del livello di uscita delle curve di gamma.

**Valori disponibili:**
- Da **-64** a **+64**.

:return: Comando Visca.

---

#### **getGammaOffsetValue**

```python
camera = CameraObject()
print(camera.gamma.getGammaOffsetValue())
# Output: Valore di compensazione attualmente impostato.
```

**Descrizione:** Recupera il valore attuale di compensazione della gamma.

:return: Comando Visca per ottenere il Valore offset gamma.

---

### **Gamma Level**

#### **setGammaLevelValue**

```python
camera = CameraObject()
print(camera.gamma.setGammaLevelValue(5))
# Output: Comando per impostare il livello di gamma.
```

**Descrizione:** Regola il livello di correzione della curva gamma.

**Valori disponibili:**
- Da **-7** a **+7**.

:return: Comando Visca.

---

#### **getGammaLevelValue**

```python
camera = CameraObject()
print(camera.gamma.getGammaLevelValue())
# Output: Livello di gamma attualmente impostato.
```

**Descrizione:** Recupera il livello attuale di correzione della gamma.

:return: Comando Visca per ottenere il Livello gamma attuale.

---

### **Black Gamma**

#### **setBlackGammaLevelValue**

```python
camera = CameraObject()
print(camera.gamma.setBlackGammaLevelValue(-5))
# Output: Comando per impostare il livello di gamma del nero.
```

**Descrizione:** Regola il livello di gamma del nero per controllare le sfumature nelle aree scure.

**Valori disponibili:**
- Da **-7** a **+7**.

:return: Comando Visca.

---

#### **getBlackGammaLevelValue**

```python
camera = CameraObject()
print(camera.gamma.getBlackGammaLevelValue())
# Output: Livello di gamma del nero attualmente impostato.
```

**Descrizione:** Recupera il livello attuale di gamma del nero.

:return: Comando Visca per ottenere il Livello di gamma nero attuale.

---

#### **setBlackGammaRangeValue**

```python
camera = CameraObject()
print(camera.gamma.setBlackGammaRangeValue(BlackGammaRAngeEnum.LOW))
# Output: Comando per impostare l'intervallo di gamma del nero.
```

**Descrizione:** Regola l'intervallo di luminosità in cui la gamma del nero è efficace.

**Opzioni disponibili:**
- **BlackGammaRAngeEnum.WIDE**: Intervallo ristretto.
- **BlackGammaRAngeEnum.MIDDLE**: Intervallo medio.
- **BlackGammaRAngeEnum.NARROW**: Intervallo ampio.

:return: Comando Visca.

---

#### **getBlackGammaRangeValue**

```python
camera = CameraObject()
print(camera.gamma.getBlackGammaRangeValue())
# Output: Intervallo di gamma del nero attualmente impostato.
```

**Descrizione:** Recupera l'intervallo di gamma del nero attualmente impostato.

:return: Comando Visca per ottenere l'Intervallo gamma nero attuale.

---

### **Black Level**

#### **setBlackLevelValue**

```python
camera = CameraObject()
print(camera.gamma.setBlackLevelValue(-15))
# Output: Comando per impostare il livello di nero master.
```

**Descrizione:** Regola il livello di nero master per l'immagine.

**Valori disponibili:**
- Da **-48** a **+48**.

:return: Comando Visca.

---

#### **getBlackLevelValue**

```python
camera = CameraObject()
print(camera.gamma.getBlackLevelValue())
# Output: Livello di nero master attualmente impostato.
```

**Descrizione:** Recupera il livello attuale di nero master.

:return:Comando Visca per ottenere il Livello nero attuale.

---

