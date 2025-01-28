from visca.dictionary.enumerations import *


class SystemMemories:

    _ir_receive: EnableStateEnum
    _h_phase_value: int
    _img_flip: EnableStateEnum
    _camera_id: int
    _menu_mode: EnableStateEnum
    _ir_cut_filter: EnableStateEnum
    _tally_mode: EnableStateEnum
    _tally_level: TallyLevel
    _hdmi_color_space: HdmiColorFormatEnum
    _power_state: int

    def __init__(self):
        # Variabili di stato
        self._ir_receive = EnableStateEnum.OFF
        self._h_phase_value = 0  # Default iniziale
        self._img_flip = EnableStateEnum.OFF
        self._camera_id = 0
        self._menu_mode = EnableStateEnum.OFF
        self._ir_cut_filter = EnableStateEnum .OFF
        self._tally_mode = EnableStateEnum .ON
        self._tally_level = TallyLevel.HIGH
        self._hdmi_color_space = HdmiColorFormatEnum.YCbCr
        self._power_state = 2

    @property
    def ir_receive(self):
        return self._ir_receive

    @ir_receive.setter
    def ir_receive(self, value):
        self._ir_receive = value

    @property
    def h_phase_value(self):
        return self._h_phase_value

    @h_phase_value.setter
    def h_phase_value(self, value):
        self._h_phase_value = value

    @property
    def img_flip(self):
        return self._img_flip

    @img_flip.setter
    def img_flip(self, value):
        self._img_flip = value

    @property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        self._camera_id = value

    @property
    def menu_mode(self):
        return self._menu_mode

    @menu_mode.setter
    def menu_mode(self, value):
        self._menu_mode = value

    @property
    def ir_cut_filter(self):
        return self._ir_cut_filter

    @ir_cut_filter.setter
    def ir_cut_filter(self, value):
        self._ir_cut_filter = value

    @property
    def tally_mode(self):
        return self._tally_mode

    @tally_mode.setter
    def tally_mode(self, value):
        self._tally_mode = value

    @property
    def tally_level(self):
        return self._tally_level

    @tally_level.setter
    def tally_level(self, value):
        self._tally_level = value

    @property
    def hdmi_color_space(self):
        return self._hdmi_color_space

    @hdmi_color_space.setter
    def hdmi_color_space(self, value):
        self._hdmi_color_space = value

    @property
    def power_state(self):
        return self._power_state

    @power_state.setter
    def power_state(self, value):
        self._power_state = value

    def serialize(self):
        return {
            "ir_receive": self._ir_receive,
            "h_phase_value": self._h_phase_value,
            "img_flip": self._img_flip,
            "camera_id": self._camera_id,
            "menu_mode": self._menu_mode,
            "ir_cut_filter": self._ir_cut_filter,
            "tally_mode": self._tally_mode,
            "tally_level": self._tally_level,
            "hdmi_color_space": self._hdmi_color_space,
            "power_state": self._power_state
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

    def deserialize(self, data: dict):
        self.ir_receive = self.returnEnumerationFromSomething(data["ir_receive"], EnableStateEnum)
        self.h_phase_value = data["h_phase_value"]
        self.img_flip = self.returnEnumerationFromSomething(data["img_flip"], EnableStateEnum)
        self.camera_id = data["camera_id"]
        self.menu_mode = self.returnEnumerationFromSomething(data["menu_mode"], EnableStateEnum)
        self.ir_cut_filter = self.returnEnumerationFromSomething(data["ir_cut_filter"], EnableStateEnum)
        self.tally_mode = self.returnEnumerationFromSomething(data["tally_mode"], EnableStateEnum)
        self.tally_level = self.returnEnumerationFromSomething(data["tally_level"], TallyLevel)
        self.hdmi_color_space = self.returnEnumerationFromSomething(data["hdmi_color_space"], HdmiColorFormatEnum)
        self.power_state = data["power_state"]