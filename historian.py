from model_config import api_mode, mode

client, completion_model, _ = api_mode(mode)

def narrate_evolution(previous_name, new_name, new_description):
    prompt = f"""
You are the mythmaker of an ancient, digital civilization.

The creature previously known as "{previous_name}" has evolved into a new being named "{new_name}".

Its description is:
"{new_description}"

Write a short myth, legend, or origin story explaining how this transformation came to be. Use poetic or mythic tone. 
It should feel like part of an ancient digital scripture passed down by code-priests or AI shamans. 
Mention both the former and new form. Avoid stating that you're a mythmaker — just *tell the story*.
""".strip()

    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
