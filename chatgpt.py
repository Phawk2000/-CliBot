import openai

# Set up your OpenAI API credentials
openai.api_key = 'Api key here'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the ChatGPT model
        prompt=prompt,
        max_tokens=100,  # Adjust the max tokens as needed
        temperature=0.7,  # Adjust the temperature as needed
        n=1,  # Number of responses to generate
        stop=None,  # Optional stop sequence to end the response
    )

    # Extract and return the generated response
    if response.choices:
        return response.choices[0].text.strip()

    return ""  # Empty response if no choices are available

# Main loop
while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break

    # Call the chat_with_gpt function to get the AI response
    response = chat_with_gpt(user_input)

    print("ChatGPT: " + response)
