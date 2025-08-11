import asyncio
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_tracing_disabled(True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(client=client, model="gemini-1.5-flash"),
    )
    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())
