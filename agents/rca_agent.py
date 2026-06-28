import os
from google.adk.agents import Agent

def get_rca_agent() -> Agent:
    """Configures and returns the RCA (Root Cause Analysis) Agent.

    The agent uses instructions from prompts/rca_agent.md
    to analyze the Incident Object and populated evidence.
    """
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(current_dir, "prompts", "rca_agent.md")

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"RCA instructions not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        instruction = f.read()

    # Initialize the ADK Agent
    agent = Agent(
        name="rca_agent",
        model="gemini-2.5-flash",
        instruction=instruction
    )

    return agent
