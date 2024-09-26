# vllm_query_app.py

import os
import requests
import json

# Configuration
VLLM_API_BASE = "https://vllm.bluelobster.ai/v1"
API_KEY = "token-abc123"

# Template for the system message
SYSTEM_TEMPLATE = """You are a helpful AI assistant. Respond to the user's query to the best of your ability."""

def send_query(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_TEMPLATE},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100
    }
    
    response = requests.post(f"{VLLM_API_BASE}/chat/completions", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

def main():
    print("vLLM Query Application")
    print("Type 'exit' to quit the application.")
    
    while True:
        user_input = input("\nEnter your query: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break
        
        response = send_query(user_input)
        print("\nAI Response:")
        print(response)

if __name__ == "__main__":
    main()