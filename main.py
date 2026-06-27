import os
import asyncio
import warnings

# Suppress experimental/deprecation warnings to ensure clean JSON stdout
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from agents.email_processor import get_email_processor_agent
from google.adk.runners import Runner

from google.adk.sessions import InMemorySessionService
from google.genai import types

# Load environment variables from the .env file in the current working directory
dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path=dotenv_path)

async def run_agent():
    # 1. Initialize the Email Processing Agent
    agent = get_email_processor_agent()
    
    # 2. Setup the runner and in-memory session service
    session_service = InMemorySessionService()
    
    # Await session creation to prevent SessionNotFoundError
    session = await session_service.create_session(
        app_name="FutureCATLeaf",
        user_id="user_console"
    )
    
    runner = Runner(
        app_name="FutureCATLeaf",
        agent=agent,
        session_service=session_service
    )
    
    # 3. Formulate the user instruction
    email_file_path = os.path.join("data", "incidents", "incident_lot_number.txt")
    user_prompt = f"Please read the email from the file '{email_file_path}' and extract the structured incident object as pure JSON."
    
    user_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_prompt)]
    )
    
    # 4. Execute the agent runner using the active session ID
    events = runner.run(
        user_id="user_console",
        session_id=session.id,
        new_message=user_message
    )
    
    # 5. Gather response content from events
    full_response = ""
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    full_response += part.text
                    
    # Clean and output the JSON result
    print(full_response.strip())

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Warning: GEMINI_API_KEY environment variable is not set.")
        print("Please configure it in a '.env' file or your system environment variables.")
        print("Example: GEMINI_API_KEY=AIzaSy...")
        return
        
    asyncio.run(run_agent())

if __name__ == "__main__":
    main()
