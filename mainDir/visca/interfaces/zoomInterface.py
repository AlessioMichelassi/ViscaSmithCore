from mainDir.visca.dictionary.dictionaries import zoomDictionary
from mainDir.visca.dictionary.enumerations import *
from mainDir.visca.baseClasses.baseInterfaceClass import BaseInterfaceClass
from mainDir.visca.dataStucture.commandProcessor import CommandProcessor
from mainDir.visca.memories.zoomMemories import ZoomMemories



class ZoomInterface(BaseInterfaceClass):
    def __init__(self, _zoom_memories: ZoomMemories, _zoomDictionary: dict):
        super().__init__()
        self.zoomMemories = _zoom_memories
        self.command_map = _zoomDictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    # Zoom Stop
    def stopZoom(self):
        self._last_command = None
        return self.processor.set("stop_zoom")

    # Zoom Tele Standard
    def zoomTeleStandard(self):
        self._last_command = None
        return self.processor.set("tele_standard")

    # Zoom Wide Standard
    def zoomWideStandard(self):
        self._last_command = None
        return self.processor.set("wide_standard")

    # Zoom Tele Variable
    def zoomTeleVariable(self, speed: int):
        """
        Esegue uno zoom variabile in modalità Tele.
        :param speed: Velocità di zoom (0–7).
        :return: Comando formattato per il Tele Zoom Variabile.
        """
        if speed < 0 or speed > 7:
            raise ValueError("Velocità fuori range per Tele Zoom Variabile (0-7).")
        self._last_command = None
        return self.processor.set("tele_variable", speed)

    # Zoom Wide Variable
    def zoomWideVariable(self, speed: int):
        """
        Esegue uno zoom variabile in modalità Wide.
        :param speed: Velocità di zoom (0–7).
        :return: Comando formattato per il Wide Zoom Variabile.
        """
        if speed < 0 or speed > 7:
            raise ValueError("Velocità fuori range per Wide Zoom Variabile (0-7).")
        self._last_command = None
        return self.processor.set("wide_variable", speed)

    # Zoom Direct
    def setZoomValue(self, position: int):
        if 0 > position or position > 16384:
            raise ValueError("Posizione fuori range per Zoom Direct.")
        self._last_command = None
        self.zoomMemories.zoom_value = position
        return self.processor.set("direct", position)

    def getZoomDirect(self):
        self._last_command = "get direct"
        return self.processor.inquire("direct")

    # Zoom Mode
    def setZoomMode(self, mode: ZoomModeEnum):
        if mode not in ZoomModeEnum:
            raise ValueError("Modalità fuori range per Zoom Mode.")
        self._last_command = None
        self.zoomMemories.zoom_mode = mode
        return self.processor.set("mode", mode.value)

    def getZoomMode(self):
        self._last_command = "get mode"
        return self.processor.inquire("mode")

    # Tele Convert
    def setTeleConvert(self, state: EnableStateEnum):
        if state not in EnableStateEnum:
            raise ValueError("Stato fuori range per Tele Convert.")
        self._last_command = None
        self.zoomMemories.tele_convert = state
        return self.processor.set("tele_convert", state.value)

    def getTeleConvert(self):
        self._last_command = "get tele_convert"
        return self.processor.inquire("tele_convert")

    # Digital Zoom On/Off
    def digitalZoomOn(self):
        self._last_command = None
        return self.processor.set("digital_zoom_on")

    def digitalZoomOff(self):
        self._last_command = None
        return self.processor.set("digital_zoom_off")

    # Clear Image Zoom On/Off
    def clearImageZoomOn(self):
        self._last_command = None
        return self.processor.set("clear_image_zoom_on")

    def clearImageZoomOff(self):
        self._last_command = None
        return self.processor.set("clear_image_zoom_off")

if __name__ == "__main__":
    zoomMemories = ZoomMemories()
    interface = ZoomInterface(zoomMemories, zoomDictionary)
    print(interface.stopZoom())
    print("zomm tele standard: 8x 01 04 07 02 FF")
    print(interface.zoomTeleStandard())
    print("zoom wide standard: 8x 01 04 07 03 FF")
    print(interface.zoomWideStandard())
    print("zoom tele variable: 8x 01 04 07 2p FF - 5")
    print(interface.zoomTeleVariable(5))
    print("zoom wide variable: 8x 01 04 07 3p FF - 5")
    print(interface.zoomWideVariable(5))
    print("zoom direct: 8x 01 04 47 0p 0p 0p 0p FF - 2000")
    print(interface.setZoomValue(2000))
    print("zoom direct: 8x 01 04 47 0p 0p 0p 0p FF - 4000")
    print(interface.setZoomValue(4000))
    print("get zoom direct:")
    print(interface.getZoomDirect())
    print("zoom mode: 8x 01 04 07 0p FF")
    print(interface.setZoomMode(ZoomModeEnum.DIGITAL))
    print("get zoom mode:")
    print(interface.getZoomMode())
    print("tele convert: 8x 01 7E 04 36 02 FF")
    print(interface.setTeleConvert(EnableStateEnum.ON))
    print("get tele convert:")
    print(interface.getTeleConvert())
    print("digital zoom on: 8x 01 04 07 2p FF")

    print(interface.digitalZoomOn())
    print("digital zoom off: 8x 01 04 07 3p FF")
    print(interface.digitalZoomOff())
    print("clear image zoom on: 8x 01 04 06 04 FF")
    print(interface.clearImageZoomOn())
    print("clear image zoom off: 8x 01 04 06 03 FF")
    print(interface.clearImageZoomOff())
