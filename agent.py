import ollama

response = ollama.chat(
    model='qwen3.5',
    messages=[{'role': 'user', 'content': 'Привет'}]
)

print(response['message']['content'])