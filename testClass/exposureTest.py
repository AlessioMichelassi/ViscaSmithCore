import logging
import time
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from visca.cameraObject import CameraObject
from visca.client.clientObject import ClientObject
from visca.dictionary.enumerations import *

logging.basicConfig(level=logging.DEBUG)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 52381

if __name__ == "__main__":
    app = QApplication([])


    def handleError(error):
        logging.error(f"❌ ERRORE RILEVATO: {error}")
        global command_queue  # Per svuotare la coda in caso di errore critico
        command_queue = []  # Interrompe l'esecuzione dei comandi rimanenti
        logging.error("🛑 Arresto della coda di test a causa di un errore critico.")
        app.quit()  # Esce dal ciclo di esecuzione di PyQt


    camera = CameraObject()
    client = ClientObject(camera)
    client.connectToServer(SERVER_HOST, SERVER_PORT)

    # Collegamento ai segnali per debug
    client.error_SIGNAL.connect(handleError)
    client.info_SIGNAL.connect(print)
    client.serverMessage.connect(print)

    # Rilevazione automatica di metodi GET e SET
    get_methods = {name: method for name, method in vars(camera.exposure.__class__).items() if callable(method) and name.startswith("get")}
    set_methods = {name: method for name, method in vars(camera.exposure.__class__).items() if callable(method) and name.startswith("set")}

    logging.info(f"🔍 Trovati {len(get_methods)} metodi GET e {len(set_methods)} metodi SET.")

    # Mappa valori di test per i metodi SET
    test_values = {
        "setExposureMode": ExposureModeEnum.MANUAL,
        "setIrisValue": IrisSettingsEnum.F2_0,
        "setGainValue": GainValueEnum.GAIN_0DB,
        "setGainLimit": GainValueEnum.GAIN_0DB,
        "setGainPointMode": EnableStateEnum.ON,
        "setGainPointValue": GainValueEnum.GAIN_0DB,
        "setShutterValue": 2,
        "setMaxShutter": ShutterSpeedEnum_60.s1_350,
        "setMinShutter": ShutterSpeedEnum_60.s1_1,
        "setAeSpeedValue": 1,
        "setAutoSlowShutterMode": EnableStateEnum.ON,
        "setExposureCompensationMode": EnableStateEnum.ON,
        "setExposureCompensationValue": 0,
        "setBacklightMode": EnableStateEnum.ON,
        "setSpotlightMode": EnableStateEnum.ON,
        "setVisibilityEnhancerMode": EnableStateEnum.ON,
        "setVisibilityEnhancerLevel": (
            VisibilityEnhancerEffectLevel.NORMAL,
            VisibilityEnhancerBrightnessCompensation.STANDARD,
            VisibilityEnhancerCompensationLevel.LOW
        ),
        "setLowLightBiasMode": EnableStateEnum.ON,
        "setLowLightBiasLevel": LowLightBiasLevel.LLB_04,
        "setHighSensitivity": EnableStateEnum.ON
    }

    # Costruzione dinamica della coda di comandi
    command_queue = []

    # Aggiungi i comandi GET alla coda
    for method_name in get_methods:
        try:
            method = getattr(camera.exposure, method_name)
            cmd = method()
            command_queue.append(cmd)
            logging.info(f"[QUEUE GET] {method_name} → {cmd}")
        except Exception as e:
            logging.error(f"[ERRORE GET] {method_name}: {e}")

    # Aggiungi i comandi SET alla coda con i valori di test
    for method_name in set_methods:
        try:
            method = getattr(camera.exposure, method_name)
            if method_name in test_values:
                param = test_values[method_name]
                cmd = method(param) if not isinstance(param, tuple) else method(*param)
                command_queue.append(cmd)
                logging.info(f"[QUEUE SET] {method_name}({param}) → {cmd}")
            else:
                logging.warning(f"[SKIPPED] Nessun valore di test per {method_name}")
        except Exception as e:
            logging.error(f"[ERRORE SET] {method_name}: {e}")

    def send_next_command():
        """Invia il comando successivo nella coda al client VISCA."""
        if command_queue:
            cmd = command_queue.pop(0)
            client.enqueueViscaString(cmd)
            logging.info(f"\n\t******** ")
            logging.info(f"\t******** SENDING: {cmd}")
            logging.info(f"\t******** ")
            QTimer.singleShot(500, send_next_command)  # Aspetta 500ms prima di inviare il prossimo comando
        else:
            logging.info("✅ Test completato, nessun altro comando nella coda.")

    # Avvia l'invio dei comandi dopo un piccolo ritardo
    QTimer.singleShot(2000, send_next_command)

    app.exec()
