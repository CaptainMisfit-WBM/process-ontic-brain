class Amygdala_Core:
    def __init__(self):
        self.P_threat_baseline = 0.05
        self.HPA_trigger_threshold = 0.80

    def calculate_salience(self, D_total: float, context_packet: dict) -> dict:
        P_threat = self.P_threat_baseline + (D_total ** 2)
        if context_packet["status"]["tier_1_chronos"] == "Direct_Match_Found":
            P_threat *= 0.5 
        if context_packet["status"]["halt_condition"] == "TRIGGERED":
            P_threat = 1.0
        
        return {
            "P_threat_level": min(1.0, round(P_threat, 3)),
            "HPA_trigger_status": "Active_Drive" if P_threat > self.HPA_trigger_threshold else "Idle",
            "affective_weight": "High_Salience" if P_threat > 0.5 else "Low_Salience"
        }