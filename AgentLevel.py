import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# 🔑 Your Gemini API Key (from https://aistudio.google.com/app/apikey)
GEMINI_API_KEY = "AIzaSyBM5RYQmoeMuqWex2xCjmQP20ZSnvG6OIU"

set_tracing_disabled(disabled=True)

# Create OpenAI-compatible Gemini client
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

async def main():
    # Define your agent
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(
            model="gemini-1.5-flash",
            openai_client=client
        ),
    )

    # Run the agent
    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
