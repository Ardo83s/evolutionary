import openai
client = openai.OpenAI(api_key="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")

def generate_mutation(parent_description):
    prompt = f"""
You are an AI entity that evolves synthetic lifeforms. Based on the following organism, generate a new one that mutates some traits toward being more human-like. Be creative, but keep a clear lineage.

Parent organism:
{parent_description}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
