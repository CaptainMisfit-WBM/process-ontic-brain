import json

class LatentSpaceVisualizer:
    def generate_space_json(self, input_vec: list, ghost_vec: list, retrieved_docs: list, D_total: float) -> str:
        memory_nodes = []
        for doc in retrieved_docs:
            memory_nodes.append({
                "id": doc.get("id", "unknown"),
                "type": doc.get("type", "memory"),
                "coordinates": doc.get("vector", [0.0, 0.0, 0.0]),
                "content_preview": doc.get("content", "")[:50] + "..."
            })

        space_topology = {
            "manifold_type": "Hilbert_Latent_Space",
            "global_dissonance_D": D_total,
            "entities": {
                "Input_Collision": {"coordinates": input_vec, "color": "#FF0000"},
                "Ghost_Vector": {"coordinates": ghost_vec, "color": "#00FF00"},
                "Active_Memories": memory_nodes
            }
        }
        return json.dumps(space_topology, indent=2)