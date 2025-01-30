import logging
from visca.cameraObject import CameraObject
from visca.dataStucture.messagePacker import MessagePacker
from visca.dictionary.enumerations import *
from visca.interfaces.exposureInterface import ExposureInterface
from visca.interfaces.colorInterface import ColorInterface



class CameraCommandTester:
    def __init__(self):
        self.camera = CameraObject()
        self.packer = MessagePacker()
        self.command_queue = []

        # Rilevazione automatica di metodi GET e SET per tutte le interfacce
        self.interfaces = {
            "exposure": self.camera.exposure,
            "color": self.camera.color,
            "zoom": self.camera.zoom,
            "focus": self.camera.focus,
            "panTilt": self.camera.panTilt,
            "system": self.camera.system
        }

        self.test_values = {
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
            "setHighSensitivity": EnableStateEnum.ON,
            "setWhiteBalanceMode": WhiteBalanceModeEnum.MANUAL,
            "setWBSpeed": 1,
            "setOffset": 0,
            "setRGain": 5,  # Valore specifico per il guadagno rosso
            "setBGain": 5,  # Valore specifico per il guadagno blu
            "setChromaSuppressMode": ChromaSuppressionEnum.STRONG,
            "setMatrixMode": MatrixSelectEnum.FL_LIGHT,
            "setLevel": 5,  # Valore specifico del livello colore
            "setPhase": 5,  # Valore specifico della fase colore
            "setRG": 5,  # Regolazione del canale R della matrice colore
            "setRB": 5,  # Regolazione del canale RB della matrice colore
            "setGR": 5,  # Regolazione del canale GR della matrice colore
            "setGB": 5,  # Regolazione del canale GB della matrice colore
            "setBR": 5,  # Regolazione del canale BR della matrice colore
            "setBG": 5,   # Regolazione del canale BG della matrice colore
            "setFocusMode": FocusModeEnum.AUTO,  # Modalità di messa a fuoco automatica
            "setFocusFarVariable": 5,  # Spostamento della messa a fuoco verso lontano
            "setFocusNearVariable": 5,  # Spostamento della messa a fuoco verso vicino
            "setFocusValue": 100,  # Valore specifico per la messa a fuoco (dipende dall'unità della camera)
            "setNearFocusLimit": 50,  # Limite minimo della messa a fuoco
            "setAfMode": AutoFocusModeEnum.NORMAL,  # Modalità autofocus normale
            "setAfSensitivity": AutoFocusSensitivityEnum.NORMAL,  # Sensibilità AF alta
            "setAfModeInterval": (AutoFocusOperationTime.NORMAL, 20),  # Tempo di intervallo AF (ipotetico)
            "setIrCorrection": EnableStateEnum.ON,  # Correzione IR attiva
            "setIRReceive": EnableStateEnum.ON,  # Abilita la ricezione IR
            "setHPhaseValue": 2,  # Imposta il valore di fase orizzontale
            "setImageFlip": EnableStateEnum.ON,  # Attiva la rotazione dell'immagine
            "setCameraID": 1,  # Imposta l'ID della camera (di default 1)
            "setMenuMode": EnableStateEnum.ON,  # Mostra il menu OSD
            "setIRCutFilter": EnableStateEnum.ON,  # Attiva il filtro IR-Cut
            "setTallyMode": EnableStateEnum.ON,  # Attiva la luce tally
            "setTallyLevel": TallyLevel.HIGH,  # Imposta il livello di intensità della tally
            "setHDMIColorSpace": HdmiColorFormatEnum.YCbCr,
            "setPowerState": EnableStateEnum.ON  # Accende la camera
        }

    def detect_methods(self, interface):
        """
        Rileva dinamicamente tutti i metodi GET e SET di una data interfaccia.
        """
        get_methods = {name: method for name, method in vars(interface.__class__).items() if callable(method) and name.startswith("get")}
        set_methods = {name: method for name, method in vars(interface.__class__).items() if callable(method) and name.startswith("set")}

        return get_methods, set_methods

    def enqueue_commands(self):
        """
        Raccoglie tutti i comandi GET e SET per ciascuna interfaccia, li esegue e li accoda alla lista dei test.
        """
        print("\n=== INIZIO TEST CAMERA COMMANDS ===\n")

        for interface_name, interface in self.interfaces.items():
            print(f"🔍 Scansione {interface_name.upper()} Interface...")
            get_methods, set_methods = self.detect_methods(interface)

            # Esegui tutti i metodi GET
            for method_name in get_methods:
                try:
                    method = getattr(interface, method_name)
                    cmd = method()
                    self.command_queue.append((interface_name, method_name, cmd))
                    print(f"[QUEUE GET] {method_name} → {cmd}")
                except Exception as e:
                    print(f"[ERRORE GET] {method_name}: {e}")
            skipped = []
            # Esegui tutti i metodi SET con i valori di test
            for method_name in set_methods:
                try:
                    method = getattr(interface, method_name)
                    if method_name in self.test_values:
                        param = self.test_values[method_name]
                        cmd = method(param) if not isinstance(param, tuple) else method(*param)
                        self.command_queue.append((interface_name, method_name, cmd))
                        print(f"[QUEUE SET] {method_name}({param}) → {cmd}")
                    else:
                        if "setDictionary" in method_name:
                            pass
                        else:
                            skipped.append(method_name)
                            print(f"[SKIPPED] Nessun valore di test per {method_name}")
                except Exception as e:

                    print(f"[ERRORE SET] {method_name}: {e}")
                    raise e

            print(skipped)

    def run_tests(self):
        """
        Esegue tutti i comandi accodati e genera il pacchetto VISCA per ciascuno.
        """
        print("\n=== INIZIO COSTRUZIONE PACCHETTI ===\n")

        for interface, method, command in self.command_queue:
            try:
                packed_command = self.packer.build_command(command)
                print(f"{interface}.{method} -> {command} -> {packed_command}")
            except Exception as e:
                print(f"[ERRORE PACKING] {method}: {e}")

        print("\n=== TEST COMPLETATI ===")


if __name__ == "__main__":
    tester = CameraCommandTester()
    tester.enqueue_commands()
    tester.run_tests()
