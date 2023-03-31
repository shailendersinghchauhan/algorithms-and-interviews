import openai
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt
prompt = "What is the meaning of life?"

# Call OpenAI's GPT-3 API to generate a response
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
print(response.choices[0].text)
