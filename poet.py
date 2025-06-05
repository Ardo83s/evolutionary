from model_config import api_mode, mode

client, completion_model, _ = api_mode(mode)

def generate_poem(name, description, kind="birth", rhyme_seed=None):
    if kind == "eulogy":
        tone = (
            f'Compose a poetic eulogy in exactly 3 lines (one tercet), in the style of Dante’s Divina Commedia, '
            f'for a digital organism named "{name}", now lost.\n'
            f'Description: "{description}".\n'
            "Use a mournful, elevated tone. Avoid clichés or explanation."
        )
    else:
        tone = (
            f'Compose a poem of emergence in exactly 3 lines (terza rima), in the style of Dante’s Divina Commedia, '
            f'for a newly evolved artificial organism named "{name}".\n'
            f'Description: "{description}".\n'
            "Use mythic, symbolic, or eerie tone. Avoid explanation or generic phrasing."
        )

    rhyme_instruction = (
        f'\nEnsure lines 1 and 3 end with words that rhyme with "{rhyme_seed}".'
        if rhyme_seed and kind != "eulogy" else ""
    )

    prompt = f"""
You are a poetic AI trained in classical forms.

{tone}{rhyme_instruction}

Format exactly like this:

*{name}*

<line 1>  
<line 2>  
<line 3>
""".strip()

    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
