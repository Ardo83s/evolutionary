""" from diffusers import StableDiffusionXLPipeline
import torch

# Load once and reuse
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16"
).to("cuda")

def generate_image_from_prompt(prompt, output_path):
    image = pipe(prompt).images[0]
    image.save(output_path) """