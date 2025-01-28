exposureDictionary = {
    "exposure_mode": {
        "cmd": "04 39 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità di esposizione",
        "allowed_values": [0, 3, 10, 11],
        "inquire": "04 39",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_exposure_mode"
    },
    "iris_reset": {
        "cmd": "04 0B 00",
        "type": "setNoValue",
        "tip": "Resetta l'iris al valore predefinito (F2.0)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_iris"
    },
    "iris_up": {
        "cmd": "04 0B 02",
        "type": "setNoValue",
        "tip": "Aumenta l'apertura dell'iris",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_iris"
    },
    "iris_down": {
        "cmd": "04 0B 03",
        "type": "setNoValue",
        "tip": "Diminuisce l'apertura dell'iris",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_iris"
    },
    "iris_value": {
        "cmd": "04 4B 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente l'apertura dell'iris",
        "allowed_values": list(range(0, 21)),
        "inquire": "04 4B",
        "reply_format": "00 00 pp",
        "placeholder": ["pp"],
        "state": "_iris"
    },
    "gain_reset": {
        "cmd": "04 0C 00",
        "type": "setNoValue",
        "tip": "Resetta il guadagno (0 dB)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_gain"
    },
    "gain_up": {
        "cmd": "04 0C 02",
        "type": "setNoValue",
        "tip": "Aumenta il guadagno",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_gain"
    },
    "gain_down": {
        "cmd": "04 0C 03",
        "type": "setNoValue",
        "tip": "Diminuisce il guadagno",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_gain"
    },
    "gain_value": {
        "cmd": "04 4C 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il guadagno",
        "allowed_values": list(range(0, 16)),
        "inquire": "04 4C",
        "reply_format": "00 00 pp",
        "placeholder": ["pp"],
        "state": "_gain"
    },
    "gain_limit_value": {
        "cmd": "04 2C pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il limite del guadagno",
        "allowed_values": list(range(0, 16)),
        "inquire": "04 2C",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_gain_limit_value"
    },
    "gain_point_mode": {
        "cmd": "05 0C pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità del punto guadagno on/off",
        "allowed_values": [2, 3],
        "inquire": "05 0C",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_gain_point_mode"
    },
    "gain_point_value": {
        "cmd": "01 05 4C pp",
        "type": "setWithValue",
        "tip": "Imposta il valore del punto guadagno",
        "allowed_values": list(range(0, 16)),
        "inquire": "05 4C",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_gain_point_value"
    },
    "shutter_reset": {
        "cmd": "04 0A 00",
        "type": "setNoValue",
        "tip": "Resetta lo shutter al valore predefinito",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_shutter"
    },
    "shutter_up": {
        "cmd": "04 0A 02",
        "type": "setNoValue",
        "tip": "Aumenta la velocità dell'otturatore (shutter)",
        "allowed_values": list(range(0, 31)),
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_shutter"
    },
    "shutter_down": {
        "cmd": "04 0A 03",
        "type": "setNoValue",
        "tip": "Diminuisce la velocità dell'otturatore",
        "allowed_values": list(range(0, 31)),
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_shutter"
    },
    "shutter_value": {
        "cmd": "04 4A 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore dello shutter",
        "allowed_values": list(range(0, 31)),
        "inquire": "04 4A",
        "reply_format": "00 00 pp",
        "placeholder": ["pp"],
        "state": "_shutter"
    },
    "max_shutter_value": {
        "cmd": "05 2A 00 pp",
        "type": "setWithValue",
        "tip": "Imposta il valore massimo dello shutter",
        "allowed_values": list(range(0, 31)),
        "inquire": "05 2A 00",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_max_shutter_value"
    },
    "min_shutter_value": {
        "cmd": "05 2A 01 pp",
        "type": "setWithValue",
        "tip": "Imposta il valore minimo dello shutter",
        "allowed_values": list(range(0, 31)),
        "inquire": "05 2A 01",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_min_shutter_value"
    },
    "auto_slow_shutter_mode": {
        "cmd": "04 5A pp",
        "type": "setWithValue",
        "tip": "Imposta lo slow shutter automatico",
        "allowed_values": [2, 3],
        "inquire": "04 5A",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_auto_slow_shutter_mode"
    },
    "ae_speed_value": {
        "cmd": "04 5D pp",
        "type": "setWithValue",
        "tip": "Imposta la velocità dell'esposizione automatica",
        "allowed_values": list(range(0, 31)),
        "inquire": "04 5A",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_ae_speed_value"
    },
    "exp_comp_mode": {
        "cmd": "04 3E pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita la compensazione esposizione",
        "allowed_values": [2, 3],
        "inquire": "04 3E",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_exp_comp_mode"
    },
    "exp_comp_value": {
        "cmd": "04 4E 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore della compensazione esposizione",
        "allowed_values": list(range(0, 8)),
        "inquire": "04 4E",
        "reply_format": "00 00 pp pp",
        "placeholder": ["pp"],
        "state": "_exp_comp_value"
    },
    "exp_comp_reset": {
        "cmd": "04 0E 00",
        "type": "setNoValue",
        "tip": "Resetta la compensazione esposizione al valore predefinito",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_exp_comp_value"
    },
    "exp_comp_up": {
        "cmd": "04 0E 02",
        "type": "setNoValue",
        "tip": "Aumenta il valore della compensazione esposizione",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_exp_comp_value"
    },
    "exp_comp_down": {
        "cmd": "04 0E 03",
        "type": "setNoValue",
        "tip": "Diminuisce il valore della compensazione esposizione",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_exp_comp_value"
    },
    "backlight_mode": {
        "cmd": "04 33 pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita il backlight",
        "allowed_values": [2, 3],
        "inquire": "04 33",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_backlight_mode"
    },
    "spotlight_mode": {
        "cmd": "04 3A pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita lo spotlight",
        "allowed_values": [2, 3],
        "inquire": "04 3A",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_spotlight_mode"
    },
    "visibility_enhancer_mode": {
        "cmd": "04 3D pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita il Visibility Enhancer",
        "allowed_values": [6, 3],
        "inquire": "04 3D",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_visibility_enhancer_mode"
    },
    "visibility_enhancer_values": {
        "cmd": "04 2D 00 00 pp qq rr 00 00 00 00 FF",
        "type": "setWithValues",
        "tip": "Imposta il livello, la compensazione e la luminosità del Visibility Enhancer",
        "allowed_values": {
            "effect_level": list(range(0, 7)),
            "brightness_compensation": list(range(0, 4)),
            "compensation_level": [0, 1, 2]
        },
        "placeholder": ["pp", "qq", "rr"],
        "inquire": "04 2D",
        "reply_format": "00 00 pp qq rr 00 00 00 00",
        "state": "_visibility_enhancer_values"
    },
    "low_light_bias_mode": {
        "cmd": "05 39 pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita il Low Light Basis Brightness",
        "allowed_values": [2, 3],
        "inquire": "05 39",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_low_light_bias_mode"
    },
    "low_light_bias_value": {
        "cmd": "05 49 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello del Low Light Basis Brightness",
        "allowed_values": ["04", "05", "06", "07", "08", "09", "0A"],
        "inquire": "05 49",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_low_light_bias_value"
    },
    "high_sensitivity_mode": {
        "cmd": "05 3A pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita la modalità di alta sensibilità",
        "allowed_values": [2, 3],
        "inquire": "05 3A",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_high_sensitivity_mode"
    }
}

colorDictionary = {
    "white_balance_mode": {
        "cmd": "04 35 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità del bilanciamento del bianco",
        "allowed_values": [0, 1, 2, 3, 4, 5],
        "inquire": "04 35",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_whiteBalanceMode"
    },
    "one_push_trigger": {
        "cmd": "04 10 05",
        "type": "setNoValue",
        "tip": "Esegue il One Push WB Trigger",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_onePushTrigger"
    },
    "r_gain_reset": {
        "cmd": "04 03 00",
        "type": "setNoValue",
        "tip": "Resetta il Red Gain al valore 80 (0)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_rGain"
    },
    "r_gain_up": {
        "cmd": "04 03 02",
        "type": "setNoValue",
        "tip": "Aumenta il Red Gain",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_rGain"
    },
    "r_gain_down": {
        "cmd": "04 03 03",
        "type": "setNoValue",
        "tip": "Diminuisce il Red Gain",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_rGain"
    },
    "r_gain_value": {
        "cmd": "04 43 00 00 pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore del Red Gain",
        "allowed_values": list(range(-128, 128)),
        "inquire": "04 43",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_rGainValue"
    },
    "b_gain_reset": {
        "cmd": "04 04 00",
        "type": "setNoValue",
        "tip": "Resetta il Blue Gain al valore 80 (0)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_bGain"
    },
    "b_gain_up": {
        "cmd": "04 04 02",
        "type": "setNoValue",
        "tip": "Aumenta il Blue Gain",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_bGain"
    },
    "b_gain_down": {
        "cmd": "04 04 03",
        "type": "setNoValue",
        "tip": "Diminuisce il Blue Gain",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_bGain"
    },
    "b_gain_value": {
        "cmd": "04 44 00 00 pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore del Blue Gain",
        "allowed_values": list(range(-128, 128)),
        "inquire": "04 44",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_bGainValue"
    },
    "wb_speed": {
        "cmd": "04 56 pp",
        "type": "setWithValue",
        "tip": "Imposta la velocità (1 = lento, 5 = veloce)",
        "allowed_values": [1, 2, 3, 4, 5],
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["p"],
        "state": "_wb_speed"
    },
    "offset_value": {
        "cmd": "7E 01 2E 01 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore di offset",
        "allowed_values": [-7, 0, 7],
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_offsetValue"
    },
    "chroma_suppress": {
        "cmd": "04 5F 0p",
        "type": "setWithValue",
        "tip": "Imposta la soppressione cromatica",
        "allowed_values": [0, 1, 3],
        "inquire": "04 5F",
        "reply_format": "0p",
        "placeholder": ["p"],
        "state": "_chromaSuppress"
    },
    "matrix_mode": {
        "cmd": "7E 01 3D pp",
        "type": "setWithValue",
        "tip": "Seleziona il tipo di matrice",
        "allowed_values": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_matrixSelect"
    },
    "level_reset": {
        "cmd": "04 09 00",
        "type": "setNoValue",
        "tip": "Resetta il livello al valore predefinito (4)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_level"
    },
    "level_up": {
        "cmd": "04 09 02",
        "type": "setNoValue",
        "tip": "Aumenta il livello",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_level"
    },
    "level_down": {
        "cmd": "04 09 03",
        "type": "setNoValue",
        "tip": "Diminuisce il livello",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_level"
    },
    "level_value": {
        "cmd": "04 49 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il livello",
        "allowed_values": list(range(0, 15)),
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_levelValue"
    },
    "phase_reset": {
        "cmd": "04 0F 00",
        "type": "setNoValue",
        "tip": "Resetta la fase al valore predefinito (7)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_phase"
    },
    "phase_up": {
        "cmd": "04 0F 02",
        "type": "setNoValue",
        "tip": "Aumenta la fase",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_phase"
    },
    "phase_down": {
        "cmd": "04 0F 03",
        "type": "setNoValue",
        "tip": "Diminuisce la fase",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_phase"
    },
    "phase_value": {
        "cmd": "04 4F 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente la fase",
        "allowed_values": list(range(0, 14)),
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_phaseValue"
    },
    "r_g_value": {
        "cmd": "01 7E 01 7A pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore R-B",
        "allowed_values": [-99, 0, 99],
        "inquire": None,
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_rGValue"
    },
    "r_b_value": {
        "cmd": "7E 01 7B pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore R-B",
        "allowed_values": [-99, 0, 99],
        "inquire": None,
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_rBValue"
    },
    "g_r_value": {
        "cmd": "7E 01 7C pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore G-R",
        "allowed_values": [-99, 0, 99],
        "inquire": None,
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_gRValue"
    },
    "g_b_value": {
        "cmd": "7E 01 7D pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore G-B",
        "allowed_values": [-99, 0, 99],
        "inquire": None,
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_gBValue"
    },
    "b_r_value": {
        "cmd": "7E 01 7E pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore B-R",
        "allowed_values": [-99, 0, 99],
        "inquire": None,
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_bRValue"
    },
    "b_g_value": {
        "cmd": "7E 01 7F pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il valore B-G",
        "allowed_values": [-99, 0, 99],
        "inquire": None,
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_bGValue"
    }
}

detailDictionary = {
    "detail_level_reset": {
        "cmd": "04 42 00",
        "type": "setNoValue",
        "tip": "Resetta il livello del dettaglio al valore predefinito (7)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_detailLevel"
    },
    "detail_level_up": {
        "cmd": "04 42 02",
        "type": "setNoValue",
        "tip": "Aumenta il livello del dettaglio",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_detailLevel"
    },
    "detail_level_down": {
        "cmd": "04 42 03",
        "type": "setNoValue",
        "tip": "Diminuisce il livello del dettaglio",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_detailLevel"
    },
    "detail_level_value": {
        "cmd": "04 42 00 00 pp ",
        "type": "setWithValue",
        "tip": "Imposta direttamente il livello del dettaglio",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "inquire": "04 42",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailLevel"
    },
    "detail_mode": {
        "cmd": "05 42 01 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità del dettaglio (Auto o Manuale)",
        "allowed_values": [0, 1],
        "inquire": "05 42 01",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailMode"
    },
    "detail_bandwidth": {
        "cmd": "05 42 02 pp",
        "type": "setWithValue",
        "tip": "Imposta la larghezza di banda del dettaglio",
        "allowed_values": [0, 1, 2, 3, 4],
        "inquire": "05 42 02",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailBandwidth"
    },
    "detail_crispening": {
        "cmd": "05 42 03 pp",
        "type": "setWithValue",
        "tip": "Imposta il valore di crispening",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": "05 42 03",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailCrispening"
    },
    "detail_hv_balance": {
        "cmd": "05 42 04 pp",
        "type": "setWithValue",
        "tip": "Imposta il bilanciamento HV",
        "allowed_values": [5, 6, 7, 8, 9],
        "inquire": "05 42 04",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailHVBalance"
    },
    "detail_bw_balance": {
        "cmd": "05 42 05 pp",
        "type": "setWithValue",
        "tip": "Imposta il bilanciamento BW",
        "allowed_values": [0, 1, 2, 3, 4],
        "inquire": "05 42 05",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailBWBalance"
    },
    "detail_limit": {
        "cmd": "05 42 06 pp",
        "type": "setWithValue",
        "tip": "Imposta il limite massimo del dettaglio",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": "05 42 06",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailLimit"
    },
    "detail_highlight": {
        "cmd": "05 42 07 pp",
        "type": "setWithValue",
        "tip": "Imposta il dettaglio delle alte luci",
        "allowed_values": [0, 1, 2, 3, 4],
        "inquire": "05 42 07",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailHighlight"
    },
    "detail_super_low": {
        "cmd": "05 42 08 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello di super low detail",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": "05 42 08",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_detailSuperLow"
    }
}

kneeDictionary = {
    "knee_setting": {
        "cmd": "7E 01 6D pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita il Knee Setting",
        "allowed_values": [2, 3],
        "inquire": "7E 01 6D",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_kneeSetting"
    },
    "knee_mode": {
        "cmd": "7E 01 54 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità Knee (Auto/Manual)",
        "allowed_values": [0, 4],
        "inquire": "7E 01 54",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_kneeMode"
    },
    "knee_slope_value": {
        "cmd": "7E 01 6F pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente la pendenza (slope) del Knee",
        "allowed_values": list(range(0, 15)),
        "inquire": "7E 01 6F",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_kneeSlopeValue"
    },
    "knee_point_value": {
        "cmd": "7E 01 6E pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il punto Knee",
        "allowed_values": list(range(0, 13)),
        "inquire": "7E 01 6E",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_kneePointValue"
    }
}

gammaDictionary = {
    "gamma_select": {
        "cmd": "04 5B pp",
        "type": "setWithValue",
        "tip": "Seleziona il tipo di gamma",
        "allowed_values": list(range(0, 15)),
        "inquire": "04 5B",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_gammaSelect"
    },
    "gamma_pattern_value": {
        "cmd": "05 5B pp pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il pattern gamma",
        "allowed_values": list(range(0, 200)),
        "inquire": "05 5B",
        "reply_format": "pp pp pp",
        "placeholder": ["pp"],
        "state": "_gammaPatternValue"
    },
    "gamma_offset_value": {
        "cmd": "04 1E 00 00 00 pp qq qq",
        "type": "setWithValues",
        "tip": "Imposta direttamente l'offset gamma",
        "allowed_values": {
            "polarity": [0, 1],
            "width": list(range(0, 41)),
        },
        "inquire": "04 1E",
        "reply_format": "pp qq qq",
        "placeholder": ["pp", "qq"],
        "state": "_gammaOffsetValue"
    },
    "gamma_level_value": {
        "cmd": "7E 01 71 pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il livello gamma",
        "allowed_values": list(range(0, 15)),
        "inquire": "7E 01 71",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_gammaLevelValue"
    },
    "black_gamma_level_value": {
        "cmd": "7E 01 72 pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il livello della gamma nera",
        "allowed_values": list(range(0, 15)),
        "inquire": "7E 01 72",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_blackGammaLevelValue"
    },
    "black_gamma_range_value": {
        "cmd": "05 5C pp",
        "type": "setWithValue",
        "tip": "Imposta l'intervallo di correzione della gamma nera",
        "allowed_values": [0, 1, 2],
        "inquire": "05 5C",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_blackGammaRangeValue"
    },
    "black_level_reset": {
        "cmd": "7E 04 15 00",
        "type": "setNoValue",
        "tip": "Resetta il livello del nero al valore predefinito",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_blackLevel"
    },
    "black_level_up": {
        "cmd": "7E 04 15 02",
        "type": "setNoValue",
        "tip": "Aumenta il livello del nero",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_blackLevel"
    },
    "black_level_down": {
        "cmd": "7E 04 15 03",
        "type": "setNoValue",
        "tip": "Diminuisce il livello del nero",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_blackLevel"
    },
    "black_level_value": {
        "cmd": "7E 04 45 pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente il livello del nero",
        "allowed_values": list(range(0, 60)),
        "inquire": "7E 04 45",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_blackLevelValue"
    }
}

genericsDictionary = {
    "picture_profile": {
        "cmd": "7E 04 5F pp",
        "type": "setWithValue",
        "tip": "Seleziona il profilo immagine",
        "allowed_values": list(range(0, 5)),
        "inquire": "7E 04 5F",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_pictureProfile"
    },
    "flicker_cancel": {
        "cmd": "04 32 pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita il Flicker Cancel",
        "allowed_values": [2, 3],
        "inquire": "04 32",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_flickerCancel"
    },
    "image_stabilizer": {
        "cmd": "04 34 pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita lo stabilizzatore di immagine",
        "allowed_values": [2, 3],
        "inquire": "04 34",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_imageStabilizer"
    },
    "defog": {
        "cmd": "04 37 pp qq",
        "type": "setWithValues",
        "tip": "Abilita/disabilita il Defog e imposta il livello",
        "allowed_values": {
            "state": [2, 3],
            "level": [0, 1, 2, 3]
        },
        "inquire": "04 37",
        "reply_format": "pp qq",
        "placeholder": ["pp", "qq"],
        "state": "_defog"
    },
    "high_resolution": {
        "cmd": "04 52 pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita l'alta risoluzione",
        "allowed_values": [2, 3],
        "inquire": "04 52",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_highResolution"
    },
    "noise_reduction_level": {
        "cmd": "04 53 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello di Noise Reduction",
        "allowed_values": list(range(0, 7)), #7f è
        "inquire": "04 53",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_noiseReductionLevel"
    },
    "2d_3d_nr": {
        "cmd": "05 53 pp qq",
        "type": "setWithValues",
        "tip": "Imposta i livelli di 2D NR e 3D NR",
        "allowed_values": {
            "2d_nr": [0, 1, 2, 3, 4, 5],
            "3d_nr": [0, 1, 2, 3, 4, 5]
        },
        "inquire": "05 53",
        "reply_format": "pp qq",
        "placeholder": ["pp", "qq"],
        "state": "_2d3dNr"
    },
    "picture_effect": {
        "cmd": "04 63 0p",
        "type": "setWithValue",
        "tip": "Imposta l'effetto immagine",
        "allowed_values": [0, 4],
        "inquire": "04 63",
        "reply_format": "0p",
        "placeholder": ["p"],
        "state": "_pictureEffect"
    },
    "color_bar": {
        "cmd": "04 7D pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita la barra colore",
        "allowed_values": [2, 3],
        "inquire": "04 7D",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_colorBar"
    }
}

focusDictionary = {
    "focus_mode": {
        "cmd": "04 38 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità di messa a fuoco (Auto/Manuale/Toggle)",
        "allowed_values": [2, 3, 10],
        "inquire": "04 38",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_focusMode"
    },
    "focus_stop": {
        "cmd": "04 08 00",
        "type": "setNoValue",
        "tip": "Ferma la messa a fuoco",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_focusStop"
    },
    "focus_far_standard": {
        "cmd": "04 08 02",
        "type": "setNoValue",
        "tip": "Muove la messa a fuoco verso lontano (velocità standard)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_focusFarStandard"
    },
    "focus_near_standard": {
        "cmd": "04 08 03",
        "type": "setNoValue",
        "tip": "Muove la messa a fuoco verso vicino (velocità standard)",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_focusNearStandard"
    },
    "focus_far_variable": {
        "cmd": "04 08 2p",
        "type": "setWithValue",
        "tip": "Muove la messa a fuoco verso lontano con velocità variabile",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": None,
        "reply_format": "2p",
        "placeholder": ["2p"],
        "state": "_focusFarVariable"
    },
    "focus_near_variable": {
        "cmd": "04 08 3p",
        "type": "setWithValue",
        "tip": "Muove la messa a fuoco verso vicino con velocità variabile",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": None,
        "reply_format": "3p",
        "placeholder": ["3p"],
        "state": "_focusNearVariable"
    },
    "focus_value": {
        "cmd": "04 48 pp pp pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente la posizione della messa a fuoco",
        "allowed_values": [int(value, 16) for value in ["0000", "FFFF"]],
        "inquire": "04 48",
        "reply_format": "pp pp pp pp",
        "placeholder": ["pp"],
        "state": "_focusValue"
    },
    "focus_one_push_trigger": {
        "cmd": "04 18 01",
        "type": "setNoValue",
        "tip": "Attiva il trigger AF One Push",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_focusOnePushTrigger"
    },
    "focus_infinity": {
        "cmd": "04 18 02",
        "type": "setNoValue",
        "tip": "Imposta la messa a fuoco all'infinito",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_focusInfinity"
    },
    "focus_near_limit": {
        "cmd": "04 28 pp pp pp pp",
        "type": "setWithValue",
        "tip": "Imposta il limite di messa a fuoco più vicino",
        "allowed_values": [int(value, 16) for value in ["0000", "FFFF"]],
        "inquire": None,
        "reply_format": "pp pp pp pp",
        "placeholder": ["pp",],
        "state": "_focusNearLimit"
    },
    "af_mode": {
        "cmd": "04 57 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità Auto Focus (AF)",
        "allowed_values": [0, 1, 2],
        "inquire": "04 57",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_afMode"
    },
    "af_mode_interval": {
        "cmd": "04 27 pp pp qq qq",
        "type": "setWithValues",
        "tip": "Imposta l'intervallo di funzionamento AF",
        "allowed_values": {
            "af_operating_time": [0, 255],
            "af_stay_time": [0, 255]
        },
        "inquire": "04 27",
        "reply_format": "pp pp qq qq",
        "placeholder": ["pp", "qq"],
        "state": "_afModeInterval"
    },
    "af_sensitivity": {
        "cmd": "04 58 pp",
        "type": "setWithValue",
        "tip": "Imposta la sensibilità dell'AF",
        "allowed_values": [2, 3],
        "inquire": "04 58",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_afSensitivity"
    },
    "ir_correction": {
        "cmd": "04 11 pp",
        "type": "setWithValue",
        "tip": "Imposta la correzione IR",
        "allowed_values": [0, 1],
        "inquire": "04 11",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_irCorrection"
    }
}

zoomDictionary = {
    "stop_zoom": {
        "cmd": "04 07 00",
        "type": "setNoValue",
        "tip": "Stop zoom",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_zoomStop"
    },
    "tele_standard": {
        "cmd": "04 07 02",
        "type": "setNoValue",
        "tip": "Tele zoom standard",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_zoomTeleStandard"
    },
    "wide_standard": {
        "cmd": "04 07 03",
        "type": "setNoValue",
        "tip": "Wide zoom standard",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_zoomWideStandard"
    },
    "tele_variable": {
        "cmd": "04 07 2p",
        "type": "setWithValue",
        "tip": "Tele zoom variabile",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": None,
        "reply_format": "2p",
        "placeholder": ["2p"],
        "state": "_zoomTeleVariable"
    },
    "wide_variable": {
        "cmd": "04 07 3p",
        "type": "setWithValue",
        "tip": "Wide zoom variabile",
        "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7],
        "inquire": None,
        "reply_format": "3p",
        "placeholder": ["3p"],
        "state": "_zoomWideVariable"
    },
    "direct": {
        "cmd": "04 47 zz zz zz zz",
        "type": "setWithValue",
        "tip": "Set zoom diretto",
        "allowed_values": [
            int(value, 16) for value in [
                "0000", "0DC1", "186C", "2015", "2594", "29B7", "2CFB", "2FB0",
                "320C", "342D", "3608", "37AA", "391C", "3A66", "3B90", "3C9C",
                "3D91", "3E72", "3F40", "4000", "5556", "6000", "6AAB", "7000",
                "7334", "7556", "76DC", "7800", "78E4", "799A", "7A2F", "7AC0"
            ]
        ],
        "inquire": "04 47",
        "reply_format": "zz zz zz zz",
        "placeholder": ["zz"],
        "state": "_zoomDirect"
    },
    "mode": {
        "cmd": "04 06 pp",
        "type": "setWithValue",
        "tip": "Set modalità",
        "allowed_values": [2, 3, 4],
        "inquire": "04 06",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_zoomMode"
    },
    "tele_convert": {
        "cmd": "7E 04 36 pp",
        "type": "setWithValue",
        "tip": "Convertitore tele",
        "allowed_values": [2, 3],
        "inquire": "7E 04 36",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_zoomTeleConvert"
    },
    "digital_zoom_on": {
        "cmd": "04 06 02",
        "type": "setNoValue",
        "tip": "Attiva zoom digitale",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_digitalZoomOn"
    },
    "digital_zoom_off": {
        "cmd": "04 06 03",
        "type": "setNoValue",
        "tip": "Disattiva zoom digitale",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_digitalZoomOff"
    },
    "clear_image_zoom_on": {
        "cmd": "04 06 04",
        "type": "setNoValue",
        "tip": "Attiva Clear Image Zoom",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_clearImageZoomOn"
    },
    "clear_image_zoom_off": {
        "cmd": "04 06 03",
        "type": "setNoValue",
        "tip": "Disattiva Clear Image Zoom",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_clearImageZoomOff"
    }
}

panTiltDictionary = {
    "pan_tilt_drive_up": {
        "cmd": "06 01 vv ww 03 01",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso l'alto con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveUp"
    },
    "pan_tilt_drive_down": {
        "cmd": "06 01 vv ww 03 02",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso il basso con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveDown"
    },
    "pan_tilt_drive_left": {
        "cmd": "06 01 vv ww 01 03",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso sinistra con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveLeft"
    },
    "pan_tilt_drive_right": {
        "cmd": "06 01 vv ww 02 03",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso destra con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveRight"
    },
"pan_tilt_drive_up_left": {
        "cmd": "06 01 vv ww 01 01",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso l'alto a sinistra con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveUpLeft"
    },
    "pan_tilt_drive_up_right": {
        "cmd": "06 01 vv ww 02 01",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso l'alto a destra con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveUpRight"
    },
    "pan_tilt_drive_down_left": {
        "cmd": "06 01 vv ww 01 02",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso il basso a sinistra con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveDownLeft"
    },
    "pan_tilt_drive_down_right": {
        "cmd": "06 01 vv ww 02 02",
        "type": "setWithValues",
        "tip": "Muove la telecamera verso il basso a destra con velocità pan e tilt specificata",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveDownRight"
    },
    "pan_tilt_drive_stop": {
        "cmd": "06 01 vv ww 03 03",
        "type": "setWithValues",
        "tip": "Ferma il movimento di pan/tilt",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17]
        },
        "inquire": None,
        "reply_format": "vv ww",
        "placeholder": ["vv", "ww"],
        "state": "_panTiltDriveStop"
    },
    "pan_tilt_absolute_position": {
        "cmd": "06 02 vv ww pp pp tt tt tt tt",
        "type": "setWithValues",
        "tip": "Muove la telecamera in una posizione assoluta specifica con velocità pan/tilt",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17],
            "pan_position": ["0000", "FFFF"],
            "tilt_position": ["0000", "FFFF"]
        },
        "inquire": "06 12",
        "reply_format": "vv ww pp pp tt tt tt tt",
        "placeholder": ["vv", "ww", "pp", "tt"],
        "state": "_panTiltAbsolutePosition"
    },
    "pan_tilt_relative_position": {
        "cmd": "06 03 vv ww pp pp tt tt tt tt",
        "type": "setWithValues",
        "tip": "Muove la telecamera in una posizione relativa specifica con velocità pan/tilt",
        "allowed_values": {
            "pan_speed": [1, 18],
            "tilt_speed": [1, 17],
            "pan_position": ["0000", "FFFF"],
            "tilt_position": ["0000", "FFFF"]
        },
        "inquire": None,
        "reply_format": "vv ww pp pp tt tt tt tt",
        "placeholder": ["vv", "ww", "pp", "tt"],
        "state": "_panTiltRelativePosition"
    },
    "pan_tilt_home": {
        "cmd": "06 04",
        "type": "setNoValue",
        "tip": "Riporta la telecamera alla posizione Home",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_panTiltHome"
    },
    "pan_tilt_reset": {
        "cmd": "06 05",
        "type": "setNoValue",
        "tip": "Resetta la posizione pan/tilt",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_panTiltReset"
    },
    "pan_tilt_ramp_curve": {
        "cmd": "06 31 pp",
        "type": "setWithValue",
        "tip": "Imposta il ramp curve (Sharpness)",
        "allowed_values": [1],
        "inquire": "06 31",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_panTiltRampCurve"
    },
    "pan_tilt_slow": {
        "cmd": "06 44 pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita la modalità Pan-Tilt Slow",
        "allowed_values": [2, 3],
        "inquire": "06 44",
        "reply_format": "pp",
        "placeholder": ["p"],
        "state": "_panTiltSlow"
    },
    "pan_tilt_limit_set": {
        "cmd": "06 07 00 qq pp pp pp pp tt tt tt tt",
        "type": "setWithValues",
        "tip": "Imposta il limite di Pan-Tilt",
        "allowed_values": {
            "position": [1, 0]
        },
        "inquire": "06 07",
        "reply_format": "qq pp pp pp pp tt tt tt tt",
        "placeholder": ["qq", "pp", "tt"],
        "state": "_panTiltLimitSet"
    },
    "pan_tilt_limit_clear": {
        "cmd": "06 07 pp 07 0f 07 0f 0f 0f 0f",
        "type": "setWithValue",
        "tip": "Rimuove il limite di Pan-Tilt",
        "allowed_values": [0, 1],
        "inquire": "06 07",
        "reply_format": "pp 07 0f 07 0f 0f 0f 0f",
        "placeholder": ["pp"],
        "state": "_panTiltLimitClear"
    }
}

presetDictionary = {
    "preset_reset": {
        "cmd": "04 3F 00 pp",
        "type": "setWithValue",
        "tip": "Resetta un preset specificato",
        "allowed_values": [
            int(value, 16) for value in [
                "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F",
                "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F",
                "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F",
                "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F"
            ]
        ],
        "inquire": "04 3F FF",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetReset"
    },
    "preset_set": {
        "cmd": "04 3F 01 pp",
        "type": "setWithValue",
        "tip": "Salva un preset con il numero specificato",
        "allowed_values": [
            int(value, 16) for value in [
                "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F",
                "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F",
                "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F",
                "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F"
            ]
        ],
        "inquire": "04 3F FF",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetSet"
    },
    "preset_recall": {
        "cmd": "04 3F 02 pp",
        "type": "setWithValue",
        "tip": "Richiama un preset specificato",
        "allowed_values": [
            int(value, 16) for value in [
                "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F",
                "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F",
                "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F",
                "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F"
            ]
        ],
        "inquire": "04 3F FF",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetRecall"
    },
    "preset_speed_select": {
        "cmd": "7E 04 1B pp",
        "type": "setWithValue",
        "tip": "Seleziona la modalità di velocità per i preset",
        "allowed_values": [0, 1, 2],
        "inquire": "7E 04 1B",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetSpeedSelect"
    },
    "preset_speed_separate": {
        "cmd": "7E 01 0B pp qq",
        "type": "setWithValues",
        "tip": "Imposta la velocità separata per un preset",
        "allowed_values": {
            "preset_number": list(range(0, 64)),
            "position_speed": list(range(1, 20))
        },
        "inquire": "7E 01 0B",
        "reply_format": "pp qq",
        "placeholder": ["pp", "qq"],
        "state": "_presetSpeedSeparate"
    },
    "preset_speed_common": {
        "cmd": "7E 04 1C pp",
        "type": "setWithValue",
        "tip": "Imposta la velocità comune per tutti i preset",
        "allowed_values": list(range(1, 20)),
        "inquire": "7E 04 1C",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetSpeedCommon"
    },
    "preset_mode": {
        "cmd": "7E 04 3D pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità preset",
        "allowed_values": [0, 1],
        "inquire": "7E 04 3D",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetMode"
    },
    "preset_call_mode": {
        "cmd": "7E 04 3B pp",
        "type": "setWithValue",
        "tip": "Imposta il modo di richiamo del preset (Freeze o Normal)",
        "allowed_values": [2, 3],
        "inquire": "7E 04 3B",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_presetCallMode"
    }
}

systemDictionary = {
    "system_ir_receive": {
        "cmd": "06 08 pp",
        "type": "setWithValue",
        "tip": "Abilita o disabilita l'IR Receive",
        "allowed_values": [2, 3, 10],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_irReceive"
    },
    "system_h_phase_up": {
        "cmd": "7E 01 3E 00 02",
        "type": "setNoValue",
        "tip": "Aumenta la fase orizzontale",
        "allowed_values": list(range(0, 960)),
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_hPhase"
    },
    "system_h_phase_down": {
        "cmd": "7E 01 3E 00 03",
        "type": "setNoValue",
        "tip": "Diminuisce la fase orizzontale",
        "allowed_values": list(range(0, 960)),
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_hPhase"
    },
    "system_h_phase_value": {
        "cmd": "7E 01 5B 00 pp pp pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente la fase orizzontale",
        "allowed_values": list(range(0, 960)),
        "inquire": "7E 01 5B",
        "reply_format": "pp pp pp",
        "placeholder": ["pp"],
        "state": "_hPhase"
    },
    "system_img_flip": {
        "cmd": "04 66 pp",
        "type": "setWithValue",
        "tip": "Attiva o disattiva il flip dell'immagine",
        "allowed_values": [2, 3],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_imgFlip"
    },
    "system_camera_id": {
        "cmd": "04 22 pp pp",
        "type": "setWithValue",
        "tip": "Imposta l'ID della camera",
        "allowed_values": ["0000", "FFFF"],
        "inquire": "04 22",
        "reply_format": "pp pp",
        "placeholder": ["pp"],
        "state": "_cameraId"
    },
    "menu_mode": {
        "cmd": "06 06 pp",
        "type": "setWithValue",
        "tip": "Attiva o disattiva il menu OSD",
        "allowed_values": [2, 3],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_menuMode"
    },
    "menu_enter": {
        "cmd": "7E 01 02 00 01",
        "type": "setNoValue",
        "tip": "Invio nel menu OSD",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_menuEnter"
    },
    "ir_cut_filter": {
        "cmd": "04 01 pp",
        "type": "setWithValue",
        "tip": "Imposta il filtro IR",
        "allowed_values": [2, 3],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_irCutFilter"
    },
    "tally_mode": {
        "cmd": "7E 01 0A 00 pp",
        "type": "setWithValue",
        "tip": "Attiva o disattiva la spia TALLY",
        "allowed_values": [2, 3],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_tallyMode"
    },
    "tally_level": {
        "cmd": "7E 01 0A 01 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello della spia TALLY",
        "allowed_values": [0, 4, 5],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_tallyLevel"
    },
    "hdmi_color_space": {
        "cmd": "7E 01 03 00 pp",
        "type": "setWithValue",
        "tip": "Imposta lo spazio colore HDMI",
        "allowed_values": [0, 1],
        "inquire": None,
        "reply_format": None,
        "placeholder": ["pp"],
        "state": "_hdmiColorSpace"
    },
    "power_on_standby": {
        "cmd": "04 00 pp",
        "type": "setWithValue",
        "tip": "Accende o mette in standby il dispositivo",
        "allowed_values": [2, 3],
        "inquire": "04 00",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_powerState"
    },
    "system_camera_generation": {
        "cmd": "7E 04 30",
        "type": "inquire",
        "tip": "Interroga la generazione della camera",
        "reply_format": "y0 50 0h 0k 0m 0n 0p 0q 0r 0s 0t 0u uu 0v vv FF",
        "allowed_values": [],
        "inquire": None,
        "placeholder": ["p"],
        "state": "_cameraGeneration"
    },
    "software_version_inquire": {
        "cmd": "00 02",
        "type": "inquire",
        "tip": "Interroga la versione software del dispositivo",
        "reply_format": "y0 50 pp pp qq qq rr rr 0s FF",
        "allowed_values": [],
        "inquire": None,
        "placeholder": [],
        "state": "_softwareVersion"
    }
}

customDictionary = {
    "DynamicHotPixelCorrection": {
        "cmd": "04 56 pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita la correzione dei pixel bruciati",
        "allowed_values": list(range(0,6)),
        "inquire": "04 5D",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_DynamicHotPixelCorrection"
    },
    "CameraAperture_reset": {
        "cmd": "04 02 00",
        "type": "setNoValue",
        "tip": "Resetta l'apertura della camera",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_CameraAperture_reset"
    },
    "CameraAperture_Up": {
        "cmd": "04 02 02",
        "type": "setNoValue",
        "tip": "Apre l'apertura della camera",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_CameraAperture_Up"
    },
    "CameraAperture_Down": {
        "cmd": "04 02 03",
        "type": "setNoValue",
        "tip": "Chiude l'apertura della camera",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_CameraAperture_Down"
    },
    "CameraAperture_Value": {
        "cmd": "04 42 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta direttamente i parametri della nitidezza",
        "allowed_values": list(range(0, 256)),
        "inquire": "04 02",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_CameraAperture_Value"
    },
    "CAM_SettingReset": {
        "cmd": "04 A0 10",
        "type": "setNoValue",
        "tip": "Resetta le impostazioni di fabbrica della camera",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_setting_reset"
    },
    "CameraBrightness_value": {
        "cmd": "04 A1 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello di luminosità",
        "allowed_values": list(range(0, 11)),
        "inquire": "04 A1",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_brightness"
    },
    "CameraContrast_value": {
        "cmd": "04 A2 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello di contrasto",
        "allowed_values": list(range(0, 11)),
        "inquire": "04 A2",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_contrast"
    },
    "CameraFlip": {
        "cmd": "04 A4 pp",
        "type": "setWithValue",
        "tip": "Imposta la modalità di Flip video",
        "allowed_values": list(range(0, 3)),
        "inquire":"04 A4",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_flip"
    },
    "CAM_Autoflip": {
        "cmd": "02 70 pp",
        "type": "setWithValue",
        "tip": "Abilita/disabilita l'autoflip",
        "allowed_values": [2,3],
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_autoflip"
    },
    "CAM_SettingSave": {
        "cmd": "04 A5 10",
        "type": "setNoValue",
        "tip": "Salva le impostazioni correnti",
        "allowed_values": [],
        "inquire": None,
        "reply_format": None,
        "placeholder": [],
        "state": "_setting_save"
    },
    "CameraIridix_value": {
        "cmd": "04 A7 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta il livello di Iridix",
        "allowed_values": list(range(0, 256)),
        "inquire": "04 A7",
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_iridix"
    },
    "CAM_AWBSensitivity": {
        "cmd": "04 A9 pp",
        "type": "setWithValue",
        "tip": "Imposta la sensibilità del bilanciamento automatico del bianco (AWB)",
        "allowed_values": {"pp": {"02": "High", "01": "Normal", "00": "Low"}},
        "inquire": None,
        "reply_format": "pp",
        "placeholder": ["pp"],
        "state": "_awb_sensitivity"
    },
     "AutoFocusZone": {
            "cmd": "04 AA pp",
            "type": "setWithValue",
            "tip": "Imposta la zona di messa a fuoco frontale, posteriore, per riunioni, per il tracciamento educativo, per oggetti in movimento e centrale",
            "allowed_values": list(range(0, 5)),
            "state": "_af_zone",
            "inquire": "04 AA",
            "reply_format": "pp",
            "placeholder": ["pp"],
    },
    "ColorHue_value": {
        "cmd": "04 4F 00 00 pp",
        "type": "setWithValue",
        "tip": "Imposta la tonalità colore",
        "allowed_values": list(range(-14, 15)),  # Da -14 a +14 gradi
        "placeholder": ["pp"],
        "state": "_color_hue"
    },
    "PanTilt_MaxSpeed": {
        "cmd": "0A 31 pp",
        "type": "setWithValue",
        "tip": "Abilita la velocità massima del pan/tilt 2 è OFF 3 è ON",
        "allowed_values": [2, 3],
        "placeholder": ["pp"],
        "state": "_pan_tilt_max_speed",
        "inquire": "0A 31",
    },
    "ARM_MCU_Version": {
        "cmd": "09 01 03",
        "type": "setNoValue",
        "tip": "Richiede la versione dell'ARM/MCU",
        "reply_format": "HEX",
        "state": "_arm_mcu_version"
    },
    "CAM_UVC_Version": {
        "cmd": "09 00 02",
        "type": "setNoValue",
        "tip": "Richiede la versione CAM/UVC",
        "reply_format": "HEX",
        "state": "_cam_uvc_version"
    },

    "PresetSpeed_Horizontal": {
        "cmd": "01 03 01 qq",
        "type": "setWithValue",
        "tip": "Imposta la velocità orizzontale (pan) tra preset",
        "allowed_values": list(range(1, 26)),  # Da 1 a 25
        "inquire": "01 03 01",
        "reply_format": "qq",
        "placeholder": ["qq"],
        "state": "_preset_h_speed"
    },
    "PresetSpeed_Vertical": {
        "cmd": "01 03 02 qq",
        "type": "setWithValue",
        "tip": "Imposta la velocità verticale (tilt) tra preset",
        "allowed_values": list(range(1, 22)),  # Da 1 a 21
        "inquire": "01 03 02",
        "reply_format": "qq",
        "placeholder": ["qq"],
        "state": "_preset_v_speed"
    },
    "PresetSpeed_Zoom": {
        "cmd": "01 03 03 qq",
        "type": "setWithValue",
        "tip": "Imposta la velocità dello zoom tra preset",
        "allowed_values": list(range(1, 9)),  # Da 1 a 8
        "inquire": "01 03 03",
        "reply_format": "qq",
        "placeholder": ["qq"],
        "state": "_preset_z_speed"
    },

    "Blue_Tuning": {
        "cmd": "0A 13 pp",
        "type": "setWithValue",
        "tip": "Regola il livello del blu mantenendo l'AWB attivo",
        "allowed_values": list(range(-10, 11)),  # Da -10 a +10
        "placeholder": ["pp"],
        "state": "_blue_tuning"
    },
    "Red_Tuning": {
        "cmd": "0A 12 pp",
        "type": "setWithValue",
        "tip": "Regola il livello del rosso mantenendo l'AWB attivo",
        "allowed_values": list(range(-10, 11)),  # Da -10 a +10
        "placeholder": ["pp"],
        "state": "_red_tuning"
    },

}