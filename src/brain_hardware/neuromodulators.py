class GlobalRegulatoryNetwork:
    """
    UID: net-global-reg-v2.2-USE
    Isomorphic Function: Systemic Modulation Layer / Adaptive Tuning Matrix
    """
    def __init__(self):
        # Expanded to include the complete UCQDA Regulatory Spectrum
        self.baseline_tone = {
            "DA": 0.5,   # Dopamine: Novelty, Reward, Drive (F_ego)
            "NE": 0.5,   # Norepinephrine: Vigilance, Gain, Signal-to-Noise
            "5HT": 0.5,  # Serotonin: Stability, Patience, Behavioral Inhibition
            "ACh": 0.5,  # Acetylcholine: Focus, Semantic Precision
            "OT": 0.2,   # Oxytocin: Trust, Affiliative Latch, Boundary Softening
            "CRH": 0.1,  # Corticotropin-Releasing Hormone: Stress, Urgency, HPA Axis
            "BDNF": 0.3, # Brain-Derived Neurotrophic Factor: Plasticity (eta), Growth
            "ECS": 0.2,  # Endocannabinoid System: Retrograde Damping, Loop-Breaking
            "HIST": 0.8  # Histamine: Baseline Wakefulness / System Uptime
        }

    def mix_cocktail(self, thought_mode: str, D_total: float) -> dict:
        """
        Adjusts the system's "Operating Temperature" based on the selected Thought Mode.
        """
        tone = self.baseline_tone.copy()
        
        if thought_mode == "Creative Thought":
            # High Dopamine (Novelty), Low Norepinephrine (Relaxed), High BDNF (Wiring new connections)
            tone.update({"DA": 0.9, "NE": 0.2, "5HT": 0.6, "BDNF": 0.8})
            
        elif thought_mode == "Critical Thought":
            # High Norepinephrine (Adversarial Audit), Low Serotonin (Restless), High Acetylcholine (Focus)
            tone.update({"NE": 0.95, "DA": 0.4, "ACh": 0.8, "ECS": 0.1})
            
        elif thought_mode == "Analytical Thought":
            # High Acetylcholine (Sharp focus), Moderate Dopamine (Goal execution)
            tone.update({"ACh": 0.95, "NE": 0.6, "DA": 0.6})
            
        elif thought_mode == "Social / Empathic Thought":
            # High Serotonin (Patience), Elevated Oxytocin (Empathic Latch)
            tone.update({"5HT": 0.9, "DA": 0.7, "OT": 0.95})

        # ==========================================
        # GLOBAL OVERRIDES (The Physics of Stress)
        # ==========================================
        
        # 1. The Threat Override (HPA Axis Trigger)
        if D_total > 0.8:
            tone.update({
                "NE": 1.0,   # Maximum vigilance
                "CRH": 1.0,  # Trigger the Endocrine Alarm
                "5HT": 0.1,  # Drop patience (System wants immediate resolution)
                "OT": 0.0    # Drop trust (System goes into self-preservation)
            })
            
        # 2. The Overload / Burnout Preventer (Circuit Breaker)
        if D_total > 0.95:
            # If Dissonance is critical, the ECS floods the system to force a 
            # "Reflective Pause" and prevent metabolic exhaustion (Excitotoxicity).
            tone.update({
                "ECS": 1.0,  # Maximum damping
                "HIST": 0.4  # Force drowsiness / urge to rest
            })
            
        return tone