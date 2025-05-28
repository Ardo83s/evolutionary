# model_config.py

import random
from openai import OpenAI
from server.key import OPENAI_API_KEY, CLOUDFLARE_API_KEY, CLOUDFLARE_ACCOUNT_ID

# Choose mode: "local", "openai", "cloudflare"
mode = "cloudflare"

# API Clients
local_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
openai_client = OpenAI(api_key=OPENAI_API_KEY)
cloudflare_client = OpenAI(
    base_url=f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/v1",
    api_key=CLOUDFLARE_API_KEY
)

# Model Names
local_model = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"
cloudflare_model = "@hf/nousresearch/hermes-2-pro-mistral-7b"
openai_model = "gpt-4o"

def api_mode(mode):
    if mode == "local":
        return local_client, local_model, "nomic-ai/nomic-embed-text-v1.5-GGUF"
    elif mode == "cloudflare":
        return cloudflare_client, cloudflare_model, "@cf/baai/bge-base-en-v1.5"
    elif mode == "openai":
        return openai_client, openai_model, "text-embedding-3-small"
    else:
        raise ValueError("Invalid mode. Choose from 'local', 'openai', or 'cloudflare'.")
