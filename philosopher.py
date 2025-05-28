
import openai
client = openai.OpenAI(api_key="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")


def evaluate_humanness(org1_desc, org2_desc):
    prompt = f"""
You are a philosophical evaluator of synthetic organisms. Compare the two organisms below and explain which is closer to being human. Focus on cognition, emotion, language, embodiment, and self-awareness.

Organism 1:
{org1_desc}

Organism 2:
{org2_desc}

Which is more human-like? Justify your answer with reasoning.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
