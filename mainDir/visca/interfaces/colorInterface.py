import logging

from mainDir.visca.dictionary.dictionaries import colorDictionary
from mainDir.visca.dictionary.enumerations import *
from mainDir.visca.dataStucture.commandProcessor import CommandProcessor
from mainDir.visca.memories.colorMemories import ColorMemories
from mainDir.visca.baseClasses.baseInterfaceClass import BaseInterfaceClass



class ColorInterface(BaseInterfaceClass):

    def __init__(self, _colorMemories: ColorMemories, _commandMap: dict):
        super().__init__()
        self.colorMemories = _colorMemories
        self.command_map = _commandMap
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setWhiteBalanceMode(self, mode: WhiteBalanceModeEnum):
        """
        Seleziona la modalità di bilanciamento del bianco.

        Modalità disponibili:
        - **AUTO1**: Regola automaticamente il colore per avvicinarlo
          all'immagine visualizzata.
        - **AUTO2**: Regola automaticamente il bilanciamento del bianco
          per riprodurre i colori originali degli oggetti, eliminando le
          influenze dell’illuminazione ambiente.
        - **INDOOR**: Fissa R/B GAIN a una temperatura di colore di 3200 K.
        - **OUTDOOR**: Fissa R/B GAIN a una temperatura di colore di 5800 K.
        - **ONE PUSH**: Regola il bilanciamento del bianco al momento
          della pressione di specifici pulsanti (ad esempio, il pulsante
          HOME del telecomando o il pulsante ONE PUSH AWB del joystick)
          mentre si inquadra un soggetto bianco di grandi dimensioni.
        - **MANUAL**: Permette la regolazione manuale del bilanciamento
          del bianco.

        :param mode: Modalità di bilanciamento del bianco (WhiteBalanceModeEnum).
        :return: Comando inviato al processore.
        """
        self._last_command = None
        self.colorMemories.whiteBalanceMode = mode
        return self.processor.set("white_balance_mode", mode.value)

    def getWhiteBalanceMode(self):
        self._last_command = "get white_balance_mode"
        return self.processor.inquire("white_balance_mode")

    def onePushTrigger(self):
        self._last_command = None
        return self.processor.set("one_push_trigger")

    def setWBSpeed(self, value: int):
        """
        Imposta la velocità di convergenza del bilanciamento del bianco.

        Valori disponibili:
        - **1**: Lento.
        - **5**: Veloce.

        Questa impostazione è valida solo per le modalità AUTO1 e AUTO2.

        :param value: Velocità del bilanciamento del bianco (1-5).
        :return: Comando inviato.
        """
        self._last_command = None
        self.colorMemories.wbSpeed = value
        return self.processor.set("wb_speed", value)

    def getWBSpeed(self):
        self._last_command = "get wb_speed"
        return self.processor.inquire("wb_speed")

    def setOffset(self, value : int):
        """
            Sposta il punto di convergenza del bilanciamento del bianco.

            Valori disponibili:
            - **-7**: Spostamento massimo verso il blu.
            - **+7**: Spostamento massimo verso il rosso.

            Applicabile alle modalità AUTO1, AUTO2 e ONE PUSH.

            :param value: Offset per il bilanciamento del bianco (0 a 14).
            :return: Comando inviato.
            """
        if value < -7 or value > 7:
            raise ValueError("Valore fuori range per setOffset secondo lo standard VISCA.")
        self._last_command = None
        self.colorMemories.offset = value
        value = value + 7
        return self.processor.set("offset_value", value)

    def getOffset(self):
        self._last_command = "get offset_value"
        return self.processor.inquire("offset_value")

    def setRGainReset(self):
        self._last_command = None
        self.colorMemories.rGain = 80
        return self.processor.set("r_gain_reset")

    def setRGainUp(self):
        self._last_command = None
        if self.colorMemories.rGain < 127:
            self.colorMemories.rGain += 1
        else:
            self.colorMemories.rGain = 127
        return self.processor.set("r_gain_up")

    def setRGainDown(self):
        self._last_command = None
        if self.colorMemories.rGain > -128:
            self.colorMemories.rGain -= 1
        else:
            self.colorMemories.rGain = -128
        return self.processor.set("r_gain_down")

    def setRGain(self, value: int):
        """
        Imposta manualmente il valore del Red Gain (R GAIN).

        Valori disponibili:
        - Da -128 a +127.

        Valido solo per la modalità MANUAL.

        :param value: Valore per il Red Gain.
        :return: Comando inviato.
        """
        if value < -128 or value > 127:
            raise ValueError("Valore fuori range per setRGain secondo lo standard VISCA.")

        self._last_command = None
        self.colorMemories.rGain = value
        value = value + 128
        return self.processor.set("r_gain_value", value)

    def getRGain(self):
        self._last_command = "get r_gain_value"
        return self.processor.inquire("r_gain_value")

    def setBGainReset(self):
        self._last_command = None
        self.colorMemories.bGain = 80
        return self.processor.set("b_gain_reset")

    def setBGainUp(self):
        self._last_command = None
        if self.colorMemories.bGain < 127:
            self.colorMemories.bGain += 1
        else:
            self.colorMemories.bGain = 127
        return self.processor.set("b_gain_up")

    def setBGainDown(self):
        self._last_command = None
        if self.colorMemories.bGain > -128:
            self.colorMemories.bGain -= 1
        else:
            self.colorMemories.bGain = -128
        return self.processor.set("b_gain_down")

    def setBGain(self, value: int):
        """
        Imposta manualmente il valore del Blue Gain (B GAIN).

        Valori disponibili:
        - Da **-128** a **+127**.

        Valido solo per la modalità MANUAL.

        :param value: Valore per il Blue Gain.
        :return: Comando inviato.
        """

        if value < -128 or value > 127:
            raise ValueError("Valore fuori range per setBGain secondo lo standard VISCA.")
        self._last_command = None
        self.colorMemories.bGain = value
        value = value + 128
        return self.processor.set("b_gain_value", value)

    def getBGain(self):
        self._last_command = "get b_gain_value"
        return self.processor.inquire("b_gain_value")

    def setChromaSuppressMode(self, mode: ChromaSuppressionEnum):
        """
        Imposta la modalità di soppressione cromatica.

        Modalità disponibili:
        - **OFF**: Soppressione cromatica disattivata.
        - **LOW**: Soppressione cromatica leggera.
        - **HIGH**: Soppressione cromatica intensa.

        :param mode: Modalità di soppressione cromatica (ChromaSuppressionEnum).
        :return: Comando inviato.
        """
        self._last_command = None
        self.colorMemories.chromaSuppression = mode
        return self.processor.set("chroma_suppress", mode.value)

    def getChromaSuppressMode(self):
        """
        Recupera la modalità attuale di soppressione cromatica.

        :return: Modalità attuale (ChromaSuppressionEnum).
        """
        self._last_command = "get chroma_suppress"
        return self.processor.inquire("chroma_suppress")

    def setMatrixMode(self, value: MatrixSelectEnum):
        """
        Seleziona una matrice preimpostata per il calcolo.

        Opzioni disponibili:
        - **STD**, **HIGH SAT**, **FL LIGHT**, **MOVIE**, **STILL**,
          **CINEMA**, **PRO**, **ITU709**, **B/W**.

        Non valido se MATRIX è impostato su OFF.

        :param value: Matrice da selezionare (MatrixSelectEnum).
        :return: Comando inviato.
        """
        self._last_command = None
        self.colorMemories.matrix = value
        return self.processor.set("matrix_mode", value.value)

    def getMatrixMode(self):
        """
        Recupera la modalità attuale della matrice.

        :return: Matrice attuale (MatrixSelectEnum).
        """
        self._last_command = "get matrix_mode"
        return self.processor.inquire("matrix_mode")

    def setLevelReset(self):
        """
        Reimposta il livello di colore al valore predefinito (4).

        :return: Comando inviato.
        """
        self._last_command = None
        self.colorMemories.saturation = 4
        return self.processor.set("level_reset")

    def setLevelUp(self):
        """
        Incrementa il livello di colore.

        :return: Comando inviato.
        """
        self._last_command = None
        if self.colorMemories.saturation < 14:
            self.colorMemories.saturation += 1
        else:
            self.colorMemories.saturation = 14
        return self.processor.set("level_up")

    def setLevelDown(self):
        """
        Decrementa il livello di colore.

        :return: Comando inviato.
        """
        self._last_command = None
        if self.colorMemories.saturation > 0:
            self.colorMemories.saturation -= 1
        else:
            self.colorMemories.saturation = 0
        return self.processor.set("level_down")

    def setLevel(self, value: int):
        """
        Regola la densità del colore nell'immagine.

        Valori disponibili:
        - **0**: Colori meno densi.
        - **14**: Colori più densi.

        Non valido se MATRIX è impostato su OFF.

        :param value: Livello di densità del colore (0-14).
        :return: Comando inviato.
        """
        if value < 0 or value > 14:
            raise ValueError("Valore fuori range per setLevel secondo lo standard VISCA.")
        self._last_command = None
        self.colorMemories.saturation = value
        return self.processor.set("level_value", value)

    def getLevel(self):
        """
        Recupera il livello attuale di densità del colore.

        :return: Livello attuale (0-14).
        """
        self._last_command = "get level_value"
        return self.processor.inquire("level_value")

    def setPhaseReset(self):
        """
        Reimposta la fase al valore predefinito.

        :return: Comando inviato.
        """
        self._last_command = None
        self.colorMemories.phase = 0
        return self.processor.set("phase_reset")

    def setPhaseUp(self):
        """
        Incrementa la fase.

        :return: Comando inviato.
        """
        self._last_command = None
        if self.colorMemories.phase < 7:
            self.colorMemories.phase += 1
        else:
            self.colorMemories.phase = 7
        return self.processor.set("phase_up")

    def setPhaseDown(self):
        """
        Decrementa la fase.

        :return: Comando inviato.
        """
        self._last_command = None
        if self.colorMemories.phase > -7:
            self.colorMemories.phase -= 1
        else:
            self.colorMemories.phase = -7
        return self.processor.set("phase_down")

    def setPhase(self, value: int):
        """
        Regola la tonalità generale del colore dell'immagine.

        Valori disponibili:
        - Da **-7** a **+7**.

        Non valido se MATRIX è impostato su OFF.

        :param value: Valore della fase (-7 a +7).
        :return: Comando inviato.
        """
        if value < -7 or value > 7:
            raise ValueError("Valore fuori range per setPhase secondo lo standard VISCA.")
        self._last_command = None
        self.colorMemories.phase = value
        value += 7
        return self.processor.set("phase_value", value)

    def getPhase(self):
        """
        Recupera il valore attuale della fase.

        :return: Valore della fase (-7 a +7).
        """
        self._last_command = "get phase_value"
        return self.processor.inquire("phase_value")

    def setRG(self, value: int):
        """
        Imposta il coefficiente per la combinazione R-G.

        Valori disponibili:
        - Da -99 a +99

        Non valido se MATRIX è impostato su OFF.
        :param value: Valore del coefficiente (0-255).
        :return: Comando inviato.
        """

        self._last_command = None
        if value < -99 or value > 99:
            raise ValueError("Valore fuori range per setRG secondo lo standard VISCA.")
        self.colorMemories.rG = value
        value = value + 99
        return self.processor.set("r_g_value", value)

    def getRG(self):
        self._last_command = "get r_g_value"
        return self.processor.inquire("r_g_value")

    def setRB(self, value: int):
        """
        Imposta il coefficiente per la combinazione R-B.

        Valori disponibili:
        - Da 0-255

        Non valido se MATRIX è impostato su OFF.

        :param value: Valore del coefficiente
        :return: Comando inviato.
        """

        self._last_command = None
        if value < -99 or value > 99:
            raise ValueError("Valore fuori range per setRB secondo lo standard")
        self.colorMemories.rB = value
        value = value + 99
        return self.processor.set("r_b_value", value)

    def getRB(self):
        self._last_command = "get r_b_value"
        return self.processor.inquire("r_b_value")

    def setGR(self, value: int):
        """
        Imposta il coefficiente per la combinazione G-R.

        Valori disponibili:
        - Da -99 a +99

        Non valido se MATRIX è impostato su OFF.

        :param value: Valore del coefficiente
        :return: Comando inviato.
        """

        self._last_command = None
        if value < -99 or value > 99:
            raise ValueError("Valore fuori range per setGR secondo lo standard VISCA.")
        self.colorMemories.gR = value
        value = value + 99
        return self.processor.set("g_r_value", value)

    def getGR(self):
        self._last_command = "get g_r_value"
        return self.processor.inquire("g_r_value")

    def setGB(self, value: int):
        """
        Imposta il coefficiente per la combinazione G-B.

        Valori disponibili:
        - Da -99 a +99

        Non valido se MATRIX è impostato su OFF.

        :param value: Valore del coefficiente
        :return: Comando inviato.
        """

        self._last_command = None
        if value < -99 or value > 99:
            raise ValueError("Valore fuori range per setGB secondo lo standard VISCA.")
        self.colorMemories.gB = value
        value = value + 99
        return self.processor.set("g_b_value", value)

    def getGB(self):
        self._last_command = "get g_b_value"
        return self.processor.inquire("g_b_value")

    def setBR(self, value: int):
        """
        Imposta il coefficiente per la combinazione B-R.

        Valori disponibili:
        - Da -99 a +99

        Non valido se MATRIX è impostato su OFF.

        :param value: Valore del coefficiente
        :return: Comando inviato.
        """
        self._last_command = None
        if value < -99 or value > 99:
            raise ValueError("Valore fuori range per setBR secondo lo standard VISCA.")
        self.colorMemories.bR = value
        value = value + 99
        return self.processor.set("b_r_value", value)

    def getBR(self):
        self._last_command = "get b_r_value"
        return self.processor.inquire("b_r_value")

    def setBG(self, value: int):
        """
        Imposta il coefficiente per la combinazione B-G.

        Valori disponibili:
        - Da -99 a +99

        Non valido se MATRIX è impostato su OFF.

        :param value: Valore del coefficiente
        :return: Comando inviato.
        """
        self._last_command = None
        if value < -99 or value > 99:
            raise ValueError("Valore fuori range per setBG secondo lo standard VISCA.")
        self.colorMemories.bG = value
        value = value + 99
        return self.processor.set("b_g_value", value)

    def getBG(self):
        self._last_command = "get b_g_value"
        return self.processor.inquire("b_g_value")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    colorMemories = ColorMemories()
    color = ColorInterface(colorMemories, colorDictionary)

    print(color.__class__.__dict__.keys())
    print("SET WHITE BALANCE MODE")
    print(color.getWhiteBalanceMode())
    print(color.setWhiteBalanceMode(WhiteBalanceModeEnum.AUTO_1))
    print(color.getWhiteBalanceMode())
    print("ONE PUSH TRIGGER")
    print(color.onePushTrigger())
    print("RG GAIN")
    print(color.setRGainReset())
    print(color.setRGainUp())
    print(color.setRGainDown())
    print(f"RG GAIN: {color.setRGain(125)}")
    print(f"RG GAIN: {color.setRGain(50)}")

    print(color.getRGain())
    print("BG GAIN")
    print(color.setBGainReset())
    print(color.setBGainUp())
    print(color.setBGainDown())
    print(color.setBGain(125))
    print(color.getBGain())
    print("WB OFFSET")
    print(color.setOffset(2))
    print(color.getOffset())
    print("CHROMA SUPPRESS")
    print(color.setChromaSuppressMode(ChromaSuppressionEnum.WEAK))
    print(color.getChromaSuppressMode())
    print("MATRIX MODE")
    print(color.setMatrixMode(MatrixSelectEnum.STD))
    print(color.getMatrixMode())
    print("LEVEL")
    print(color.setLevelReset())
    print(color.setLevelUp())
    print(color.setLevelDown())
    print(color.setLevel(2))
    print(color.getLevel())
    print("PHASE")
    print(color.setPhaseReset())
    print(color.setPhaseUp())
    print(color.setPhaseDown())
    print(color.setPhase(2))
    print(color.getPhase())
    print("RG")

