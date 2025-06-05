
'''def generate_sdxl_prompt(name, description):
    summary = description.split(".")[0].strip()
    if len(summary.split()) > 20:
        summary = " ".join(summary.split()[:20])
    return (
        f"{name}, synthetic lifeform, {summary}, anatomical diagram, scientific rendering, "
        f"monochrome, white background"
    )'''

""" def generate_sdxl_prompt(name, description):
    # Extract main sentence for context
    summary = description.split(".")[0].strip()

    # Basic trait detection
    key_features = []
    desc = description.lower()

    if "limb" in desc or "appendage" in desc or "bipedal" in desc:
        key_features.append("limb structure or joint anatomy")
    if "eye" in desc or "visual" in desc or "sight" in desc:
        key_features.append("ocular systems")
    if "vocal" in desc or "language" in desc or "communication" in desc:
        key_features.append("vocal emitter or language module")
    if "neural" in desc or "memory" in desc or "cognition" in desc:
        key_features.append("neural cortex or memory lattice")
    if "skin" in desc or "surface" in desc or "texture" in desc:
        key_features.append("dermal layers or surface mesh")
    if "energy" in desc or "metabolize" in desc:
        key_features.append("internal energy processing system")

    if not key_features:
        key_features.append("core anatomical structure")

    # Assemble the final visual prompt
    traits_text = ", ".join(key_features)
    prompt = (
        f"{name}, synthetic lifeform. Depict {traits_text}. "
        f"Scientific anatomical diagram, lateral view, monochrome, clean linework, labeled schematic."
    )
    return prompt """


from model_config import api_mode, mode

client, completion_model, _ = api_mode(mode)

def generate_sdxl_prompt(name, description):
    prompt = f"""
You are an AI assistant that generates concise visual prompts for synthetic organisms.

Create a **single, clear sentence** describing how to render an anatomical diagram of the organism named "{name}" based on this description:
\"\"\"{description}\"\"\"

The output should follow this style:
- Scientific anatomical diagram
- Lateral view
- Blueprint or monochrome
- Labeled parts
- Concise, not poetic or explanatory

Return only the visual prompt as one sentence.
""".strip()

    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip().split("\n")[0]


