from visca.dictionary.dictionaries import genericsDictionary
from visca.dictionary.enumerations import *
from visca.baseClasses.baseInterfaceClass import BaseInterfaceClass
from visca.dataStucture.commandProcessor import CommandProcessor
from visca.memories.genericsMemories import GenericsMemories



class GenericsInterface(BaseInterfaceClass):
    def __init__(self, _genericMemories: GenericsMemories, _genericsDictionary: dict):
        super().__init__()
        self.genericsMemories = _genericMemories
        self.command_map = _genericsDictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    # Picture Profile
    def setPictureProfile(self, mode: PictureProfileEnum):
        self._last_command = None
        self.genericsMemories.picture_profile = mode
        return self.processor.set("picture_profile", mode.value)

    def getPictureProfile(self):
        self._last_command = "get picture_profile"
        return self.processor.inquire("picture_profile")

    # Flicker Cancel
    def setFlickerCancel(self, enableState: EnableStateEnum):
        self._last_command = None
        self.genericsMemories.flicker_cancel = enableState
        return self.processor.set("flicker_cancel", enableState.value)

    def getFlickerCancel(self):
        self._last_command = "get flicker_cancel"
        return self.processor.inquire("flicker_cancel")

    # Image Stabilizer
    def setImageStabilizer(self, enableState: EnableStateEnum):
        self._last_command = None
        self.genericsMemories.image_stabilizer = enableState
        return self.processor.set("image_stabilizer", enableState.value)

    def getImageStabilizer(self):
        self._last_command = "get image_stabilizer"
        return self.processor.inquire("image_stabilizer")

    # Defog
    def setDefog(self, state: EnableStateEnum, level: int):
        if level not in range(0, 3):
            raise ValueError("Valore fuori range per Defog Level.")
        self._last_command = None
        self.genericsMemories.defog = {"state": state, "level": level}
        return self.processor.set("defog", state.value, level)

    def getDefog(self):
        self._last_command = "get defog"
        return self.processor.inquire("defog")

    # High Resolution
    def setHighResolution(self, mode: EnableStateEnum):
        self._last_command = None
        self.genericsMemories.high_resolution = mode
        return self.processor.set("high_resolution", mode.value)

    def getHighResolution(self):
        self._last_command = "get high_resolution"
        return self.processor.inquire("high_resolution")

    # Noise Reduction Level
    def setNoiseReductionLevel(self, level: NoiseReductionLevel):
        """
        Imposta il livello di riduzione del rumore.
        :param level:  Livello di riduzione del rumore. Valori possibili: 0-5, 127
        :return:
        """
        if level not in NoiseReductionLevel:
            raise ValueError("Valore fuori range per Noise Reduction Level.")
        self._last_command = None
        self.genericsMemories.noise_reduction = level
        return self.processor.set("noise_reduction_level", level.value)

    def getNoiseReductionLevel(self):
        self._last_command = "get noise_reduction_level"
        return self.processor.inquire("noise_reduction_level")

    # 2D/3D Noise Reduction
    def set2D3DNoiseReduction(self, nr_2d: NoiseReduction2DEnum, nr_3d: NoiseReduction3DEnum):
        """
        Imposta i livelli di riduzione del rumore 2D e 3D.
        :param nr_2d:  valori possibili: 0-5
        :param nr_3d:  valori possibili: 0-5
        :return:
        """
        self._last_command = None
        self.genericsMemories.n2D_3DNoiseReduction = {"2D": nr_2d, "3D": nr_3d}
        return self.processor.set("2d_3d_nr", nr_2d.value, nr_3d.value)

    def get2D3DNoiseReduction(self):
        self._last_command = "get 2d_3d_nr"
        return self.processor.inquire("2d_3d_nr")

    # Picture Effect
    def setPictureEffect(self, mode: PictureEffectEnum):
        self._last_command = None
        self.genericsMemories.picture_effect = mode
        return self.processor.set("picture_effect", mode.value)

    def getPictureEffect(self):
        self._last_command = "get picture_effect"
        return self.processor.inquire("picture_effect")

    # Color Bar
    def setColorBar(self, mode: EnableStateEnum):
        self._last_command = None
        self.genericsMemories.color_bar = mode
        return self.processor.set("color_bar", mode.value)

    def getColorBar(self):
        self._last_command = "get color_bar"
        return self.processor.inquire("color_bar")


if __name__ == "__main__":
    genericMemories = GenericsMemories()
    interface = GenericsInterface(genericMemories, genericsDictionary)
    print(interface.setPictureProfile(PictureProfileEnum.PP2))
    print(interface.getPictureProfile())

    print(interface.setFlickerCancel(EnableStateEnum.ON))
    print(interface.getFlickerCancel())

    print(interface.setImageStabilizer(EnableStateEnum.ON))
    print(interface.getImageStabilizer())

    print(interface.setDefog(EnableStateEnum.ON, 2))
    print(interface.getDefog())

    print(interface.setHighResolution(EnableStateEnum.ON))
    print(interface.getHighResolution())

    print(interface.setNoiseReductionLevel(NoiseReductionLevel.STRONG))
    print(interface.getNoiseReductionLevel())
    print(genericMemories.n2D_3DNoiseReduction)
    print(interface.set2D3DNoiseReduction(NoiseReduction2DEnum.NR_2, NoiseReduction3DEnum.NR_3))
    print(interface.get2D3DNoiseReduction())

    print(genericMemories.n2D_3DNoiseReduction)
    print(interface.setPictureEffect(PictureEffectEnum.BandW))
    print(interface.getPictureEffect())

    print(interface.setColorBar(EnableStateEnum.ON))
    print(interface.getColorBar())