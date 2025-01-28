from visca.dictionary.dictionaries import detailDictionary
from visca.dictionary.enumerations import *
from visca.baseClasses.baseInterfaceClass import BaseInterfaceClass
from visca.dataStucture.commandProcessor import CommandProcessor
from visca.memories.detailMemories import DetailMemories

class DetailInterface(BaseInterfaceClass):

    def __init__(self, _detailMemories: DetailMemories, _detailDictionary: dict):
        super().__init__()
        self.detailMemories = _detailMemories
        self.command_map = _detailDictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    # Detail Level
    def resetDetailLevel(self):
        """
        Reset Detail Level to default value 0
        :return:
        """
        self._last_command = None
        self.detailMemories.detail_level = 0
        return self.processor.set("detail_level_reset")

    def detailUp(self):
        """
        Increase Detail Level by 1
        Il livello di dettaglio va da -7 a +7
        :return:
        """
        self._last_command = None
        if self.detailMemories.detail_level < 7:
            self.detailMemories.detail_level += 1
        else:
            self.detailMemories.detail_level = 7
        return self.processor.set("detail_level_up")

    def detailDown(self):
        self._last_command = None
        if self.detailMemories.detail_level > -7:
            self.detailMemories.detail_level -= 1
        else:
            self.detailMemories.detail_level = -7
        return self.processor.set("detail_level_down")

    def setDetailLevel(self, value: int):
        if value < -7 or value > 7:
            raise ValueError("Valore fuori range per Detail Level (-7, 7).")
        self._last_command = None
        self.detailMemories.detail_level = value
        value = value + 7
        return self.processor.set("detail_level_value", value)

    def getDetailLevel(self):
        self._last_command = "get detail_level_value"
        return self.processor.inquire("detail_level_value")

    # Detail Mode
    def setDetailMode(self, mode: EnumMode):
        """
        Set Detail Mode : MANUAL, AUTO
        :param mode:
        :return:
        """
        self._last_command = None
        self.detailMemories.detail_mode = mode
        return self.processor.set("detail_mode", mode.value)

    def getDetailMode(self):
        self._last_command = "get detail_mode"
        return self.processor.inquire("detail_mode")

    # Detail Bandwidth
    def setDetailBandwidth(self, mode: DetailBandWidthEnum):
        """
        Set Detail Bandwidth DEFAULT, LOW, MIDDLE, HIGH, WIDE
        :param value:
        :return:
        """
        self._last_command = None
        self.detailMemories.detail_bandwidth = mode
        return self.processor.set("detail_bandwidth", mode.value)

    def getDetailBandwidth(self):
        self._last_command = "get detail_bandwidth"
        return self.processor.inquire("detail_bandwidth")

    # Detail Crispening
    def setDetailCrispening(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Valore fuori range per Detail Crispening (0-7).")
        self._last_command = None
        self.detailMemories.detail_crispening = value
        return self.processor.set("detail_crispening", value)

    def getDetailCrispening(self):
        self._last_command = "get detail_crispening"
        return self.processor.inquire("detail_crispening")

    # Detail HV Balance
    def setDetailHVBalance(self, value: int):
        if value < -2 or value > 2:
            raise ValueError("Valore fuori range per Detail HV Balance (-2 e 2).")
        self._last_command = None
        self.detailMemories.detail_hv_balance = value
        value = value + 2
        return self.processor.set("detail_hv_balance", value)

    def getDetailHVBalance(self):
        self._last_command = "get detail_hv_balance"
        return self.processor.inquire("detail_hv_balance")

    # Detail BW Balance
    def setDetailBWBalance(self, mode: DetailBWBalanceEnum):
        self._last_command = None
        self.detailMemories.detail_bw_balance = mode
        return self.processor.set("detail_bw_balance", mode.value)

    def getDetailBWBalance(self):
        self._last_command = "get detail_bw_balance"
        return self.processor.inquire("detail_bw_balance")

    # Detail Limit
    def setDetailLimit(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Valore fuori range per Detail Limit (0-7).")
        self._last_command = None
        self.detailMemories.detail_limit = value
        return self.processor.set("detail_limit", value)

    def getDetailLimit(self):
        self._last_command = "get detail_limit"
        return self.processor.inquire("detail_limit")

    # Detail Highlight
    def setDetailHighlight(self, value: int):
        if value < 0 or value > 4:
            raise ValueError("Valore fuori range per Detail Highlight (0-4).")
        self._last_command = None
        self.detailMemories.detail_highlight = value
        return self.processor.set("detail_highlight", value)

    def getDetailHighlight(self):
        self._last_command = "get detail_highlight"
        return self.processor.inquire("detail_highlight")

    # Detail Super Low
    def setDetailSuperLow(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Valore fuori range per Detail Super Low (0-7).")
        self._last_command = None
        self.detailMemories.detail_super_low = value
        return self.processor.set("detail_super_low", value)

    def getDetailSuperLow(self):
        self._last_command = "get detail_super_low"
        return self.processor.inquire("detail_super_low")

if __name__ == "__main__":
    detailMemories = DetailMemories()
    detailInterface = DetailInterface(detailMemories, detailDictionary)
    print("Detail Interface")
    print(f"test get detail mode:       \t\t{detailInterface.getDetailMode()}")
    print(f"test get detail level:      \t\t{detailInterface.getDetailLevel()}")
    print(f"test get detail bandwidth:  \t\t{detailInterface.getDetailBandwidth()}")
    print(f"test get detail crispening: \t\t{detailInterface.getDetailCrispening()}")
    print(f"test get detail hv balance: \t\t{detailInterface.getDetailHVBalance()}")
    print(f"test get detail bw balance: \t\t{detailInterface.getDetailBWBalance()}")
    print(f"test get detail limit:      \t\t{detailInterface.getDetailLimit()}")
    print(f"test get detail highlight:  \t\t{detailInterface.getDetailHighlight()}")
    print(f"test get detail super low:  \t\t{detailInterface.getDetailSuperLow()}")

    print(f"test set detail mode:       \t\t{detailInterface.setDetailMode(EnumMode.MANUAL)}")
    print(f"test set detail level:      \t\t{detailInterface.setDetailLevel(5)}")
    print(f"test set detail bandwidth:  \t\t{detailInterface.setDetailBandwidth(DetailBandWidthEnum.HIGH)}")
    print(f"test set detail crispening: \t\t{detailInterface.setDetailCrispening(3)}")
    print(f"test set detail hv balance: \t\t{detailInterface.setDetailHVBalance(-2)}")
    print(f"test set detail bw balance: \t\t{detailInterface.setDetailBWBalance(DetailBWBalanceEnum.TYPE_1)}")
    print(f"test set detail limit:      \t\t{detailInterface.setDetailLimit(4)}")