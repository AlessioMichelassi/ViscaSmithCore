from visca.dictionary.enumerations import *


class FocusMemories:

    _focus_mode: FocusModeEnum
    _focus_value: int
    _af_mode: AutoFocusModeEnum
    _af_sensitivity: AutoFocusSensitivityEnum
    _ir_correction: IRCorrectionEnum

    def __init__(self):
        self._focus_mode = FocusModeEnum.AUTO
        self._focus_value = 0
        self._af_mode = AutoFocusModeEnum.NORMAL
        self._af_sensitivity = AutoFocusSensitivityEnum.NORMAL
        self._ir_correction = IRCorrectionEnum.STANDARD

    @property
    def focus_mode(self):
        return self._focus_mode

    @focus_mode.setter
    def focus_mode(self, mode: FocusModeEnum):
        self._focus_mode = mode

    @property
    def focus_value(self):
        return self._focus_value

    @focus_value.setter
    def focus_value(self, value: int):
        self._focus_value = value

    @property
    def af_mode(self):
        return self._af_mode

    @af_mode.setter
    def af_mode(self, mode: AutoFocusModeEnum):
        self._af_mode = mode

    @property
    def af_sensitivity(self):
        return self._af_sensitivity

    @af_sensitivity.setter
    def af_sensitivity(self, sensitivity: AutoFocusSensitivityEnum):
        self._af_sensitivity = sensitivity

    @property
    def ir_correction(self):
        return self._ir_correction

    @ir_correction.setter
    def ir_correction(self, correction: IRCorrectionEnum):
        self._ir_correction = correction

    def serialize(self):
        return {
            "focus_mode": self._focus_mode.value,
            "focus_value": self._focus_value,
            "af_mode": self._af_mode.value,
            "af_sensitivity": self._af_sensitivity,
            "ir_correction": self._ir_correction
        }

    @staticmethod
    def returnEnumerationFromSomething(something, enumeration):
        """
        Converte un valore in un'istanza dell'enumerazione specificata.

        :param something: Il valore da convertire.
        :param enumeration: L'enumerazione target.
        :return: Un'istanza dell'enumerazione.
        :raises ValueError: Se la conversione non è possibile.
        """
        try:
            if isinstance(something, enumeration):
                return something  # È già un'istanza dell'enumerazione
            elif isinstance(something, int):
                return enumeration(something)  # Converte direttamente dall'intero
            elif isinstance(something, str):
                # Prova prima a convertire dal nome dell'enumerazione
                if something in enumeration.__members__:
                    return enumeration[something]
                # Se non è un nome, prova a convertirlo in un intero
                num = int(something)
                return enumeration(num)
            else:
                raise ValueError(f"Impossibile convertire il valore '{something}' in {enumeration.__name__}.")
        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Errore durante la conversione di '{something}' in {enumeration.__name__}: {e}")

    def deserialize(self, data):
        self._focus_mode = self.returnEnumerationFromSomething(data.get("focus_mode"), FocusModeEnum)
        self._focus_value = data.get("focus_value")
        self._af_mode = self.returnEnumerationFromSomething(data.get("af_mode"), AutoFocusModeEnum)
        self._af_sensitivity = self.returnEnumerationFromSomething(data.get("af_sensitivity"), AutoFocusSensitivityEnum)
        self._ir_correction = self.returnEnumerationFromSomething(data.get("ir_correction"), IRCorrectionEnum)