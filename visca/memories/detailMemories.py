
from visca.dictionary.enumerations import *


class DetailMemories:
    # Stato interno
    _detail_level : int
    _detail_mode : EnumMode
    _detail_bandwidth: DetailBandWidthEnum
    _detail_crispening : int
    _detail_hv_balance : int
    _detail_bw_balance: DetailBWBalanceEnum
    _detail_limit : int
    _detail_highlight : int
    _detail_super_low : int

    def __init__(self):
        # default values
        self._detail_level = 0
        self._detail_mode = EnumMode.MANUAL
        self._detail_bandwidth = DetailBandWidthEnum.DEFAULT
        self._detail_crispening = 0
        self._detail_hv_balance = 0
        self._detail_bw_balance = DetailBWBalanceEnum.TYPE_2
        self._detail_limit = 0
        self._detail_highlight = 0
        self._detail_super_low = 0

    @property
    def detail_level(self):
        return self._detail_level

    @detail_level.setter
    def detail_level(self, value):
        self._detail_level = value

    @property
    def detail_mode(self):
        return self._detail_mode

    @detail_mode.setter
    def detail_mode(self, value: EnumMode):
        self._detail_mode = value

    @property
    def detail_bandwidth(self):
        return self._detail_bandwidth

    @detail_bandwidth.setter
    def detail_bandwidth(self, value: DetailBandWidthEnum):
        self._detail_bandwidth = value

    @property
    def detail_crispening(self):
        return self._detail_crispening

    @detail_crispening.setter
    def detail_crispening(self, value):
        self._detail_crispening = value

    @property
    def detail_hv_balance(self):
        return self._detail_hv_balance

    @detail_hv_balance.setter
    def detail_hv_balance(self, value):
        self._detail_hv_balance = value

    @property
    def detail_bw_balance(self):
        return self._detail_bw_balance

    @detail_bw_balance.setter
    def detail_bw_balance(self, value: DetailBWBalanceEnum):
        self._detail_bw_balance = value

    @property
    def detail_limit(self):
        return self._detail_limit

    @detail_limit.setter
    def detail_limit(self, value):
        self._detail_limit = value

    @property
    def detail_highlight(self):
        return self._detail_highlight

    @detail_highlight.setter
    def detail_highlight(self, value):
        self._detail_highlight = value

    @property
    def detail_super_low(self):
        return self._detail_super_low

    @detail_super_low.setter
    def detail_super_low(self, value):
        self._detail_super_low = value

    def serialize(self):
        return {
            "detail_level": self._detail_level,
            "detail_mode": self._detail_mode,
            "detail_bandwidth": self._detail_bandwidth,
            "detail_crispening": self._detail_crispening,
            "detail_hv_balance": self._detail_hv_balance,
            "detail_bw_balance": self._detail_bw_balance,
            "detail_limit": self._detail_limit,
            "detail_highlight": self._detail_highlight,
            "detail_super_low": self._detail_super_low
        }

    def deserialize(self, data):
        try:
            if not isinstance(data, dict):
                raise ValueError("I dati devono essere un dizionario.")

            self._detail_level = data.get("detail_level", self._detail_level)
            self._detail_mode = data.get("detail_mode", self._detail_mode)
            self._detail_bandwidth = data.get("detail_bandwidth", self._detail_bandwidth)
            self._detail_crispening = data.get("detail_crispening", self._detail_crispening)
            self._detail_hv_balance = data.get("detail_hv_balance", self._detail_hv_balance)
            self._detail_bw_balance = data.get("detail_bw_balance", self._detail_bw_balance)
            self._detail_limit = data.get("detail_limit", self._detail_limit)
            self._detail_highlight = data.get("detail_highlight", self._detail_highlight)
            self._detail_super_low = data.get("detail_super_low", self._detail_super_low)

        except Exception as e:
            print(f"Errore durante la deserializzazione: {e}")
            return False