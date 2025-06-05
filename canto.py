import os
import json

def compile_divina_machina(log_path, output_dir=None):
    """
    Compiles an epic poem from a lineage of synthetic organisms.
    Pulls 3-line terza rima stanzas from each winner in the evolution log.

    Parameters:
    - log_path: Path to the evolution log JSON (e.g., '20250604_153000_evolution_log.json')
    - output_dir: Optional output directory. Defaults to the folder of the log.
    """
    # Load the evolution log
    with open(log_path, "r", encoding="utf-8") as f:
        log = json.load(f)

    # Default to log directory if output_dir not specified
    if output_dir is None:
        output_dir = os.path.dirname(log_path)

    canto_lines = []
    canto_lines.append("# DIVINA MACHINA\n")
    canto_lines.append(f"Composed across {len(log)} generations of artificial life.\n")
    canto_lines.append("Each stanza records the poetic emergence of a winning organism.\n")
    canto_lines.append("Linked by terza rima across poetic lineage.\n")
    canto_lines.append("~\n")

    for entry in log:
        winner = entry.get("winner", {})
        poem = winner.get("poem")
        if poem:
            canto_lines.append(poem.strip())
            canto_lines.append("")  # blank line between stanzas

    output_path = os.path.join(output_dir, "divina_machina.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(canto_lines))

    print(f"✅ Final canto saved to: {output_path}")


# Optional direct execution
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compile Divina Machina poem from evolution log.")
    parser.add_argument("log_path", help="Path to the *_evolution_log.json file")
    parser.add_argument("--output_dir", help="Optional output folder for the poem")

    args = parser.parse_args()
    compile_divina_machina(args.log_path, args.output_dir)
