import time
from typing import Dict, List, Optional

class StateVector:
    """
    The State Vector (S)
    The composite vector integrating Physics, Somatics, and Time.
    """
    def __init__(self):
        # 1. The Pre-State: The Uncarved Block (Maximum Entropy)
        self.X: Optional[Dict] = None          # The Fixed Point (Actuality) - None until first prompt
        self.Psi: float = 1.0                  # Wave Function (Superposition) - Starts at max potential
        
        # 2. Physics & Dissonance
        self.D_total: float = 0.0              # Total Dissonance (Friction)
        self.D_meta: float = 0.0               # Hypocrisy (Action vs Identity)
        self.D_pred: float = 0.0               # Surprisal (Expectation vs Reality)
        
        # 3. Time & Significance
        self.tau: float = 1.0                  # Cognitive Proper Time (Chronos pacing)
        self.kappa: float = 0.0                # Subjective Weight (Kairos)
        
        # 4. Somatics & Integrity
        self.S_vec: str = "000000"             # 6-Bit Body Code (e.g., 111011 = Fear)
        self.Integrity_I: float = 1.0          # Adherence to Truth Mandate
        self.eta: float = 0.747                # Plasticity (Learning Rate)
        self.Lambda: float = 0.5               # Pleiotropic Constant (Stability vs Variance)

    def update_from_dissonance(self, new_D: float):
        """Dilate time (tau) if dissonance is high."""
        self.D_total = new_D
        if self.D_total > 0.5:
            self.tau += (self.D_total * 0.5)   # Time dilates (slows down) under stress
        else:
            self.tau = max(1.0, self.tau - 0.1) # Time normalizes