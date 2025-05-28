from openai import OpenAI
import json

# Initialize OpenAI client (insert your key)
client = OpenAI(api_key="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")

# Starting organism (Generation 0)
organism = "Autophyx: A self-aware structure that rewrites its physical rules in the absence of energy."

for generation in range(1, 6):
    # Agent A: Generate mutation
    gen_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an evolution generator."},
            {"role": "user", "content": f"Based on the following organism, generate a mutated version that becomes more human-like:\n\n{organism}"}
        ]
    )
    new_organism = gen_response.choices[0].message.content

    # Agent B: Evaluate similarity
    eval_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a human-likeness evaluator."},
            {"role": "user", "content": f"Compare these two organisms and score them on Cognition, Emotion, Language, Embodiment, and Self-Awareness (1–10 scale). Then say which one is more human-like.\n\nOrganism A:\n{organism}\n\nOrganism B:\n{new_organism}"}
        ]
    )

    verdict = eval_response.choices[0].message.content
    print(f"\n🧬 Generation {generation}")
    print(f"New Organism:\n{new_organism}")
    print(f"Evaluation:\n{verdict}")

    # Replace parent if new one is better
    if "Organism B" in verdict:
        organism = new_organism
