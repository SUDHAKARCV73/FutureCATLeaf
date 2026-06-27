import os
import sys
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

async def run_agent(filename: str):
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
    
    # 3. Resolve the email file path (either direct path or relative to data/incidents/)
    if os.path.exists(filename):
        email_file_path = filename
    else:
        email_file_path = os.path.join("data", "incidents", filename)
        
    if not os.path.exists(email_file_path):
        print(f"Error: File '{filename}' not found directly or in 'data/incidents/'.")
        return

    # 4. Formulate the user instruction
    user_prompt = f"Please read the email from the file '{email_file_path}' and extract the structured incident object as pure JSON."
    
    user_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_prompt)]
    )
    
    # 5. Execute the agent runner using the active session ID
    events = runner.run(
        user_id="user_console",
        session_id=session.id,
        new_message=user_message
    )
    
    # 6. Gather response content from events
    full_response = ""
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    full_response += part.text
                    
    # Clean the response to ensure no markdown blocks are present in stdout
    response_text = full_response.strip()
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    elif response_text.startswith("```"):
        response_text = response_text[3:]
        
    if response_text.endswith("```"):
        response_text = response_text[:-3]
        
    response_text = response_text.strip()
    print(response_text)

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Warning: GEMINI_API_KEY environment variable is not set.")
        print("Please configure it in a '.env' file or your system environment variables.")
        print("Example: GEMINI_API_KEY=AIzaSy...")
        return
        
    # Check if a filename/path parameter was passed
    if len(sys.argv) < 2:
        print("Usage: python main.py <incident_file_path>")
        print("Example: python main.py data/incidents/incident_lot_number.txt")
        return
        
    filename = sys.argv[1]
    asyncio.run(run_agent(filename))

if __name__ == "__main__":
    main()
