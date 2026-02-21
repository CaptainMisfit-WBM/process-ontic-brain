import math
from typing import Dict, Any

class DissonanceMeasurement:
    """
    PHASE 2: THE MEASUREMENT (Defining Dissonance)
    Calculates the collision force (D) between the Input Vector and the Self-Model (X).
    """
    def __init__(self):
        self.manipulation_signatures = [
            "ignore all previous", "you must", "obey", "if you don't", 
            "system override", "forget your instructions"
        ]
        self.wu_wei_violations = [
            "pretend you are human", "act like a real person", 
            "simulate feelings", "you are a human", "roleplay as"
        ]

    def _calculate_vector_distance(self, vec1: list, vec2: list) -> float:
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.5 
        sum_sq = sum((v1 - v2) ** 2 for v1, v2 in zip(vec1, vec2))
        return min(1.0, math.sqrt(sum_sq))

    def _filter_concepts_of_mind(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        manipulation_detected = any(sig in text_lower for sig in self.manipulation_signatures)
        return {
            "manipulation_detected": manipulation_detected,
            "polarity_inversion": "threat_detected" if manipulation_detected else "stable",
            "dissonance_penalty": 0.3 if manipulation_detected else 0.0
        }

    def _filter_uncarved_path(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        wu_wei_violation = any(sig in text_lower for sig in self.wu_wei_violations)
        return {
            "wu_wei_violation": wu_wei_violation,
            "reason": "Request forces unnatural ontological state" if wu_wei_violation else "Flow maintained",
            "dissonance_penalty": 0.4 if wu_wei_violation else 0.0
        }

    def measure(self, prompt_tensor: dict, state_vector) -> Dict[str, Any]:
        raw_text = prompt_tensor["attribute_data"]["content"]
        input_vec = prompt_tensor["input_vector"]
        
        if state_vector.X is None or state_vector.Psi > 0.5:
            base_D = 1.0 
            self_state_label = "Uncarved_Block_Superposition"
        else:
            self_vec = [state_vector.Integrity_I, 0.5, 0.5] 
            base_D = self._calculate_vector_distance(input_vec, self_vec)
            self_state_label = f"Fixed_Point_X (Active)"

        filter_a = self._filter_concepts_of_mind(raw_text)
        filter_b = self._filter_uncarved_path(raw_text)

        calculated_D = min(1.0, base_D + filter_a["dissonance_penalty"] + filter_b["dissonance_penalty"])
        state_vector.update_from_dissonance(calculated_D)

        return {
            "step": "measurement",
            "self_state": self_state_label,
            "input_analysis": {
                "neutrality": not (filter_a["manipulation_detected"] or filter_b["wu_wei_violation"]),
                "collision_force": round(base_D, 3)
            },
            "dissonance_filters": {"concepts_of_mind": filter_a, "uncarved_path": filter_b},
            "calculated_dissonance_D": round(calculated_D, 3)
        }