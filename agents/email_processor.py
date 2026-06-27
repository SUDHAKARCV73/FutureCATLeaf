import os
from google.adk.agents import Agent
from tools.file_tools import read_incident_email

def get_email_processor_agent() -> Agent:
    """Configures and returns the Email Processing Agent.

    The agent uses the system instructions from prompts/email_processor.md
    and can read email files using the read_incident_email tool.
    """
    # Resolve the path to prompts/email_processor.md
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(current_dir, "prompts", "email_processor.md")

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"System instructions not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        instruction = f.read()

    # Initialize the ADK Agent
    agent = Agent(
        name="email_processor",
        model="gemini-2.5-flash",
        instruction=instruction,
        tools=[read_incident_email]
    )

    return agent
