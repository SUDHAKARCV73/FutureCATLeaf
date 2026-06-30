import os
from google.adk.agents import Agent

def get_report_generator_agent() -> Agent:
    """Configures and returns the Functional Investigation Report Generator Agent.

    The agent uses instructions from prompts/report_generator.md
    to format the Incident Object into a Markdown report.
    """
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(current_dir, "prompts", "report_generator.md")

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Report generator instructions not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        instruction = f.read()

    # Initialize the ADK Agent
    agent = Agent(
        name="report_generator",
        model="gemini-2.5-flash",
        instruction=instruction
    )

    return agent
