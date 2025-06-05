""" 
import os
from visualizer import generate_image_from_prompt

def generate_images_from_folder(folder_path):
    prompt_files = [f for f in os.listdir(folder_path) if f.endswith("_prompt.txt")]

    for prompt_file in prompt_files:
        prompt_path = os.path.join(folder_path, prompt_file)
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read().strip()

        name_base = prompt_file.replace("_prompt.txt", "")
        image_path = os.path.join(folder_path, f"{name_base}.png")

        print(f"🎨 Generating image for: {name_base}")
        generate_image_from_prompt(prompt, image_path)

    print("\n✅ All images generated.")

if __name__ == "__main__":
    folder = input("Enter evolution folder path (e.g. 20250604_153000_evolution): ").strip()
    generate_images_from_folder(folder) """
