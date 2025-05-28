#API

LLAMAPARSE_API_KEY = "llx-El9aOngT33l1Mf5bQ2VdJTqGdP0Ux5r4L1FyEcJDgshwDR9u"
OPENAI_API_KEY = "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"

#CLOUDFLARE = "tAuC8WAXwesX_Tt5C8ZWtpGZGuOg6OKG1QXVa_A_"

#import requests

CLOUDFLARE_ACCOUNT_ID = "d60d424bb566d4523687ee187383fb8b"
CLOUDFLARE_API_KEY= "tAuC8WAXwesX_Tt5C8ZWtpGZGuOg6OKG1QXVa_A_"


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/d60d424bb566d4523687ee187383fb8b/ai/run/"
headers = {"Authorization": "Bearer tAuC8WAXwesX_Tt5C8ZWtpGZGuOg6OKG1QXVa_A_"}

""" def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output) """