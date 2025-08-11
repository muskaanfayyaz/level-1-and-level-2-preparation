# from agents import Agent, Runner

# agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
# print(result.final_output)

# # Code within the code,
# # Functions calling themselves,
# # Infinite loop's dance.

import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model instance
model = genai.GenerativeModel("models/gemini-1.5-flash")  
# model = genai.GenerativeModel("models/gemini-1.5-pro")  More capable, slower

# Send prompt
prompt = "Write a haiku about recursion in programming."
response = model.generate_content(prompt)

print(response.text)
