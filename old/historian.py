import openai

client = openai.OpenAI(api_key="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")

def narrate_evolution(previous_name, new_name, new_description):
    prompt = f"""
You are the mythmaker of an evolving synthetic species. Write a poetic and mythic reflection on the transformation from {previous_name} to {new_name}. Include philosophical thoughts on its changing identity and humanity.

Description of the new form:
{new_description}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

