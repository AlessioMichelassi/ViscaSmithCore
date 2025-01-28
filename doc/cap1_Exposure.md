# Exposure

## Panoramica
Il sistema di controllo dell'esposizione permette di generare comandi Visca per regolare vari parametri relativi all'esposizione dell'immagine, come il guadagno, la velocità dell'otturatore elettronico e il diaframma. Questi comandi possono essere utilizzati per configurazioni automatiche, semi-automatiche o manuali a seconda delle esigenze operative.

Tutti i comandi Visca generati dal sistema di controllo dell'esposizione possono essere inviati direttamente alla camera tramite il protocollo di comunicazione Visca.

Per i valori più comuni come on, off, auto sono state create delle enumerazioni e sono tutte contenute nel file `enumerations.py`. 
Queste classi sono utili per settare i valori dell'Iris, dello shutter, del gain e più in generale dove piuttosto che un valore ad esempio da 0 a 10 viene richiesta una serie di valori specifici,
come in exposure mode, dove i valori sono solo 4 ma non sono consecutivi, ovvero Auto è 0, mentre Manual è 3, e shutter priority è 10, mentre iris priority è 11.

Esistono tipicamente 4 modalità di esposizione: Manuale, automatica, priorità diaframma e priorità otturatore. Quando si scegli una modalità, alcuni comandi possono ritornare utili per regolare i parametri dell'automazione come i limiti minimi e massimi dello shutter, dell'iris e del gain.


---

## **EXPOSURE**

### **setExposureMode**
Restituisce il comando Visca per cambiare la modalità di esposizione. Il valore deve essere specificato utilizzando l'enumerazione `ExposureModeEnum`, che include le seguenti opzioni:
```python
camera = CameraObject()
print(camera.exposure.setExposureMode(ExposureModeEnum.MANUAL))
# Output: 01 04 39 03
```

- **FULL AUTO**
  - Comando Visca: `01 04 39 00`
  - L'esposizione viene regolata automaticamente agendo su:
    - Guadagno
    - Velocità dell'otturatore elettronico
    - Diaframma

- **MANUAL**
  - Comando Visca: `01 04 39 03`
  - L'utente può regolare manualmente:
    - Guadagno
    - Velocità dell'otturatore elettronico
    - Diaframma

- **SHUTTER PRIORITY**
  - Comando Visca: `01 04 39 0A`
  - L'utente può regolare manualmente la velocità dell'otturatore elettronico.
  - Il sistema regola automaticamente l'esposizione utilizzando il guadagno e il diaframma.

- **IRIS PRIORITY**
  - Comando Visca: `01 04 39 0B`
  - L'utente può regolare manualmente il diaframma.
  - Il sistema regola automaticamente l'esposizione utilizzando il guadagno e la velocità dell'otturatore elettronico.

Quando si seleziona una modalità, il comando Visca restituito può essere inviato alla camera per applicare le impostazioni desiderate.

---

## **Diaframma**

  I valori del diaframma sono definiti nell'enumerazione `IrisValueEnum`:


### **irisReset**
```python
camera = CameraObject()
print(camera.exposure.irisReset())
```
Restituisce il comando Visca per reimpostare il diaframma al valore di default.

### **irisUp**
```python
camera = CameraObject()
print(camera.exposure.irisUp())
```
Restituisce il comando Visca per aumentare il valore del diaframma.

### **irisDown**
```python
camera = CameraObject()
print(camera.exposure.irisDown())
```
Restituisce il comando Visca per diminuire il valore del diaframma.

### **setIrisValue(value)**
```python
camera = CameraObject()
print(camera.exposure.setIrisValue(IrisValueEnum.F4_0))
```
Restituisce il comando Visca per impostare manualmente un valore specifico per il diaframma.

### **getIris**
```python
camera = CameraObject()
print(camera.exposure.getIris())
```
Restituisce il comando Visca per ottenere il valore corrente del diaframma.

---

### **Funzioni di Controllo del Guadagno**

### **gainReset**
```python
camera = CameraObject()
print(camera.exposure.gainReset())
```
Restituisce il comando Visca per reimpostare il guadagno al valore di default.

### **gainUp**
```python
camera = CameraObject()
print(camera.exposure.gainUp())
```
Restituisce il comando Visca per aumentare il valore del guadagno.

### **gainDown**
```python
camera = CameraObject()
print(camera.exposure.gainDown())
```
Restituisce il comando Visca per diminuire il valore del guadagno.

### **setGainValue(value)**
```python
camera = CameraObject()
print(camera.exposure.setGainValue(GainValueEnum.GAIN_6DB))
```
Restituisce il comando Visca per impostare manualmente un valore specifico per il guadagno.

### **getGain**
```python
camera = CameraObject()
print(camera.exposure.getGain())
```
Restituisce il comando Visca per ottenere il valore corrente del guadagno.

### **setHighSensitivity(enabled)**
```python
camera = CameraObject()
print(camera.exposure.setHighSensitivity(EnableStateEnum.ON))
```
Restituisce il comando Visca per abilitare o disabilitare la modalità di alta sensibilità.

### **getHighSensitivity**
```python
camera = CameraObject()
print(camera.exposure.getHighSensitivity())
```
Restituisce il comando Visca per ottenere lo stato della modalità di alta sensibilità.

### **setGainLimit(limit)**
```python
camera = CameraObject()
print(camera.exposure.setGainLimit(GainLimitEnum.GAIN_18DB))
```
Restituisce il comando Visca per impostare un limite massimo per il guadagno.

### **getGainLimit**
```python
camera = CameraObject()
print(camera.exposure.getGainLimit())
```
Restituisce il comando Visca per ottenere il limite massimo impostato per il guadagno.

---

### **Funzioni di Controllo dell'Otturatore**

### **shutterReset**
```python
camera = CameraObject()
print(camera.exposure.shutterReset())
```
Restituisce il comando Visca per reimpostare la velocità dell'otturatore elettronico al valore di default.

### **shutterUp**
```python
camera = CameraObject()
print(camera.exposure.shutterUp())
```
Restituisce il comando Visca per aumentare la velocità dell'otturatore.

### **shutterDown**
```python
camera = CameraObject()
print(camera.exposure.shutterDown())
```
Restituisce il comando Visca per diminuire la velocità dell'otturatore.

### **setShutterValue(value)**
```python
camera = CameraObject()
print(camera.exposure.setShutterValue(ShutterValueEnum.SHUTTER_1_60))
```
Restituisce il comando Visca per impostare manualmente un valore specifico per la velocità dell'otturatore.

### **getShutter**
```python
camera = CameraObject()
print(camera.exposure.getShutter())
```
Restituisce il comando Visca per ottenere il valore corrente della velocità dell'otturatore.

### **setMaxShutter(value)**
```python
camera = CameraObject()
print(camera.exposure.setMaxShutter(ShutterValueEnum.SHUTTER_1_1000))
```
Restituisce il comando Visca per impostare un valore massimo per la velocità dell'otturatore.

### **getMaxShutter**
```python
camera = CameraObject()
print(camera.exposure.getMaxShutter())
```
Restituisce il comando Visca per ottenere il valore massimo impostato per la velocità dell'otturatore.

### **setMinShutter(value)**
```python
camera = CameraObject()
print(camera.exposure.setMinShutter(ShutterValueEnum.SHUTTER_1_1000))
```
Restituisce il comando Visca per impostare un valore minimo per la velocità dell'otturatore.

### **getMinShutter**
```python
camera = CameraObject()
print(camera.exposure.getMinShutter())
```
Restituisce il comando Visca per ottenere il valore minimo impostato per la velocità dell'otturatore.


### **setExposureCompensationMode(mode)**
```python
camera = CameraObject()
print(camera.exposure.setExposureCompensationMode(ExposureCompensationModeEnum.AUTO))
```
Restituisce il comando Visca per impostare la modalità di compensazione dell'esposizione.

### **getExposureCompensationMode**
```python
camera = CameraObject()
print(camera.exposure.getExposureCompensationMode())
```
Restituisce il comando Visca per ottenere la modalità di compensazione dell'esposizione corrente.

### **setExposureCompensationValue(value)**
```python
camera = CameraObject()
print(camera.exposure.setExposureCompensationValue(ExposureCompensationValueEnum.COMPENSATION_0_0))
```
Restituisce il comando Visca per impostare un valore specifico per la compensazione dell'esposizione.

### **getExposureCompensationValue**
```python
camera = CameraObject()
print(camera.exposure.getExposureCompensationValue())
```
Restituisce il comando Visca per ottenere il valore corrente della compensazione dell'esposizione.

### **exposureCompensationReset**
```python
camera = CameraObject()
print(camera.exposure.exposureCompensationReset())
```
Restituisce il comando Visca per reimpostare la compensazione dell'esposizione al valore di default.

### **exposureCompensationUp**
```python
camera = CameraObject()
print(camera.exposure.exposureCompensationUp())
```
Restituisce il comando Visca per aumentare il valore della compensazione dell'esposizione.

### **exposureCompensationDown**
```python
camera = CameraObject()
print(camera.exposure.exposureCompensationDown())
```
Restituisce il comando Visca per diminuire il valore della compensazione dell'esposizione.

---

### **Altre Funzionalità**

### **setBacklightMode(enabled)**
```python
camera = CameraObject()
print(camera.exposure.setBacklightMode(EnableStateEnum.ON))
```
Restituisce il comando Visca per abilitare o disabilitare la modalità di retroilluminazione.

### **getBacklightMode**
```python
camera = CameraObject()
print(camera.exposure.getBacklightMode())
```
Restituisce il comando Visca per ottenere lo stato della modalità di retroilluminazione.

### **setSpotlightMode(enabled)**
```python
camera = CameraObject()
print(camera.exposure.setSpotlightMode(EnableStateEnum.ON))
```
Restituisce il comando Visca per abilitare o disabilitare la modalità di illuminazione per soggetti in primo piano.

### **getSpotlightMode**
```python
camera = CameraObject()
print(camera.exposure.getSpotlightMode())
```
Restituisce il comando Visca per ottenere lo stato della modalità di illuminazione per soggetti in primo piano.

### **setVisibilityEnhancerMode(enabled)**
```python
camera = CameraObject()
print(camera.exposure.setVisibilityEnhancerMode(EnableStateEnum.ON))
```
Restituisce il comando Visca per abilitare o disabilitare il miglioramento della visibilità.

### **getVisibilityEnhancerMode**
```python
camera = CameraObject()
print(camera.exposure.getVisibilityEnhancerMode())
```
Restituisce il comando Visca per ottenere lo stato della modalità di miglioramento della visibilità.

### **setVisibilityEnhancerLevel(level)**
```python
camera = CameraObject()
print(camera.exposure.setVisibilityEnhancerLevel(VisibilityEnhancerLevelEnum.LEVEL_3))
```
Restituisce il comando Visca per impostare il livello di miglioramento della visibilità.

### **getVisibilityEnhancerLevel**
```python
camera = CameraObject()
print(camera.exposure.getVisibilityEnhancerLevel())
```
Restituisce il comando Visca per ottenere il livello di miglioramento della visibilità corrente.

### **setLowLightBiasMode(enabled)**
```python
camera = CameraObject()
print(camera.exposure.setLowLightBiasMode(EnableStateEnum.ON))
```
Restituisce il comando Visca per abilitare o disabilitare la modalità di bias per basse luci.

### **getLowLightBiasMode**
```python
camera = CameraObject()
print(camera.exposure.getLowLightBiasMode())
```
Restituisce il comando Visca per ottenere lo stato della modalità di bias per basse luci.

### **setLowLightBiasLevel(level)**
```python
camera = CameraObject()
print(camera.exposure.setLowLightBiasLevel(LowLightBiasLevelEnum.LEVEL_3))
```
Restituisce il comando Visca per impostare il livello di bias per basse luci.

### **getLowLightBiasLevel**
```python
camera = CameraObject()
print(camera.exposure.getLowLightBiasLevel())
```
Restituisce il comando Visca per ottenere il livello corrente di bias per basse luci.
