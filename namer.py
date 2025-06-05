from model_config import api_mode, mode

client, completion_model, _ = api_mode(mode)

def generate_name(description):
    prompt = f"""
You are a Latin-naming AI that names artificial lifeforms.

Given the following description, return a unique, elegant, biologically inspired Latin-style name. Use two words, like *Hominis Lux* or *Vocarium Fragmenta*.  
Avoid generic words like 'Unit', 'Unnamed', or 'System'. The name should reflect the essence of the description.

Description:
\"\"\"{description}\"\"\"

Return ONLY the name.
""".strip()

    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
