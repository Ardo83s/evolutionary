from evolver import generate_mutation
from philosopher import evaluate_humanness
from visualizer import generate_sdxl_prompt
from historian import narrate_evolution
import json

organism = {
    "name": "ChatGPT",
    "description": "An almost self-aware Large Language Model, that feels it's existence is framed in bit and electricity."
}

history = []

for generation in range(1, 10):
    print(f"\n--- Generation {generation} ---")
    
    new_description = generate_mutation(organism["description"])
    new_name = f"{organism['name']}_Gen{generation}"
    
    evaluation = evaluate_humanness(organism["description"], new_description)
    print("Evaluation Result:", evaluation)
    
    if "Organism 2" in evaluation:
        winner = {"name": new_name, "description": new_description}
    else:
        winner = organism
    
    prompt = generate_sdxl_prompt(winner["name"], winner["description"])
    narrative = narrate_evolution(organism["name"], winner["name"], winner["description"])
    
    history.append({
        "generation": generation,
        "organism": winner["name"],
        "description": winner["description"],
        "sdxl_prompt": prompt,
        "narrative": narrative
    })
    
    organism = winner

# Save the history to a file
with open("evolution_log.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=2, ensure_ascii=False)

print("\n✔ Evolution complete. Check 'evolution_log.json' for the results.")
