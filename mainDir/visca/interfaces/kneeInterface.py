from mainDir.visca.dictionary.dictionaries import kneeDictionary
from mainDir.visca.dictionary.enumerations import *
from mainDir.visca.baseClasses.baseInterfaceClass import BaseInterfaceClass
from mainDir.visca.dataStucture.commandProcessor import CommandProcessor
from mainDir.visca.memories.kneeMemories import KneeMemories


class KneeInterface(BaseInterfaceClass):

    def __init__(self, _kneeMemories: KneeMemories, _kneeDictionary: dict):
        super().__init__()
        self.kneeMemories = _kneeMemories
        self.command_map = _kneeDictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setKneeSetting(self, mode: EnableStateEnum):
        """
        Abilita o disabilita il Knee Setting.

        Valori disponibili:
        - **2**: Disabilitato.
        - **3**: Abilitato.

        :param mode: Stato del Knee Setting ON/OFF.
        :return: Comando inviato.
        """

        self._last_command = None
        self.kneeMemories.knee_setting = mode
        return self.processor.set("knee_setting", mode.value)

    def getKneeSetting(self):
        self._last_command = "get knee_setting"
        return self.processor.inquire("knee_setting")

    # Knee Mode
    def setKneeMode(self, mode: KneeEnum):
        """
        Imposta la modalità Knee.

        Valori disponibili:
        - **0**: Modalità Auto.
        - **4**: Modalità Manual.

        :param mode:
        :param value: Modalità Knee.
        :return: Comando inviato.
        """

        self._last_command = None
        self.kneeMemories.knee_mode = mode
        return self.processor.set("knee_mode", mode.value)

    def getKneeMode(self):
        self._last_command = "get knee_mode"
        return self.processor.inquire("knee_mode")

    # Knee Slope Value
    def setKneeSlopeValue(self, value: int):
        """
        Imposta la pendenza (slope) del Knee.

        Valori disponibili:
        -7 a +7
        - **0-14**: Valori da 0x00 a 0x0E.

        :param value: Valore della pendenza.
        :return: Comando inviato.
        """
        if value < -7 or value > 7:
            raise ValueError("Valore fuori range per Knee Slope Value (-7, 7).")
        self._last_command = None
        self.kneeMemories.knee_slope_value = value
        value = value + 7
        return self.processor.set("knee_slope_value", value)

    def getKneeSlopeValue(self):
        self._last_command = "get knee_slope_value"
        return self.processor.inquire("knee_slope_value")

    # Knee Point Value
    def setKneePointValue(self, value: int):
        """
        Imposta il punto Knee.

        Valori disponibili:
        - **0-12**: Valori da 0x00 a 0x0C.

        :param value: Valore del punto Knee.
        :return: Comando inviato.
        """
        if value not in self.command_map["knee_point_value"]["allowed_values"]:
            raise ValueError("Valore fuori range per Knee Point Value.")
        self._last_command = None
        self.kneeMemories.knee_point_value = value
        return self.processor.set("knee_point_value", value)

    def getKneePointValue(self):
        self._last_command = "get knee_point_value"
        return self.processor.inquire("knee_point_value")

if __name__ == "__main__":
    kneeMemories = KneeMemories()
    kneeInterface = KneeInterface(kneeMemories, kneeDictionary)

    print("\nTESTING setKneeSetting")
    print(kneeInterface.setKneeSetting(EnableStateEnum.OFF))
    print(kneeInterface.setKneeSetting(EnableStateEnum.ON))

    print("\nTESTING getKneeSetting")
    print(kneeInterface.getKneeSetting())

    print("\nTESTING setKneeMode")
    print(kneeInterface.setKneeMode(KneeEnum.AUTO))
    print(kneeInterface.setKneeMode(KneeEnum.MANUAL))

    print("\nTESTING getKneeMode")
    print(kneeInterface.getKneeMode())

    print("\nTESTING setKneeSlopeValue")
    print(kneeInterface.setKneeSlopeValue(0))
    print(kneeInterface.setKneeSlopeValue(-7))
    print(kneeInterface.setKneeSlopeValue(7))

    print("\nTESTING getKneeSlopeValue")
    print(kneeInterface.getKneeSlopeValue())

    print("\nTESTING setKneePointValue")
    print(kneeInterface.setKneePointValue(0))
    print(kneeInterface.setKneePointValue(12))
    print(kneeInterface.setKneePointValue(6))

    print("\nTESTING getKneePointValue")
    print(kneeInterface.getKneePointValue())