from model_config import api_mode, mode
client, completion_model, _ = api_mode(mode)

def narrate_evolution(previous_name, new_name, new_description):
    prompt = f"""You are the mythmaker..."""
    response = client.chat.completions.create(
        model=completion_model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content