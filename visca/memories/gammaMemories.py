from visca.dictionary.enumerations import *


class GammaMemories:

    _gamma_select: GammaLevelEnum
    _gamma_pattern_value: int
    _gamma_offset_value: dict
    _gamma_level_value: int
    _black_gamma_level_value: int
    _black_gamma_range_value: BlackGammaRAngeEnum
    _black_level: int
    _black_level_value: int

    def __init__(self):
        # Stato iniziale
        self._gamma_select = GammaLevelEnum.STD
        self._gamma_pattern_value = 0
        self._gamma_offset_value = {"polarity": GammaPolarityEnum.POSITIVE, "width": 0}
        self._gamma_level_value = 0
        self._black_gamma_level_value = 0
        self._black_gamma_range_value = BlackGammaRAngeEnum.MIDDLE
        self._black_level = 0
        self._black_level_value = 0

    @property
    def gamma_select(self):
        return self._gamma_select

    @gamma_select.setter
    def gamma_select(self, value):
        self._gamma_select = value

    @property
    def gamma_pattern_value(self):
        return self._gamma_pattern_value

    @gamma_pattern_value.setter
    def gamma_pattern_value(self, value):
        self._gamma_pattern_value = value

    @property
    def gamma_offset_value(self):
        return self._gamma_offset_value

    @gamma_offset_value.setter
    def gamma_offset_value(self, value: dict):
        self._gamma_offset_value = value

    @property
    def gamma_level_value(self):
        return self._gamma_level_value

    @gamma_level_value.setter
    def gamma_level_value(self, value):
        self._gamma_level_value = value

    @property
    def black_gamma_level_value(self):
        return self._black_gamma_level_value

    @black_gamma_level_value.setter
    def black_gamma_level_value(self, value):
        self._black_gamma_level_value = value

    @property
    def black_gamma_range_value(self):
        return self._black_gamma_range_value

    @black_gamma_range_value.setter
    def black_gamma_range_value(self, value:BlackGammaRAngeEnum):
        self._black_gamma_range_value = value

    @property
    def black_level_value(self):
        return self._black_level_value

    @black_level_value.setter
    def black_level_value(self, value):
        self._black_level_value = value

    def serialize(self):
        return {
            "gamma_select": self._gamma_select.name,
            "gamma_pattern_value": self._gamma_pattern_value,
            "gamma_offset_value": self._gamma_offset_value,
            "gamma_level_value": self._gamma_level_value,
            "black_gamma_level_value": self._black_gamma_level_value,
            "black_gamma_range_value": self._black_gamma_range_value,
            "black_level_value": self._black_level_value,
        }

    def deserialize(self, data):
        self.gamma_select = self.returnEnumerationFromSomething(data.get("gamma_select"), GammaLevelEnum)
        self.gamma_pattern_value = data.get("gamma_pattern_value", self.gamma_pattern_value)
        self.gamma_offset_value = data.get("gamma_offset_value", self.gamma_offset_value)
        self.gamma_level_value = data.get("gamma_level_value", self.gamma_level_value)
        self.black_gamma_level_value = data.get("black_gamma_level_value", self.black_gamma_level_value)
        self.black_gamma_range_value = data.get("black_gamma_range_value", self.black_gamma_range_value)
        self.black_level_value = data.get("black_level_value", self.black_level_value)

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