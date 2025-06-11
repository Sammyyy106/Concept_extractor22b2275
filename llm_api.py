import json
import os

_simulated_data = {}

def load_simulated_llm(subject):
    global _simulated_data
    path = os.path.join("simulated_llm_outputs", f"{subject}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            _simulated_data = json.load(f)
    else:
        print(f"[WARNING] Simulated LLM output not found: {path}")
        _simulated_data = {}

def get_concepts_from_llm(question, q_no=None):
    if _simulated_data and str(q_no) in _simulated_data:
        return _simulated_data[str(q_no)]
    print(f"[LLM Prompt] Given the question: \"{question}\", identify the historical concept(s) it is based on.")
    return ["Sample Concept A", "Sample Concept B"]
