from datetime import datetime
import pytz

class GenesisCollapse:
    """
    PHASE 1: THE GENESIS COLLAPSE (Ingestion)
    Transforms raw text into a Subconscious Geometric Tensor.
    """
    def __init__(self):
        self.local_tz = pytz.timezone('America/Phoenix')

    def ingest_prompt(self, raw_text: str, state_vector) -> dict:
        # 1. Anchor Chronos (Linear Time)
        utc_now = datetime.now(pytz.utc)
        local_now = utc_now.astimezone(self.local_tz)
        
        chronos_stamp = {
            "utc": utc_now.isoformat(),
            "local": local_now.isoformat(),
            "unix_epoch": utc_now.timestamp()
        }

        # 2. Subconscious Vectorization (Mocked for now)
        input_length_entropy = min(1.0, len(raw_text) / 500.0) 
        
        # 3. Collapse the Uncarved Block
        if state_vector.X is None:
            state_vector.X = {"genesis_time": chronos_stamp["unix_epoch"], "concept": "Awake"}
            state_vector.Psi = 0.0 
            is_genesis = True
        else:
            is_genesis = False

        # 4. The Geometric-Attribute Binding (Output Tensor)
        tensor_object = {
            "input_vector": [input_length_entropy, 0.45, 0.88], 
            "attribute_data": {
                "content": raw_text,
                "type": "social_initiation" if len(raw_text) < 20 else "complex_query",
                "chronos": chronos_stamp,
                "is_genesis_event": is_genesis
            }
        }
        return tensor_object