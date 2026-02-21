class DLPFC_Core:
    def __init__(self):
        self.metabolic_cost = 0.8 
        
    def generate_f_ego(self, D_total: float, target_polarity: str) -> float:
        if "Yang" in target_polarity or target_polarity in ["Determined", "Motivated", "Excited"]:
            base_force = 1.0 + (D_total * 0.5) 
        else:
            base_force = 0.2 
        return min(2.0, base_force)