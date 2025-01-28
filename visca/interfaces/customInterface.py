from enum import Enum

from visca.dictionary.dictionaries import customDictionary
from visca.baseClasses.baseInterfaceClass import BaseInterfaceClass
from visca.dataStucture.commandProcessor import CommandProcessor


class DynamicHotPixelCorrectionEnum(Enum):
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4
    AGGRESSIVE = 5

class CameraFlipEnum(Enum):
    OFF = 0
    FLIP_H = 1
    FLIP_V = 2
    FLIP_HV = 3

class AutoFocusZoneEnum(Enum):
    FRONT_FOCUS = 0
    BACK_FOCUS = 1
    MEETING_FOCUS = 2
    EDUCATION_TRACKING_FOCUS = 3
    MOVING_OBJECT_FOCUS = 4
    CENTER_FOCUS = 5

class PanTiltStateEnum(Enum):
    OFF = 2
    ON = 3


class CustomInterface(BaseInterfaceClass):

    def __init__(self, _customMemories, _customDictionary):
        super().__init__()
        self.customMemories = _customMemories
        self.command_map = _customDictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDynamicHotPixelCorrection(self, mode: DynamicHotPixelCorrectionEnum):
        self._last_command = None
        self.customMemories.dynamicHotPixelCorrection = mode
        return self.processor.set("DynamicHotPixelCorrection", mode.value)

    def getDynamicHotPixelCorrection(self):
        self._last_command = "get DynamicHotPixelCorrection"
        return self.processor.inquire("DynamicHotPixelCorrection")

    def cameraApertureReset(self):
        self._last_command = None
        self.customMemories.cameraAperture = 0
        return self.processor.set("CameraAperture_reset")

    def cameraApertureUp(self):
        self._last_command = None
        if self.customMemories.cameraAperture < 255:
            self.customMemories.cameraAperture += 1
        else:
            self.customMemories.cameraAperture = 255
        return self.processor.set("CameraAperture_Up")

    def cameraApertureDown(self):
        self._last_command = None
        if self.customMemories.cameraAperture > 0:
            self.customMemories.cameraAperture -= 1
        else:
            self.customMemories.cameraAperture = 0
        return self.processor.set("CameraAperture_Down")

    def setCameraAperture(self, value: int):
        if value < 0 or value > 255:
            raise ValueError("Valore fuori range per Camera Aperture (0, 255).")
        self._last_command = None
        self.customMemories.cameraAperture = value
        return self.processor.set("CameraAperture_Value", value)

    def getCameraAperture(self):
        self._last_command = "get CameraAperture_Value"
        return self.processor.inquire("CameraAperture_Value")

    def setCameraBrightnessUp(self):
        self._last_command = None
        if self.customMemories.cameraBrightness < 10:
            self.customMemories.cameraBrightness += 1
        else:
            self.customMemories.cameraBrightness = 10
        return self.setCameraBrightness(self.customMemories.cameraBrightness)

    def setCameraBrightnessDown(self):
        self._last_command = None
        if self.customMemories.cameraBrightness > 0:
            self.customMemories.cameraBrightness -= 1
        else:
            self.customMemories.cameraBrightness = 0
        return self.setCameraBrightness(self.customMemories.cameraBrightness)

    def setCameraBrightness(self, value: int):
        if value < 0 or value > 10:
            raise ValueError("Valore fuori range per Camera Brightness (0, 10).")
        self._last_command = None
        self.customMemories.cameraBrightness = value
        return self.processor.set("CameraBrightness_value", value)

    def getCameraBrightness(self):
        self._last_command = "get CameraBrightness_value"
        return self.processor.inquire("CameraBrightness_value")

    def setCameraContrastUp(self):
        self._last_command = None
        if self.customMemories.cameraContrast < 10:
            self.customMemories.cameraContrast += 1
        else:
            self.customMemories.cameraContrast = 10
        return self.setCameraContrast(self.customMemories.cameraContrast)

    def setCameraContrastDown(self):
        self._last_command = None
        if self.customMemories.cameraContrast > 0:
            self.customMemories.cameraContrast -= 1
        else:
            self.customMemories.cameraContrast = 0
        return self.setCameraContrast(self.customMemories.cameraContrast)

    def setCameraContrast(self, value: int):
        if value < 0 or value > 10:
            raise ValueError("Valore fuori range per Camera Contrast (0, 10).")
        self._last_command = None
        self.customMemories.cameraContrast = value
        return self.processor.set("CameraContrast_value", value)

    def getCameraContrast(self):
        self._last_command = "get CameraContrast_value"
        return self.processor.inquire("CameraContrast_value")

    def setCameraFlip(self, mode: CameraFlipEnum):
        self._last_command = None
        self.customMemories.cameraFlip = mode
        return self.processor.set("CameraFlip", mode.value)

    def getCameraFlip(self):
        self._last_command = "get CameraFlip"
        return self.processor.inquire("CameraFlip")

    def setCameraIridix(self, value: int):
        if value < 0 or value > 256:
            raise ValueError("Valore fuori range per Camera Iridix (0, 256).")
        self._last_command = None
        self.customMemories.cameraIridix = value
        return self.processor.set("CameraIridix_value", value)

    def getCameraIridix(self):
        self._last_command = "get CameraIridix_value"
        return self.processor.inquire("CameraIridix_value")

    def setAutoFocusZone(self, mode: AutoFocusZoneEnum):
        self._last_command = None
        self.customMemories.autoFocusZone = mode
        return self.processor.set("AutoFocusZone", mode.value)

    def getAutoFocusZone(self):
        self._last_command = "get AutoFocusZone"
        return self.processor.inquire("AutoFocusZone")

    def setColorHue(self, value: int):
        if value < -14 or value > 14:
            raise ValueError("Valore fuori range per Color Hue (-14, 14).")
        self._last_command = None
        self.customMemories.colorHue = value
        value += 14
        return self.processor.set("ColorHue_value", value)

    def getColorHue(self):
        self._last_command = "get ColorHue_value"
        return self.processor.inquire("ColorHue_value")

    def setPanTiltMaxSpeed(self, mode: PanTiltStateEnum):
        self._last_command = None
        self.customMemories.panTiltMaxSpeed = mode
        return self.processor.set("PanTilt_MaxSpeed", mode.value)

    def getPanTiltMaxSpeed(self):
        self._last_command = "get PanTilt_MaxSpeed"
        return self.processor.inquire("PanTilt_MaxSpeed")

    def setPresetPanSpeed(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Valore fuori range per Pan Tilt Speed (0, 7).")
        self._last_command = None
        self.customMemories.presetSpeed_horizontal = value
        return self.processor.set("PresetSpeed_Horizontal", value)

    def getPresetPanSpeed(self):
        self._last_command = "get PresetSpeed_Horizontal"
        return self.processor.inquire("PresetSpeed_Horizontal")

    def setPresetTiltSpeed(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Valore fuori range per Pan Tilt Speed (0, 7).")
        self._last_command = None
        self.customMemories.presetSpeed_vertical = value
        return self.processor.set("PresetSpeed_Vertical", value)

    def getPresetTiltSpeed(self):
        self._last_command = "get PresetSpeed_Vertical"
        return self.processor.inquire("PresetSpeed_Vertical")

    def setPresetZoomSpeed(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Valore fuori range per Zoom Speed (0, 7).")
        self._last_command = None
        self.customMemories.presetSpeed_zoom = value
        return self.processor.set("PresetSpeed_Zoom", value)

    def getPresetZoomSpeed(self):
        self._last_command = "get PresetSpeed_Zoom"
        return self.processor.inquire("PresetSpeed_Zoom")

if __name__ == "__main__":
    from visca.memories.customMemories import CustomMemories
    customMemories = CustomMemories()
    dictionary = customDictionary
    customInterface = CustomInterface(customMemories, dictionary)
    print(f"TEST setDynamicHotPixelCorrection: {customInterface.setDynamicHotPixelCorrection(DynamicHotPixelCorrectionEnum.AGGRESSIVE)}")
    print(f"TEST getDynamicHotPixelCorrection: {customInterface.getDynamicHotPixelCorrection()}")

    print(f"TEST cameraApertureReset: {customInterface.cameraApertureReset()}")
    print(f"TEST cameraApertureUp: {customInterface.cameraApertureUp()}")
    print(f"TEST cameraApertureDown: {customInterface.cameraApertureDown()}")
    print(f"TEST setCameraAperture: {customInterface.setCameraAperture(128)}")
    print(f"TEST getCameraAperture: {customInterface.getCameraAperture()}")

    print(f"TEST setCameraBrightness: {customInterface.setCameraBrightness(5)}")
    print(f"TEST getCameraBrightness: {customInterface.getCameraBrightness()}")

    print(f"TEST setCameraContrast: {customInterface.setCameraContrast(5)}")
    print(f"TEST getCameraContrast: {customInterface.getCameraContrast()}")

    print(f"TEST setCameraFlip: {customInterface.setCameraFlip(CameraFlipEnum.FLIP_HV)}")
    print(f"TEST getCameraFlip: {customInterface.getCameraFlip()}")

    print(f"TEST setCameraIridix: {customInterface.setCameraIridix(128)}")
    print(f"TEST getCameraIridix: {customInterface.getCameraIridix()}")

    print(f"TEST setAutoFocusZone: {customInterface.setAutoFocusZone(AutoFocusZoneEnum.CENTER_FOCUS)}")
    print(f"TEST getAutoFocusZone: {customInterface.getAutoFocusZone()}")

    print(f"TEST setColorHue: {customInterface.setColorHue(7)}")
    print(f"TEST getColorHue: {customInterface.getColorHue()}")

    print(f"TEST setPanTiltMaxSpeed: {customInterface.setPanTiltMaxSpeed(PanTiltStateEnum.ON)}")
    print(f"TEST getPanTiltMaxSpeed: {customInterface.getPanTiltMaxSpeed()}")

    print(f"TEST setPresetPanSpeed: {customInterface.setPresetPanSpeed(5)}")
    print(f"TEST getPresetPanSpeed: {customInterface.getPresetPanSpeed()}")

    print(f"TEST setPresetTiltSpeed: {customInterface.setPresetTiltSpeed(5)}")
    print(f"TEST getPresetTiltSpeed: {customInterface.getPresetTiltSpeed()}")

    print(f"TEST setPresetZoomSpeed: {customInterface.setPresetZoomSpeed(5)}")
    print(f"TEST getPresetZoomSpeed: {customInterface.getPresetZoomSpeed()}")