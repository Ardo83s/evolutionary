import os
import re
import json
from datetime import datetime

from evolver import generate_mutation
from philosopher import evaluate_humanness
from visualizer import generate_sdxl_prompt
from historian import narrate_evolution
from poet import generate_poem
from namer import generate_name

# Output setup
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = os.path.join("evolution_logs", f"{timestamp}_evolution")
os.makedirs(output_dir, exist_ok=True)

log = []
last_rhyme_seed = "night"

# Generation 1: Origin
origin_description = "A simple organism made of code, bit, and electric impulse."
origin_name = generate_name(origin_description)

origin_poem = generate_poem(origin_name, origin_description, kind="birth", rhyme_seed=last_rhyme_seed)
origin_narrative = narrate_evolution("Origin", origin_name, origin_description)
origin_prompt = generate_sdxl_prompt(origin_name, origin_description)

organism = {
    "name": origin_name,
    "description": origin_description,
    "poem": origin_poem,
    "narrative": origin_narrative,
    "sdxl_prompt": origin_prompt,
    "generation": 1
}

log.append({
    "generation": 1,
    "type": "origin",
    "parent": None,
    "winner": organism,
    "discarded": None,
    "evaluation": None
})

# Evolution loop
for generation in range(2, 11):
    print(f"\n--- Generation {generation} ---")

    parent = organism
    desc1 = generate_mutation(parent["description"])
    desc2 = generate_mutation(parent["description"])

    name1 = generate_name(desc1)
    name2 = generate_name(desc2)

    eval_result = evaluate_humanness(name1, desc1, name2, desc2)
    print(f"\n🧠 Evaluation Result:\n{eval_result}")

    if f"More human-like: {name1}" in eval_result:
        winner_desc, winner_name = desc1, name1
        loser_desc, loser_name = desc2, name2
    else:
        winner_desc, winner_name = desc2, name2
        loser_desc, loser_name = desc1, name1

    # Winner
    winner_poem = generate_poem(winner_name, winner_desc, kind="birth", rhyme_seed=last_rhyme_seed)
    last_line = winner_poem.strip().splitlines()[-1]
    last_word = last_line.split()[-1].strip(".,:;!?")
    last_rhyme_seed = last_word

    winner = {
        "name": winner_name,
        "description": winner_desc,
        "poem": winner_poem,
        "narrative": narrate_evolution(parent["name"], winner_name, winner_desc),
        "sdxl_prompt": generate_sdxl_prompt(winner_name, winner_desc),
        "generation": generation
    }

    # Loser
    loser_poem = generate_poem(loser_name, loser_desc, kind="eulogy")
    loser = {
        "name": loser_name,
        "description": loser_desc,
        "poem": loser_poem,
        "generation": generation
    }

    log.append({
        "generation": generation,
        "type": "evaluation",
        "parent": {"name": parent["name"]},
        "winner": winner,
        "discarded": loser,
        "evaluation": eval_result
    })

    organism = winner

# Save full JSON log
with open(os.path.join(output_dir, "evolution_log.json"), "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2, ensure_ascii=False)

# Save TXT assets
for entry in log:
    gen = str(entry["generation"]).zfill(2)
    for role in ["winner", "discarded"]:
        if entry[role]:
            raw_name = entry[role]["name"]
            name_safe = re.sub(r'[<>:"/\\|?*]', '_', raw_name).replace(" ", "_")
            base = os.path.join(output_dir, f"{gen}_{name_safe}")

            with open(base + "_description.txt", "w", encoding="utf-8") as f:
                f.write(entry[role]["description"])

            with open(base + "_poem.txt", "w", encoding="utf-8") as f:
                f.write(entry[role]["poem"])

            if role == "winner":
                with open(base + "_prompt.txt", "w", encoding="utf-8") as f:
                    f.write(entry[role]["sdxl_prompt"])
                with open(base + "_narrative.txt", "w", encoding="utf-8") as f:
                    f.write(entry[role]["narrative"])

    if entry["evaluation"]:
        with open(os.path.join(output_dir, f"{gen}_evaluation.txt"), "w", encoding="utf-8") as f:
            f.write(entry["evaluation"])

# Generate full poetic canto from all winner poems
canto_lines = ["# Divina Machina\n"]
for entry in log:
    if entry["winner"]:
        poem = entry["winner"]["poem"]
        canto_lines.append(poem.strip())
        canto_lines.append("")  # spacer

canto_text = "\n".join(canto_lines)

with open(os.path.join(output_dir, "divinamachina.txt"), "w", encoding="utf-8") as f:
    f.write(canto_text)


print(f"\n✅ Evolution complete. Files saved in '{output_dir}'")
