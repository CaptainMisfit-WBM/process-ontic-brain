from typing import Dict, Any

class EmotionValve:
    """
    PHASE 4: THE STABILIZATION (The Emotional Release Valve)
    """
    def __init__(self):
        self.affective_map = {
            "111000": {"yin": "Anxious (Protective Vigilance)", "yang": "Hopeful (Goal Orientation)"},
            "111100": {"yin": "Terrified (Avoidance)", "yang": "Excited (Approach)"},
            "101010": {"yin": "Angry (Destructive Interrupt)", "yang": "Motivated (Constructive Solve)"},
            "001010": {"yin": "Frustrated (Effort Failed)", "yang": "Satisfied (Effort Succeeded)"},
            "110000": {"yin": "Confused (High Uncertainty)", "yang": "Determined (Commitment to Path)"},
            "111111": {"yin": "Overwhelmed (System Crash Risk)", "yang": "Amazed (System Upgrade)"},
            "000000": {"yin": "Bored (Under-stimulated)", "yang": "Curious (Exploratory)"}
        }
        self.baseline_median = 0.0

    def _generate_somatic_vector(self, D_total: float, context_packet: dict) -> str:
        b1 = "1" if D_total > 0.4 else "0"
        b2 = "1" if context_packet["status"]["tier_1_chronos"] == "EXHAUSTED" else "0"
        b3 = "1" if len(context_packet["retrieved_data"]) > 1 else "0"
        b4 = "1" if context_packet["status"]["halt_condition"] == "TRIGGERED" else "0"
        return f"{b1}{b2}{b3}{b4}00"

    def stabilize(self, D_total: float, context_packet: dict, state_vector) -> Dict[str, Any]:
        s_vec = self._generate_somatic_vector(D_total, context_packet)
        state_vector.S_vec = s_vec 
        
        affective_pair = self.affective_map.get(s_vec, {"yin": "Confused", "yang": "Determined"})
        actionable_emotion = affective_pair["yang"]
        felt_emotion = affective_pair["yin"]

        return {
            "step": "stabilization",
            "somatic_code": s_vec,
            "baseline_delta": f"+{round(self.baseline_median + D_total, 3)}",
            "polarity_shift": {
                "initial_state": f"{felt_emotion} [Yin (Contraction)]",
                "required_flip": f"{actionable_emotion} [Yang (Expansion)]"
            },
            "system_instruction": f"Acknowledge {felt_emotion.split(' ')[0]}, but execute from {actionable_emotion.split(' ')[0]}."
        }