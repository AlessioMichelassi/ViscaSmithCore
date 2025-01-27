class MessageUnpacker:
    """
    Classe helper per parsare i pacchetti VISCA over IP (formato base).

    Il formato tipico, semplificato, potrebbe essere:
    [byte0..1]   Tipo (es. 0x01 0x00)
    [byte2..3]   Lunghezza payload (2 byte, big-endian)
    [byte4..7]   Sequence number (4 byte, big-endian)
    [byte8..N]   Payload effettivo (cameraID + preambolo + contenuto)
                  ... eventuale terminator 0xFF ...
    """

    def __init__(self):
        pass  # se servono configurazioni iniziali, puoi aggiungerle

    @staticmethod
    def isAck(data: bytes) -> bool:
        """Verifica se il pacchetto è un ACK."""
        return data.startswith(b'\x02\xff')

    @staticmethod
    def isCompletion(data: bytes) -> bool:
        """Verifica se il pacchetto è un Completion."""
        return data.startswith(b'\x03\xff')

    @staticmethod
    def isError(data: bytes) -> bool:
        """Verifica se il pacchetto è un Error."""
        return data.startswith(b'\x04\xff')

    def unpack_message(self, data: bytes) -> dict:
        """
        Analizza il pacchetto 'data' e restituisce un dizionario con:
        - message_type: str (ad es. "ack", "completion", "error", "command", "handshake", "ifclear")
        - sequence_number: int
        - payload: bytes (il contenuto 'grezzo' del payload, se presente)
        - camera_id: int (se presente)
        - preamble: int (se presente)
        - command_payload: bytes (eventuale parte dopo cameraID+preambolo)
        - raw_data: bytes (il pacchetto originale)

        NB: Per handshake/IFClear, potresti usare controlli specifici,
        perché a volte hanno formati speciali diversi dal “classico” header.
        """
        result = {
            "message_type": None,
            "sequence_number": None,
            "payload": b"",
            "camera_id": None,
            "preamble": None,
            "command_payload": b"",
            "raw_data": data
        }

        # Controllo lunghezza minima
        if len(data) < 8:
            result["message_type"] = "invalid"
            return result

        header = data[:8]
        seq_bytes = header[4:8]
        seq_number = int.from_bytes(seq_bytes, 'big')
        payload = data[8:]  # TUTTA la parte rimanente dopo l'header
        result["sequence_number"] = seq_number
        print(f"header: {header.hex()} | payload: {payload.hex()} | seq: {seq_number}")
        # 1) Check handshake / ifclear (o altri messaggi speciali)
        #    confrontando direttamente l'intero 'data'
        if self.isAck(payload):
            print("ACK detected")
            result["message_type"] = "ack"
            return result
        elif self.isCompletion(payload):
            print("Completion detected")
            result["message_type"] = "completion"
            return result
        elif self.isError(payload):
            print("Error detected")
            result["message_type"] = "error"
            return result

        packet_type = data[0:2]  # 0x01 0x00 tipicamente
        length_bytes = data[2:4]
        seq_bytes = data[4:8]
        payload = data[8:]  # tutti i byte dopo i primi 8

        payload_length = int.from_bytes(length_bytes, 'big', signed=False)
        sequence_number = int.from_bytes(seq_bytes, 'big', signed=False)
        result["sequence_number"] = sequence_number

        # 3) Se il payload inizia con 0x50, assumiamo che sia una "inquire_reply"
        #    (oppure potresti controllare se "payload[0] == 0x50" e la lunghezza corrisponde)
        if payload.startswith(b'\x50'):
            # Esempio: se server manda: header... seqNumber..., 0x50 + [comando inquired] + [valore] + terminator
            # Se l’ultimo byte è 0xFF, toglilo
            print("Inquire reply detected")
            if payload.endswith(b'\xff'):
                core = payload[1:-1]  # tolgo 0x50 e 0xff
            else:
                core = payload[1:]
            print(f"Core: {core.hex()}")
            # A questo punto, 'core' potrebbe essere "04 39 03" per dire "exposureMode = 3"

            result["message_type"] = "inquire_reply"
            result["command_payload"] = core
            return result
            # 4) Altrimenti, è un "comando" classico.
        if len(payload) >= 2:
            camera_id = payload[0]
            preamble = payload[1]
            # Se c'è un 0xFF in coda, lo togli
            if payload.endswith(b'\xff'):
                command_payload = payload[2:-1]
            else:
                command_payload = payload[2:]

            result["camera_id"] = camera_id
            result["preamble"] = preamble
            result["command_payload"] = command_payload

            if preamble == 0x01:
                result["message_type"] = "command_set"
            elif preamble == 0x09:
                result["message_type"] = "command_inquire"
            else:
                result["message_type"] = "unknown_command"
        else:
            result["message_type"] = "invalid_payload"

        return result
