import os
from huggingface_hub import InferenceClient

# Use Qwen - it's currently very stable on the HF Inference API
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
token = os.getenv("HF_API_TOKEN")

if not token:
    print(" Error: HF_API_TOKEN not found. Check your environment variables.")
    exit()

client = InferenceClient(token=token)

print(f" Chatbot active (Model: {MODEL_ID})")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    try:
        # The 'chat.completions.create' call
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        print(f"\nBot: {response.choices[0].message.content}\n")
        
    except Exception as e:
        print(f"\n❌ Error with {MODEL_ID}: {e}")
        print("Tip: If it says 'not supported', the server might be down. Try again in a minute or change the MODEL_ID.\n")