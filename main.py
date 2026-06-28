import os
import sys
import asyncio
import warnings

# Suppress experimental/deprecation warnings to ensure clean JSON stdout
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from agents.email_processor import get_email_processor_agent
from agents.investigation_agent import get_investigation_agent
from agents.rca_agent import get_rca_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Load environment variables from the .env file in the current working directory
dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path=dotenv_path)

async def run_pipeline(filename: str):
    # Setup session service
    session_service = InMemorySessionService()
    
    # ----------------------------------------------------
    # Step 1: Run Email Processing Agent
    # ----------------------------------------------------
    email_processor = get_email_processor_agent()
    session1 = await session_service.create_session(
        app_name="FutureCATLeaf_Processor",
        user_id="user_console"
    )
    runner1 = Runner(
        app_name="FutureCATLeaf_Processor",
        agent=email_processor,
        session_service=session_service
    )
    
    # Resolve the email file path (either direct path or relative to data/incidents/)
    if os.path.exists(filename):
        email_file_path = filename
    else:
        email_file_path = os.path.join("data", "incidents", filename)
        
    if not os.path.exists(email_file_path):
        print(f"Error: File '{filename}' not found directly or in 'data/incidents/'.")
        return

    # User instruction for step 1
    user_prompt1 = f"Please read the email from the file '{email_file_path}' and extract the structured incident object as pure JSON."
    user_message1 = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_prompt1)]
    )
    
    # Execute step 1 runner
    events1 = runner1.run(
        user_id="user_console",
        session_id=session1.id,
        new_message=user_message1
    )
    
    response_processor = ""
    for event in events1:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_processor += part.text
                    
    # Clean the response to ensure no markdown blocks are present
    incident_json = response_processor.strip()
    if incident_json.startswith("```json"):
        incident_json = incident_json[7:]
    elif incident_json.startswith("```"):
        incident_json = incident_json[3:]
    if incident_json.endswith("```"):
        incident_json = incident_json[:-3]
    incident_json = incident_json.strip()

    # ----------------------------------------------------
    # Step 2: Run Investigation Agent
    # ----------------------------------------------------
    investigation_agent = get_investigation_agent()
    session2 = await session_service.create_session(
        app_name="FutureCATLeaf_Investigation",
        user_id="user_console"
    )
    runner2 = Runner(
        app_name="FutureCATLeaf_Investigation",
        agent=investigation_agent,
        session_service=session_service
    )
    
    # Pass the Incident JSON to the Investigation Agent
    user_prompt2 = f"Please investigate the resources for this Incident Object and return the updated object with evidence populated:\n{incident_json}"
    user_message2 = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_prompt2)]
    )
    
    # Execute step 2 runner
    events2 = runner2.run(
        user_id="user_console",
        session_id=session2.id,
        new_message=user_message2
    )
    
    response_investigation = ""
    for event in events2:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_investigation += part.text
                    
    # Clean response
    investigation_json = response_investigation.strip()
    if investigation_json.startswith("```json"):
        investigation_json = investigation_json[7:]
    elif investigation_json.startswith("```"):
        investigation_json = investigation_json[3:]
    if investigation_json.endswith("```"):
        investigation_json = investigation_json[:-3]
    investigation_json = investigation_json.strip()

    # ----------------------------------------------------
    # Step 3: Run RCA Agent
    # ----------------------------------------------------
    rca_agent = get_rca_agent()
    session3 = await session_service.create_session(
        app_name="FutureCATLeaf_RCA",
        user_id="user_console"
    )
    runner3 = Runner(
        app_name="FutureCATLeaf_RCA",
        agent=rca_agent,
        session_service=session_service
    )
    
    # Pass the populated Incident JSON to the RCA Agent
    user_prompt3 = f"Please perform an evidence-based root cause analysis for this Incident Object and return the updated object with the structured rca field populated:\n{investigation_json}"
    user_message3 = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_prompt3)]
    )
    
    # Execute step 3 runner
    events3 = runner3.run(
        user_id="user_console",
        session_id=session3.id,
        new_message=user_message3
    )
    
    response_rca = ""
    for event in events3:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_rca += part.text

    # Clean output JSON to ensure pure raw JSON stdout
    final_output = response_rca.strip()
    if final_output.startswith("```json"):
        final_output = final_output[7:]
    elif final_output.startswith("```"):
        final_output = final_output[3:]
    if final_output.endswith("```"):
        final_output = final_output[:-3]
    final_output = final_output.strip()
    
    print(final_output)

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Warning: GEMINI_API_KEY environment variable is not set.")
        print("Please configure it in a '.env' file or your system environment variables.")
        print("Example: GEMINI_API_KEY=AIzaSy...")
        return
        
    # Check if a filename/path parameter was passed
    if len(sys.argv) < 2:
        print("Usage: python main.py <incident_file_path>")
        print("Example: python main.py data/incidents/Incident_unable_to_make_plan_final.txt")
        return
        
    filename = sys.argv[1]
    asyncio.run(run_pipeline(filename))

if __name__ == "__main__":
    main()
