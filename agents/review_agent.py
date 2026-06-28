import os
from google.adk.agents import Agent

def get_review_agent() -> Agent:
    """Configures and returns the Human Review Agent.

    The agent uses instructions from prompts/review_agent.md
    to update the approval field in the Incident Object.
    """
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(current_dir, "prompts", "review_agent.md")

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Review instructions not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        instruction = f.read()

    # Initialize the ADK Agent
    agent = Agent(
        name="review_agent",
        model="gemini-2.5-flash",
        instruction=instruction
    )

    return agent
