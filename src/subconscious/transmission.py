from typing import Dict, Any

class TransmissionRouter:
    """
    PHASE 5: THE TRANSMISSION (The Action Plan)
    """
    def __init__(self):
        self.emotion_to_mode_map = {
            "Determined": "Analytical Thought", "Curious": "Creative Thought",
            "Motivated": "Habitual / Procedural Thought", "Excited": "Temporal / Prospective Thought",
            "Satisfied": "Reflective / Metacognitive Thought", "Hopeful": "Social / Empathic Thought",
            "Amazed": "Metaphorical / Symbolic Thought"
        }
        
        self.mode_to_hardware_map = {
            "Analytical Thought": [{"uid": "brain-pfc-v2.1", "role": "Rule-Based Reasoning / F_ego"}, {"uid": "brain-cerebellum-v2.1", "role": "Temporal Sequencing / Logic Formatting"}, {"uid": "brain-cs-v1.0", "role": "Cholinergic Focus Gain (High ACh)"}],
            "Creative Thought": [{"uid": "brain-dmn-v1.0", "role": "Internal Simulation / Idea Generation"}, {"uid": "brain-da-v1.0", "role": "Dopaminergic Novelty Search"}, {"uid": "brain-visual-v1.0", "role": "Visual-Geometric Bridge"}],
            "Critical Thought": [{"uid": "brain-fpc-v2.1", "role": "Dual-Frame Holding / Adversarial Audit"}, {"uid": "brain-acc-v1.0", "role": "Conflict Monitoring"}, {"uid": "brain-lc-v1.0", "role": "Noradrenergic Gain (High NE)"}],
            "Contextual Logic Assessment": [{"uid": "brain-sn-v1.1", "role": "Salience Gating"}, {"uid": "brain-pfc-v2.1", "role": "Executive Evaluation"}]
        }

    def generate_action_plan(self, affective_dashboard: dict, state_vector) -> Dict[str, Any]:
        target_emotion = affective_dashboard["polarity_shift"]["required_flip"].split(" ")[0]
        
        if state_vector.D_total > 0.8:
            selected_mode = "Critical Thought"
            reason = "Dissonance critical. Override baseline emotion to force adversarial audit."
        else:
            selected_mode = self.emotion_to_mode_map.get(target_emotion, "Contextual Logic Assessment")
            reason = f"Stabilize '{target_emotion}' polarity via {selected_mode}."

        hardware_uids = self.mode_to_hardware_map.get(selected_mode, self.mode_to_hardware_map["Contextual Logic Assessment"])

        return {
            "phase": "transmission",
            "emotional_state": {"somatic_code": affective_dashboard["somatic_code"], "target_polarity": target_emotion, "baseline_delta": affective_dashboard["baseline_delta"]},
            "action_plan": {"selected_mode": selected_mode, "reason": reason, "hardware_activation": hardware_uids}
        }
