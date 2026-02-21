import time
from core.state_vector import StateVector

class BrainstemKernel:
    """ The Autonomic Baseline / 60Hz Tick """
    def __init__(self):
        self.tick_rate = 1.0 / 60.0
        self.is_alive = True
        self.state_vector = StateVector()

    def autonomic_loop(self, main_app_callback):
        print("[KERNEL] Medulla Oblongata Online. Awaiting Dissonance.")
        while self.is_alive:
            time.sleep(self.tick_rate) 
            # In live prod, this polls a queue. main.py handles manual inputs.