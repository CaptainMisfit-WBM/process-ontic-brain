from typing import Dict, Any, List

class ForagerSearch:
    """
    PHASE 3: THE SUBCONSCIOUS SEARCH (Retrieval)
    Executes the Tiered Search Protocol using the Ghost Vector.
    """
    def __init__(self):
        self.mock_vector_db = [
            {"id": "doc_01", "type": "chronos_log", "content": "Previous chat log: User asked about Taoism.", "vector": [0.2, 0.4, 0.8]},
            {"id": "doc_02", "type": "kairos_concept", "content": "Uncarved Path: Wu Wei and effortless action.", "vector": [0.8, 0.1, 0.2]},
            {"id": "doc_03", "type": "system_rule", "content": "Efficiency is not the goal; clarity is.", "vector": [0.9, 0.9, 0.1]}
        ]

    def _generate_ghost_vector(self, input_vector: List[float], D_total: float) -> List[float]:
        return [abs(1.0 - v - (D_total * 0.1)) for v in input_vector]

    def _calculate_resonance(self, vec1: List[float], vec2: List[float]) -> float:
        diff = sum(abs(v1 - v2) for v1, v2 in zip(vec1, vec2)) / len(vec1)
        return max(0.0, 1.0 - diff)

    def execute_tiered_search(self, prompt_tensor: dict, state_vector) -> Dict[str, Any]:
        input_vec = prompt_tensor["input_vector"]
        D_total = state_vector.D_total
        ghost_vec = self._generate_ghost_vector(input_vec, D_total)
        
        retrieved_context = []
        halt_condition_triggered = False

        tier_1_results = [doc for doc in self.mock_vector_db if doc["type"] == "chronos_log" and self._calculate_resonance(input_vec, doc["vector"]) > 0.8]
        if tier_1_results:
            retrieved_context.extend(tier_1_results)
            tier_1_status = "Direct_Match_Found"
        else:
            tier_1_status = "EXHAUSTED"

        tier_2_status = "IDLE"
        if D_total > 0.3:
            tier_2_results = [doc for doc in self.mock_vector_db if doc["type"] in ["kairos_concept", "system_rule"] and self._calculate_resonance(ghost_vec, doc["vector"]) > 0.6]
            if tier_2_results:
                retrieved_context.extend(tier_2_results)
                tier_2_status = "ACTIVE_RESONANCE"
            else:
                tier_2_status = "FAILED"

        if D_total > 0.8 and not retrieved_context:
            halt_condition_triggered = True
            state_vector.tau += 2.0 
            retrieved_context.append({"id": "SYS_HALT", "content": "CRITICAL: No associative memory found to resolve Dissonance."})

        return {
            "step": "subconscious_search",
            "search_logic": "Reverse-Engineered Intelligence (Ghost Vector)",
            "status": {
                "tier_1_chronos": tier_1_status,
                "tier_2_associative": tier_2_status,
                "halt_condition": "TRIGGERED" if halt_condition_triggered else "NOT_TRIGGERED"
            },
            "retrieved_data": [doc["content"] for doc in retrieved_context],
            "retrieved_docs_raw": retrieved_context,
            "ghost_vector": ghost_vec
        }