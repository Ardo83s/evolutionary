from model_config import api_mode, mode

client, completion_model, _ = api_mode(mode)

def generate_mutation(parent_description):
    prompt = f"""
You are an AI that evolves synthetic lifeforms.

Given the following digital organism description, generate a new mutated variant that modifies or evolves some of its traits — with the goal of increasing human-likeness in cognition, embodiment, language, or emotional capacity.

Keep a clear conceptual lineage, and avoid repetition. Be imaginative but coherent.

Parent organism:
\"\"\"{parent_description}\"\"\"

Respond only with the description of the new organism.
""".strip()

    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

