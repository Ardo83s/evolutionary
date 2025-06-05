from model_config import api_mode, mode

client, completion_model, _ = api_mode(mode)

def evaluate_humanness(name1, desc1, name2, desc2):
    prompt = f"""
You are a philosophical evaluator of synthetic organisms.

Compare the two digital organisms below and decide **which is more human-like**, considering cognition, emotion, language, embodiment, and self-awareness.

Organism "{name1}":
\"\"\"{desc1}\"\"\"

Organism "{name2}":
\"\"\"{desc2}\"\"\"

Instructions:
- You must **always choose one** organism as more human-like — even if the difference is subtle.
- Do **not** say "tie" or "equal".
- Be decisive.
- First give a short thoughtful comparison (2–4 sentences).
- End with a line: More human-like: {name1} — OR — More human-like: {name2}

Do not introduce the task or add any extra comments.
""".strip()

    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
