# model_config.py

import random
import sys
import os
from openai import OpenAI

# Ensure the 'server' directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "server"))

# Import your API keys
from key import OPENAI_API_KEY, CLOUDFLARE_API_KEY, CLOUDFLARE_ACCOUNT_ID

# -------------------------
# SET THIS TO SWITCH MODES
# -------------------------
mode = "cloudflare"  # Options: "local", "openai", "cloudflare"

# -------------------------
# API Clients Setup
# -------------------------

# Local LM Studio
local_client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Dummy key for local use
)

# OpenAI
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Cloudflare Workers AI
cloudflare_client = OpenAI(
    base_url=f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/v1",
    api_key=CLOUDFLARE_API_KEY
)

# -------------------------
# Model Names
# -------------------------

local_model = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"
cloudflare_model = "@hf/nousresearch/hermes-2-pro-mistral-7b"
openai_model = "gpt-4o"

local_embedding_model = "nomic-ai/nomic-embed-text-v1.5-GGUF"
cloudflare_embedding_model = "@cf/baai/bge-base-en-v1.5"
openai_embedding_model = "text-embedding-3-small"

# -------------------------
# Unified API Selector
# -------------------------

def api_mode(mode):
    if mode == "local":
        return local_client, local_model, local_embedding_model
    elif mode == "cloudflare":
        return cloudflare_client, cloudflare_model, cloudflare_embedding_model
    elif mode == "openai":
        return openai_client, openai_model, openai_embedding_model
    else:
        raise ValueError("Invalid mode. Use 'local', 'openai', or 'cloudflare'.")
