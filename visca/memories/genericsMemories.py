from visca.dictionary.enumerations import *


class GenericsMemories:
    _picture_profile: PictureProfileEnum
    _high_resolution: EnableStateEnum
    _flicker_cancel: EnableStateEnum
    _image_stabilizer: EnableStateEnum

    _noise_reduction: NoiseReductionLevel
    _twoD_ThreeD: dict
    _pictureEffect: PictureEffectEnum
    _defog: EnableStateEnum
    _color_bar: EnableStateEnum

    def __init__(self):
        # Stato iniziale
        self._picture_profile = PictureProfileEnum.PP1
        self._high_resolution = EnableStateEnum.OFF
        self._flicker_cancel = EnableStateEnum.OFF
        self._image_stabilizer = EnableStateEnum.OFF
        self._noise_reduction = NoiseReductionLevel.WEAK
        self._twoD_ThreeD = {
            "2D": NoiseReduction2DEnum.OFF,
            "3D": NoiseReduction3DEnum.OFF
        }
        self._pictureEffect = PictureEffectEnum.OFF
        self._defog = EnableStateEnum.OFF
        self._color_bar = EnableStateEnum.OFF

    @property
    def picture_profile(self):
        return self._picture_profile

    @picture_profile.setter
    def picture_profile(self, value:PictureProfileEnum):
        if value not in PictureProfileEnum:
            raise ValueError("Valore fuori range per Picture Profile.")
        self._picture_profile = value

    @property
    def high_resolution(self):
        return self._high_resolution

    @high_resolution.setter
    def high_resolution(self, value):
        self._high_resolution = value

    @property
    def image_stabilizer(self):
        return self._image_stabilizer

    @image_stabilizer.setter
    def image_stabilizer(self, value):
        self._image_stabilizer = value

    @property
    def flicker_cancel(self):
        return self._flicker_cancel

    @flicker_cancel.setter
    def flicker_cancel(self, value):
        self._flicker_cancel = value

    @property
    def noise_reduction(self):
        return self._noise_reduction

    @noise_reduction.setter
    def noise_reduction(self, value):
        self._noise_reduction = value

    @property
    def n2D_3DNoiseReduction(self):
        return self._twoD_ThreeD

    @n2D_3DNoiseReduction.setter
    def n2D_3DNoiseReduction(self, noiseRed2D_3D: dict):
        self._twoD_ThreeD = noiseRed2D_3D

    @property
    def picture_effect(self):
        return self._pictureEffect

    @picture_effect.setter
    def picture_effect(self, mode: PictureEffectEnum):
        self._pictureEffect = mode

    @property
    def defog(self):
        return self._defog

    @defog.setter
    def defog(self, value):
        self._defog = value

    @property
    def color_bar(self):
        return self._color_bar

    @color_bar.setter
    def color_bar(self, value):
        self._color_bar = value

    def serialize(self):
        return {
            "pictureProfile": self.picture_profile,
            "highResolution": self.high_resolution,
            "flickerCancel": self.flicker_cancel,
            "imageStabilizer": self.image_stabilizer,
            "noiseReduction": self.noise_reduction,
            "2d_3d_nr": self.n2D_3DNoiseReduction,
            "pictureEffect": self.picture_effect,
            "defog": self.defog,
            "colorBar": self.color_bar
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
        self._picture_profile = self.returnEnumerationFromSomething(data["pictureProfile"], PictureProfileEnum)
        self._high_resolution = self.returnEnumerationFromSomething(data["highResolution"], EnableStateEnum)
        self._flicker_cancel = self.returnEnumerationFromSomething(data["flickerCancel"], EnableStateEnum)
        self._image_stabilizer = self.returnEnumerationFromSomething(data["imageStabilizer"], EnableStateEnum)

        self._noise_reduction = self.returnEnumerationFromSomething(data["noiseReduction"],
                                                                    NoiseReductionLevel)
        self._twoD_ThreeD = data["2d_3d_nr"]
        self._pictureEffect = self.returnEnumerationFromSomething(data["pictureEffect"], PictureEffectEnum)
        self._defog = self.returnEnumerationFromSomething(data["defog"], EnableStateEnum)
        self._color_bar = self.returnEnumerationFromSomething(data["colorBar"], EnableStateEnum)