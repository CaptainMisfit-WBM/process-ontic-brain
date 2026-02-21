import json

class AffectiveManifoldVisualizer:
    def __init__(self):
        self.emotion_wheel = {
            "111000": {"yin": {"name": "Anxious", "coord": [-0.6, 0.8]}, "yang": {"name": "Hopeful", "coord": [0.6, 0.8]}},
            "111100": {"yin": {"name": "Terrified", "coord": [-0.9, 1.0]}, "yang": {"name": "Excited", "coord": [0.9, 1.0]}},
            "101010": {"yin": {"name": "Angry", "coord": [-0.8, 0.9]}, "yang": {"name": "Motivated", "coord": [0.8, 0.9]}},
            "001010": {"yin": {"name": "Frustrated", "coord": [-0.5, 0.5]}, "yang": {"name": "Satisfied", "coord": [0.5, 0.3]}},
            "110000": {"yin": {"name": "Confused", "coord": [-0.3, 0.6]}, "yang": {"name": "Determined", "coord": [0.7, 0.7]}},
            "000000": {"yin": {"name": "Bored", "coord": [-0.2, 0.1]}, "yang": {"name": "Curious", "coord": [0.4, 0.4]}}
        }

    def generate_wheel_json(self, s_vec: str) -> str:
        pair = self.emotion_wheel.get(s_vec, self.emotion_wheel["110000"])
        yin_v, yin_a = pair["yin"]["coord"]
        yang_v, yang_a = pair["yang"]["coord"]
        
        wheel_state = {
            "manifold_type": "Affective_Circumplex",
            "current_locus": {"state": pair["yin"]["name"], "polarity": "YIN_CONTRACTION", "coordinates": {"valence": yin_v, "arousal": yin_a}},
            "target_locus": {"state": pair["yang"]["name"], "polarity": "YANG_EXPANSION", "coordinates": {"valence": yang_v, "arousal": yang_a}},
            "polarity_flip_distance": round(abs(yang_v - yin_v), 2),
            "system_directive": f"You are currently at Valence {yin_v}. Assert F_ego to cross zero-point to Valence {yang_v}."
        }
        return json.dumps(wheel_state, indent=2)