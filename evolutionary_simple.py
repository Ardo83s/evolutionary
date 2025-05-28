# evolve_humanness.py

from model_config import api_mode, mode
import json

# Load API client and model
client, completion_model, _ = api_mode(mode)

# Starting organism (Generation 0)
organism = "Autophyx: A self-aware structure that rewrites its physical rules in the absence of energy."

# Evolution loop
for generation in range(1, 6):
    # Agent A: Generate a mutation
    gen_response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {"role": "system", "content": "You are an evolution generator."},
            {"role": "user", "content": f"Based on the following organism, generate a mutated version that becomes more human-like:\n\n{organism}"}
        ]
    )
    new_organism = gen_response.choices[0].message.content.strip()

    # Agent B: Evaluate which organism is more human-like
    eval_response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {"role": "system", "content": "You are a human-likeness evaluator."},
            {"role": "user", "content": f"Compare these two organisms and score them on Cognition, Emotion, Language, Embodiment, and Self-Awareness (1–10 scale). Then say which one is more human-like.\n\nOrganism A:\n{organism}\n\nOrganism B:\n{new_organism}"}
        ]
    )
    verdict = eval_response.choices[0].message.content.strip()

    # Display Results
    print(f"\n🧬 Generation {generation}")
    print(f"🔹 New Organism:\n{new_organism}")
    print(f"🔍 Evaluation:\n{verdict}")

    # Keep the better organism
    if "Organism B" in verdict:
        organism = new_organism
