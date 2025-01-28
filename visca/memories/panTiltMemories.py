
from visca.dictionary.enumerations import *


class PanTiltMemories:

    _pan_speed: int
    _tilt_speed: int
    _pan_position: int
    _tilt_position: int
    _pan_tilt_slowMode: EnableStateEnum

    def __init__(self):
        self._pan_speed = 1
        self._tilt_speed = 1
        self._pan_position = 0
        self._tilt_position = 0
        self._pan_tilt_slowMode = EnableStateEnum.OFF

    @property
    def pan_speed(self):
        return self._pan_speed

    @pan_speed.setter
    def pan_speed(self, speed: int):
        self._pan_speed = speed

    @property
    def tilt_speed(self):
        return self._tilt_speed

    @tilt_speed.setter
    def tilt_speed(self, speed: int):
        self._tilt_speed = speed

    @property
    def pan_position(self):
        return self._pan_position

    @pan_position.setter
    def pan_position(self, position: int):
        self._pan_position = position

    @property
    def tilt_position(self):
        return self._tilt_position

    @tilt_position.setter
    def tilt_position(self, position: int):
        self._tilt_position = position

    @property
    def pan_tilt_slowMode(self):
        return self._pan_tilt_slowMode

    @pan_tilt_slowMode.setter
    def pan_tilt_slowMode(self, mode: EnableStateEnum):
        self._pan_tilt_slowMode = mode

    def serialize(self):
        return {
            "pan_speed": self._pan_speed,
            "tilt_speed": self._tilt_speed,
            "pan_position": self._pan_position,
            "tilt_position": self._tilt_position,
            "pan_tilt_slowMode": self._pan_tilt_slowMode,
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
        self._pan_speed = data.get("pan_speed", self._pan_speed)
        self._tilt_speed = data.get("tilt_speed", self._tilt_speed)
        self._pan_position = data.get("pan_position", self._pan_position)
        self._tilt_position = data.get("tilt_position", self._tilt_position)
        self._pan_tilt_slowMode = self.returnEnumerationFromSomething(data.get("pan_tilt_slowMode"), EnableStateEnum)