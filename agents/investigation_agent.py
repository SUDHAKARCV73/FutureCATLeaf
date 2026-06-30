import os
from google.adk.agents import Agent
from tools.resource_tools import (
    search_application_logs,
    read_deployment_history,
    search_master_data,
    search_knowledge_base,
    search_functional_documentation
)

def get_investigation_agent() -> Agent:
    """Configures and returns the Investigation Agent.

    The agent uses instructions from prompts/investigation_agent.md
    and queries mock resources using the tools defined in resource_tools.py.
    """
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(current_dir, "prompts", "investigation_agent.md")

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Investigation instructions not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        instruction = f.read()

    # Initialize the ADK Agent
    agent = Agent(
        name="investigation_agent",
        model="gemini-2.5-flash",
        instruction=instruction,
        tools=[
            search_application_logs,
            read_deployment_history,
            search_master_data,
            search_knowledge_base,
            search_functional_documentation
        ]
    )

    return agent
