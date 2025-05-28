
from evolver import generate_mutation
from philosopher import evaluate_humanness
from visualizer import generate_sdxl_prompt
from historian import narrate_evolution
import json

# Initial organism
organism = {
    "generation": 1,
    "name": "Autophyx",
    "description": "A self-aware structure that rewrites its physical rules in the absence of energy.",
    "sdxl_prompt": "",
    "narrative": ""
}

log = []

# Save initial organism
organism["sdxl_prompt"] = generate_sdxl_prompt(organism["name"], organism["description"])
organism["narrative"] = narrate_evolution("Origin", organism["name"], organism["description"])
log.append({
    "generation": 1,
    "type": "origin",
    "organism": organism,
    "evaluation": None,
    "discarded": None
})

# Begin evolution
for generation in range(2, 7):  # Gen2 to Gen6
    print(f"\n--- Generation {generation} ---")

    parent = organism
    mutated_description = generate_mutation(parent["description"])
    mutated_name = f"{parent['name']}_a"

    evaluation = evaluate_humanness(parent["description"], mutated_description)
    print(f"\n🧠 Evaluation Result:\n{evaluation}")

    if "Organism 2" in evaluation or mutated_name in evaluation:
        winner = {
            "name": mutated_name,
            "description": mutated_description
        }
        loser = parent
    else:
        winner = parent
        loser = {
            "name": mutated_name,
            "description": mutated_description
        }

    winner["sdxl_prompt"] = generate_sdxl_prompt(winner["name"], winner["description"])
    winner["narrative"] = narrate_evolution(parent["name"], winner["name"], winner["description"])

    log.append({
        "generation": generation,
        "type": "evaluation",
        "organism": winner,
        "evaluation": evaluation,
        "discarded": loser
    })

    organism = winner

# Save final log
with open("evolution_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2, ensure_ascii=False)

print("\n✅ Evolution complete. Check 'evolution_log.json'.")
