# model_config.py
import random
from openai import OpenAI
from server.keys import *

mode = "cloudflare"  # change this dynamically or via CLI/env

local_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
openai_client = OpenAI(api_key=OPENAI_API_KEY)
cloudflare_client = OpenAI(base_url=f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/v1", api_key=CLOUDFLARE_API_KEY)

local_embedding_model = "nomic-ai/nomic-embed-text-v1.5-GGUF"
cloudflare_embedding_model = "@cf/baai/bge-base-en-v1.5"
openai_embedding_model = "text-embedding-3-small"

gpt4o = [{"model": "gpt-4o", "api_key": OPENAI_API_KEY, "cache_seed": random.randint(0, 100000)}]
llama3 = [{"model": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF", "api_key": "any", "api_type": "openai", "base_url": "http://127.0.0.1:1234", "cache_seed": random.randint(0, 100000)}]
cloudflare_model = "@hf/nousresearch/hermes-2-pro-mistral-7b"

def api_mode(mode):
    if mode == "local":
        return local_client, llama3[0]['model'], local_embedding_model
    elif mode == "cloudflare":
        return cloudflare_client, cloudflare_model, cloudflare_embedding_model
    elif mode == "openai":
        return openai_client, gpt4o[0]['model'], openai_embedding_model
    else:
        raise ValueError("Invalid mode selected.")
