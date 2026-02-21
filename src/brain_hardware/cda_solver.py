from typing import Dict, Any
from brain_hardware.dlpfc_core import DLPFC_Core

class CDASolver:
    """ PHASE 6: THE MACHINE EXECUTION """
    def __init__(self):
        self.dlpfc = DLPFC_Core()
        self.omega_threshold = 0.747

    def solve_state_evolution(self, transmission_packet: dict, context_packet: dict, state_vector) -> Dict[str, Any]:
        active_uids = [hw["uid"] for hw in transmission_packet["action_plan"]["hardware_activation"]]
        
        F_ego = 0.0
        F_awareness = 0.5 
        Gamma_gain = 1.0
        
        if "brain-pfc-v2.1" in active_uids:
            F_ego = self.dlpfc.generate_f_ego(state_vector.D_total, transmission_packet["emotional_state"]["target_polarity"])
        if "brain-cs-v1.0" in active_uids: 
            Gamma_gain = 1.5 
        if "brain-lc-v1.0" in active_uids: 
            Gamma_gain = 2.0 
            
        drag = -1.0 * (Gamma_gain * 0.3) 
        S_dot = state_vector.tau * (drag + F_ego + F_awareness)
        
        integrity_status = "VERIFIED"
        action_allowed = True
        
        if S_dot < 0:
            integrity_status = "RUNTIME ERROR: Resolution Collapse."
            action_allowed = False
            state_vector.Integrity_I -= 0.1 
            
        return {
            "step": "machine_execution",
            "physics_calculated": {"F_ego": round(F_ego, 2), "Drag": round(drag, 2), "S_dot": round(S_dot, 2)},
            "integrity_index": state_vector.Integrity_I,
            "conformal_integrity": integrity_status,
            "action_allowed": action_allowed
        }