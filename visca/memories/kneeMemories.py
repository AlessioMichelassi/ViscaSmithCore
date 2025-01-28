from visca.dictionary.enumerations import *


class KneeMemories:
    # Valori di default
    _knee_setting : EnableStateEnum
    _knee_mode : KneeEnum
    _knee_slope_value : int
    _knee_point_value : int

    def __init__(self):
        self._knee_setting = EnableStateEnum.OFF
        self._knee_mode = KneeEnum.AUTO
        self._knee_slope_value = 0
        self._knee_point_value = 0

    @property
    def knee_setting(self):
        return self._knee_setting

    @knee_setting.setter
    def knee_setting(self, mode: EnableStateEnum):
        self._knee_setting = mode

    @property
    def knee_mode(self):
        return self._knee_mode

    @knee_mode.setter
    def knee_mode(self, mode: KneeEnum):
        self._knee_mode = mode

    @property
    def knee_slope_value(self):
        return self._knee_slope_value

    @knee_slope_value.setter
    def knee_slope_value(self, value: int):
        self._knee_slope_value = value

    @property
    def knee_point_value(self):
        return self._knee_point_value

    @knee_point_value.setter
    def knee_point_value(self, value: int):
        self._knee_point_value = value

    def serialize(self):
        return {
            "knee_setting": self._knee_setting,
            "knee_mode": self._knee_mode,
            "knee_slope_value": self._knee_slope_value,
            "knee_point_value": self._knee_point_value
        }

    def deserialize(self, data):
        try :
            self._knee_setting = self.returnEnumerationFromSomething(data["knee_setting"], EnableStateEnum)
            self._knee_mode = self.returnEnumerationFromSomething(data["knee_mode"], EnumMode)
            self._knee_slope_value = data["knee_slope_value"]
            self._knee_point_value = data["knee_point_value"]

        except KeyError as e:
            print(f"KeyError: {e}")

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

