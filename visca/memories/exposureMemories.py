
from visca.dictionary.enumerations import *


class ExposureMemories:

    _exposureMode: ExposureModeEnum
    _gainValue: GainValueEnum
    _shutterValue: ShutterSpeedEnum_60
    _irisValue: IrisSettingsEnum
    _ae_speed_value: int
    _auto_slow_shutter_mode: EnableStateEnum
    _backlight_mode: EnableStateEnum
    _exp_comp_mode: EnableStateEnum
    _exp_comp_value: int
    _gain_limit_value: GainValueEnum
    _gain_point_mode: EnableStateEnum
    _gain_point_value: GainValueEnum
    _max_shutter_value: ShutterSpeedEnum_60
    _min_shutter_value: ShutterSpeedEnum_60
    _spotlight_mode: EnableStateEnum
    _highSensitivity_mode: EnableStateEnum
    _visibility_enhancer_mode: EnableStateEnum
    _visibility_enhancer_level: dict
    _lowLightBiasis_mode: EnableStateEnum
    _lowLightBiasis_value: LowLightBiasLevel

    def __init__(self):
        """
        ExposureMemories contiene i valori che l'utente può impostare tramite
        l'interfaccia grafica. Questi valori possono essere salvati e caricati
        per mantenere le impostazioni preferite dell'utente.
        """
        self._exposureMode = ExposureModeEnum.MANUAL
        self._gainValue = GainValueEnum.GAIN_0DB
        self._shutterValue = ShutterSpeedEnum_60.s1_60
        self._irisValue = IrisSettingsEnum.F2_0
        self._ae_speed_value = 0
        self._auto_slow_shutter_mode = EnableStateEnum.OFF
        self._backlight_mode = EnableStateEnum.OFF
        self._exp_comp_mode = EnableStateEnum.OFF
        self._exp_comp_value = 0
        self._gain_limit_value = GainValueEnum.GAIN_0DB
        self._gain_point_mode = EnableStateEnum.OFF
        self._gain_point_value = GainValueEnum.GAIN_0DB
        self._max_shutter_value = ShutterSpeedEnum_60.s1_30
        self._min_shutter_value = ShutterSpeedEnum_60.s1_125
        self._spotlight_mode = EnableStateEnum.OFF
        self._highSensitivity_mode = EnableStateEnum.OFF
        self._visibility_enhancer_mode = EnableStateEnum.OFF
        self._visibility_enhancer_level = {"effect": VisibilityEnhancerEffectLevel.NORMAL,
                                           "brightness": VisibilityEnhancerBrightnessCompensation.STANDARD,
                                           "compensation": VisibilityEnhancerCompensationLevel.LOW}
        self._lowLightBiasis_mode = EnableStateEnum.OFF
        self._lowLightBiasis_value = LowLightBiasLevel.LLB_04


    @property
    def exposureMode(self) -> ExposureModeEnum:
        return self._exposureMode

    @exposureMode.setter
    def exposureMode(self, value: ExposureModeEnum):
        self._exposureMode = value

    @property
    def gainValue(self) -> GainValueEnum:
        return self._gainValue

    @gainValue.setter
    def gainValue(self, value: GainValueEnum):
        self._gainValue = value

    @property
    def shutterValue(self) -> ShutterSpeedEnum_60:
        return self._shutterValue

    @shutterValue.setter
    def shutterValue(self, value: ShutterSpeedEnum_60):
        self._shutterValue = value

    @property
    def irisValue(self) -> IrisSettingsEnum:
        return self._irisValue

    @irisValue.setter
    def irisValue(self, value: IrisSettingsEnum):
        self._irisValue = value

    @property
    def ae_speed_value(self) -> int:
        return self._ae_speed_value

    @ae_speed_value.setter
    def ae_speed_value(self, value: int):
        self._ae_speed_value = value

    @property
    def auto_slow_shutter_mode(self) -> EnableStateEnum:
        return self._auto_slow_shutter_mode

    @auto_slow_shutter_mode.setter
    def auto_slow_shutter_mode(self, value: EnableStateEnum):
        self._auto_slow_shutter_mode = value

    @property
    def backlight_mode(self) -> EnableStateEnum:
        return self._backlight_mode

    @backlight_mode.setter
    def backlight_mode(self, value: EnableStateEnum):
        self._backlight_mode = value

    @property
    def exp_comp_mode(self) -> EnableStateEnum:
        return self._exp_comp_mode

    @exp_comp_mode.setter
    def exp_comp_mode(self, value: EnableStateEnum):
        self._exp_comp_mode = value

    @property
    def exp_comp_value(self) -> int:
        return self._exp_comp_value

    @exp_comp_value.setter
    def exp_comp_value(self, value: int):
        self._exp_comp_value = value

    @property
    def gain_limit_value(self) -> GainValueEnum:
        return self._gain_limit_value

    @gain_limit_value.setter
    def gain_limit_value(self, value: GainValueEnum):
        self._gain_limit_value = value

    @property
    def gain_point_mode(self) -> EnableStateEnum:
        return self._gain_point_mode

    @gain_point_mode.setter
    def gain_point_mode(self, value: EnableStateEnum):
        self._gain_point_mode = value

    @property
    def gain_point_value(self) -> GainValueEnum:
        return self._gain_point_value

    @gain_point_value.setter
    def gain_point_value(self, value: GainValueEnum):
        self._gain_point_value = value

    @property
    def max_shutter_value(self) -> ShutterSpeedEnum_60:
        return self._max_shutter_value

    @max_shutter_value.setter
    def max_shutter_value(self, value: ShutterSpeedEnum_60):
        self._max_shutter_value = value

    @property
    def min_shutter_value(self) -> ShutterSpeedEnum_60:
        return self._min_shutter_value

    @min_shutter_value.setter
    def min_shutter_value(self, value: ShutterSpeedEnum_60):
        self._min_shutter_value = value

    @property
    def spotlight_mode(self) -> EnableStateEnum:
        return self._spotlight_mode

    @spotlight_mode.setter
    def spotlight_mode(self, value: EnableStateEnum):
        self._spotlight_mode = value

    @property
    def highSensitivity_mode(self) -> EnableStateEnum:
        return self._highSensitivity_mode

    @highSensitivity_mode.setter
    def highSensitivity_mode(self, value: EnableStateEnum):
        self._highSensitivity_mode = value

    @property
    def visibility_enhancer_mode(self) -> EnableStateEnum:
        return self._visibility_enhancer_mode

    @visibility_enhancer_mode.setter
    def visibility_enhancer_mode(self, value: EnableStateEnum):
        self._visibility_enhancer_mode = value

    @property
    def visibility_enhancer_level(self) -> (VisibilityEnhancerEffectLevel, VisibilityEnhancerBrightnessCompensation, VisibilityEnhancerCompensationLevel):
        return self._visibility_enhancer_level

    @visibility_enhancer_level.setter
    def visibility_enhancer_level(self, value: (VisibilityEnhancerEffectLevel, VisibilityEnhancerBrightnessCompensation, VisibilityEnhancerCompensationLevel)):
        self._visibility_enhancer_level = value

    @property
    def lowLightBiasis_mode(self) -> EnableStateEnum:
        return self._lowLightBiasis_mode

    @lowLightBiasis_mode.setter
    def lowLightBiasis_mode(self, value: EnableStateEnum):
        self._lowLightBiasis_mode = value

    @property
    def lowLightBiasis_value(self) -> LowLightBiasLevel:
        return self._lowLightBiasis_value

    @lowLightBiasis_value.setter
    def lowLightBiasis_value(self, value: LowLightBiasLevel):
        self._lowLightBiasis_value = value

    def serialize(self) -> dict:
        """
        Serializzazione delle impostazioni di esposizione
        :return:
        """
        return {
            "exposure_mode": self._exposureMode,
            "gain_value": self._gainValue,
            "shutter_value": self._shutterValue,
            "iris_value": self._irisValue,
            "ae_speed_value": self._ae_speed_value,
            "auto_slow_shutter_mode": self._auto_slow_shutter_mode,
            "backlight_mode": self._backlight_mode,
            "exp_comp_mode": self._exp_comp_mode,
            "exp_comp_value": self._exp_comp_value,
            "gain_limit_value": self._gain_limit_value,
            "gain_point_mode": self._gain_point_mode,
            "gain_point_value": self._gain_point_value,
            "max_shutter_value": self._max_shutter_value,
            "min_shutter_value": self._min_shutter_value,
            "spotlight_mode": self._spotlight_mode,
            "highSensitivity_mode": self._highSensitivity_mode,
            "visibility_enhancer_mode": self._visibility_enhancer_mode,
            "visibility_enhancer_level": self._visibility_enhancer_level,
            "lowLightBiasis_mode": self._lowLightBiasis_mode,
            "lowLightBiasis_value": self._lowLightBiasis_value
        }

    def deserialize(self, data):
        """
        Deserializza i dati per aggiornare le proprietà della classe Exposure.

        :param data: Dizionario contenente i dati da deserializzare.
        """
        try:
            if not isinstance(data, dict):
                raise ValueError("I dati devono essere un dizionario.")

            self._exposureMode = self.returnEnumerationFromSomething(
                data.get("exposure_mode", self._exposureMode), ExposureModeEnum
            )
            self._gainValue = self.returnEnumerationFromSomething(
                data.get("gainValue", self._gainValue), GainValueEnum
            )
            self._shutterValue = self.returnEnumerationFromSomething(
                data.get("shutterValue", self._shutterValue), ShutterSpeedEnum_60
            )
            self._irisValue = self.returnEnumerationFromSomething(
                data.get("irisValue", self._irisValue), IrisSettingsEnum
            )
            self._ae_speed_value = data.get("ae_speed_value", self._ae_speed_value)
            self._auto_slow_shutter_mode = self.returnEnumerationFromSomething(
                data.get("auto_slow_shutter_mode", self._auto_slow_shutter_mode), EnableStateEnum
            )
            self._backlight_mode = self.returnEnumerationFromSomething(
                data.get("backlight_mode", self._backlight_mode), EnableStateEnum
            )
            self._exp_comp_mode = self.returnEnumerationFromSomething(
                data.get("exp_comp_mode", self._exp_comp_mode), EnableStateEnum
            )
            self._exp_comp_value = data.get("exp_comp_value", self._exp_comp_value)
            self._gain_limit_value = self.returnEnumerationFromSomething(
                data.get("gain_limit_value", self._gain_limit_value), GainValueEnum
            )
            self._gain_point_mode = self.returnEnumerationFromSomething(
                data.get("gain_point_mode", self._gain_point_mode), EnableStateEnum
            )
            self._gain_point_value = self.returnEnumerationFromSomething(
                data.get("gain_point_value", self._gain_point_value), GainValueEnum
            )
            self._max_shutter_value = self.returnEnumerationFromSomething(
                data.get("max_shutter_value", self._max_shutter_value), ShutterSpeedEnum_60
            )
            self._min_shutter_value = self.returnEnumerationFromSomething(
                data.get("min_shutter_value", self._min_shutter_value), ShutterSpeedEnum_60
            )
            self._spotlight_mode = self.returnEnumerationFromSomething(
                data.get("spotlight_mode", self._spotlight_mode), EnableStateEnum
            )
            self._highSensitivity_mode = self.returnEnumerationFromSomething(
                data.get("highSensitivity_mode", self._highSensitivity_mode), EnableStateEnum
            )
            self._visibility_enhancer_mode = self.returnEnumerationFromSomething(
                data.get("visibility_enhancer_mode", self._visibility_enhancer_mode), EnableStateEnum
            )
            self._visibility_enhancer_level = data.get(
                "visibility_enhancer_level", self._visibility_enhancer_level
            )
            self._lowLightBiasis_mode = self.returnEnumerationFromSomething(
                data.get("lowLightBiasis_mode", self._lowLightBiasis_mode), EnableStateEnum
            )
            self._lowLightBiasis_value = self.returnEnumerationFromSomething(
                data.get("lowLightBiasis_value", self._lowLightBiasis_value), LowLightBiasLevel
            )

        except Exception as e:
            print(f"Errore durante la deserializzazione: {e}")
            raise

    @staticmethod
    def returnEnumerationFromSomething(something, enumeration):
        """
        Converte un valore in un'enumerazione specificata.

        :param something: Valore da convertire (int, str o enum).
        :param enumeration: Tipo di enumerazione target.
        :return: Valore convertito nell'enumerazione.
        """
        if isinstance(something, int):
            return enumeration(something)
        elif isinstance(something, str):
            try:
                return enumeration[int(something)]
            except ValueError:
                return enumeration[something]
        elif isinstance(something, enumeration):
            return something
        else:
            raise ValueError(f"Valore '{something}' non valido per l'enumerazione {enumeration}.")

