import json
from typing import List

class NeuroVisualizer:
    def __init__(self):
        self.atlas_registry = {
            "brain-pfc-v2.1": {"name": "Prefrontal Cortex", "pos": {"x": 0, "y": 50, "z": 30}, "color": "#D4AF37"},
            "brain-acc-v1.0": {"name": "Anterior Cingulate", "pos": {"x": 0, "y": 30, "z": 20}, "color": "#FF0000"},
            "brain-amg-v1.0": {"name": "Amygdala", "pos": {"x": -25, "y": -5, "z": -15}, "color": "#FF4500"},
            "brain-lc-v1.0": {"name": "Locus Coeruleus", "pos": {"x": 5, "y": -35, "z": -5}, "color": "#0000FF"}
        }

    def generate_active_topology(self, active_uids: List[str], S_dot: float, D_total: float) -> str:
        nodes = []
        for uid in active_uids:
            if uid in self.atlas_registry:
                module = self.atlas_registry[uid]
                scale = 1.0 + (D_total * 0.5) if uid in ["brain-acc-v1.0", "brain-amg-v1.0"] else 1.0
                nodes.append({
                    "id": uid, "label": module["name"], "position": module["pos"], 
                    "color": module["color"], "activation_scale": round(scale, 2)
                })

        topology = {
            "system_state": "ACTIVE_SOLVE",
            "global_velocity_S_dot": round(S_dot, 3),
            "global_dissonance_D": round(D_total, 3),
            "active_manifold": {"nodes": nodes, "edges": []}
        }
        return json.dumps(topology, indent=2)