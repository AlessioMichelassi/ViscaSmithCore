from mainDir.visca.dictionary.enumerations import *


class ZoomMemories:

    _zoom_mode: ZoomModeEnum
    _zoom_speed: int
    _zoom_direct: int
    _tele_convert: EnableStateEnum



    def __init__(self):
        # Stato iniziale
        self._zoom_mode = ZoomModeEnum.OPTICAL
        self._zoom_speed = 0
        self._zoom_value = 0
        self._tele_convert = EnableStateEnum.OFF

    @property
    def zoom_mode(self):
        return self._zoom_mode

    @zoom_mode.setter
    def zoom_mode(self, mode: ZoomModeEnum):
        self._zoom_mode = mode

    @property
    def zoom_speed(self):
        return self._zoom_speed

    @zoom_speed.setter
    def zoom_speed(self, speed: int):
        self._zoom_speed = speed

    @property
    def zoom_value(self):
        return self._zoom_value

    @zoom_value.setter
    def zoom_value(self, value: int):
        self._zoom_value = value

    @property
    def tele_convert(self):
        return self._tele_convert

    @tele_convert.setter
    def tele_convert(self, state: EnableStateEnum):
        self._tele_convert = state

    def serialize(self):
        return {
            "zoom_mode": self._zoom_mode,
            "zoom_speed": self._zoom_speed,
            "zoom_value": self._zoom_value,
            "tele_convert": self._tele_convert
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
        self._zoom_mode = self.returnEnumerationFromSomething(data.get("zoom_mode"), ZoomModeEnum)
        self._zoom_speed = data.get("zoom_speed")
        self._zoom_value = data.get("zoom_value")
        self._tele_convert = self.returnEnumerationFromSomething(data.get("tele_convert"), EnableStateEnum)