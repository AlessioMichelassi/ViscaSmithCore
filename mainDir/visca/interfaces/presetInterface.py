from mainDir.visca.dictionary.dictionaries import presetDictionary
from mainDir.visca.baseClasses.baseInterfaceClass import BaseInterfaceClass
from mainDir.visca.dataStucture.commandProcessor import CommandProcessor


class PresetInterface(BaseInterfaceClass):
    def __init__(self, _presetDictionary: dict):
        super().__init__()
        self.command_map = _presetDictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    def setDictionary(self, dictionary):
        self.command_map = dictionary
        self.processor = CommandProcessor(self.command_map)
        self.setup()

    # Reset Preset
    def resetPreset(self, preset_number: int):
        if preset_number not in self.command_map["preset_reset"]["allowed_values"]:
            raise ValueError("Preset number fuori range.")
        return self.processor.set("preset_reset", preset_number)

    def inquireResetPreset(self):
        return self.processor.inquire("preset_reset")

    # Set Preset
    def setPreset(self, preset_number: int):
        if preset_number not in self.command_map["preset_set"]["allowed_values"]:
            raise ValueError("Preset number fuori range.")
        return self.processor.set("preset_set", preset_number)

    def inquireSetPreset(self):
        return self.processor.inquire("preset_set")

    # Recall Preset
    def recallPreset(self, preset_number: int):
        if preset_number not in self.command_map["preset_recall"]["allowed_values"]:
            raise ValueError("Preset number fuori range.")
        return self.processor.set("preset_recall", preset_number)

    def inquireRecallPreset(self):
        return self.processor.inquire("preset_recall")

    # Preset Speed Select
    def setPresetSpeedSelect(self, mode: int):
        if mode not in self.command_map["preset_speed_select"]["allowed_values"]:
            raise ValueError("Modalità di velocità non valida.")
        return self.processor.set("preset_speed_select", mode)

    def inquirePresetSpeedSelect(self):
        return self.processor.inquire("preset_speed_select")

    # Preset Speed Separate
    def setPresetSpeedSeparate(self, preset_number: int, position_speed: int):
        if preset_number not in self.command_map["preset_speed_separate"]["allowed_values"]["preset_number"]:
            raise ValueError("Preset number fuori range.")
        if position_speed not in self.command_map["preset_speed_separate"]["allowed_values"]["position_speed"]:
            raise ValueError("Velocità posizione fuori range.")
        return self.processor.set("preset_speed_separate", preset_number, position_speed)

    def inquirePresetSpeedSeparate(self):
        return self.processor.inquire("preset_speed_separate")

    # Preset Speed Common
    def setPresetSpeedCommon(self, speed: int):
        if speed not in self.command_map["preset_speed_common"]["allowed_values"]:
            raise ValueError("Velocità comune fuori range.")
        return self.processor.set("preset_speed_common", speed)

    def inquirePresetSpeedCommon(self):
        return self.processor.inquire("preset_speed_common")

    # Preset Mode
    def setPresetMode(self, mode: int):
        if mode not in self.command_map["preset_mode"]["allowed_values"]:
            raise ValueError("Modalità preset non valida.")
        return self.processor.set("preset_mode", mode)

    def inquirePresetMode(self):
        return self.processor.inquire("preset_mode")

    # Preset Call Mode
    def setPresetCallMode(self, mode: int):
        if mode not in self.command_map["preset_call_mode"]["allowed_values"]:
            raise ValueError("Modo di richiamo preset non valido.")
        return self.processor.set("preset_call_mode", mode)

    def inquirePresetCallMode(self):
        return self.processor.inquire("preset_call_mode")


if __name__ == "__main__":
    interface = PresetInterface(presetDictionary)

    # Esempi di utilizzo
    print("Reset Preset:", interface.resetPreset(1))
    print("Set Preset:", interface.setPreset(5))
    print("Recall Preset:", interface.recallPreset(10))
    print("Set Preset Speed Select:", interface.setPresetSpeedSelect(2))
    print("Set Preset Speed Separate:", interface.setPresetSpeedSeparate(10, 15))
    print("Set Preset Speed Common:", interface.setPresetSpeedCommon(10))
    print("Set Preset Mode:", interface.setPresetMode(1))
    print("Set Preset Call Mode:", interface.setPresetCallMode(3))
