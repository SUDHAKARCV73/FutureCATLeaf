import os
import json

RESOURCES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources")

def search_application_logs(query: str) -> str:
    """Searches the application logs for any entries containing the specified query.

    Args:
        query: The search term or keyword (e.g. market name, lot number, error code).

    Returns:
        A string containing matching log lines, or a message indicating no matches.
    """
    log_file = os.path.join(RESOURCES_DIR, "logs", "application_logs.txt")
    if not os.path.exists(log_file):
        return "Log file not found."
        
    matches = []
    query_lower = query.lower()
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if query_lower in line.lower():
                matches.append(line.strip())
                
    if matches:
        return "\n".join(matches)
    return "No matching log entries found."

def read_deployment_history() -> str:
    """Reads the entire deployment history markdown file.

    Returns:
        The markdown text content of the deployment history.
    """
    deployment_file = os.path.join(RESOURCES_DIR, "deployments", "deployment_history.md")
    if not os.path.exists(deployment_file):
        return "Deployment history file not found."
        
    with open(deployment_file, "r", encoding="utf-8") as f:
        return f.read()

def search_master_data(dataset_name: str, query_key: str) -> str:
    """Searches JSON master datasets (like 'shift_calendar' or 'lot_master') for entries.

    Args:
        dataset_name: The name of the dataset to search ('shift_calendar' or 'lot_master').
        query_key: The search term (e.g. market name like 'Ghana', or lot number like 'V_AR230012').

    Returns:
        A JSON string containing the list of matching records.
    """
    dataset_file = os.path.join(RESOURCES_DIR, "master_data", f"{dataset_name}.json")
    if not os.path.exists(dataset_file):
        return f"Dataset '{dataset_name}' not found."
        
    with open(dataset_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    matches = []
    query_lower = str(query_key).lower()
    for item in data:
        item_str = str(item).lower()
        if query_lower in item_str:
            matches.append(item)
            
    return json.dumps(matches, indent=2)

def search_knowledge_base(query: str) -> str:
    """Searches the knowledge base of past RCAs for entries containing the query.

    Args:
        query: The search term or keyword (e.g. error code 'ORA-20001', process, etc.).

    Returns:
        A string containing matching sections or lines from the past RCAs.
    """
    kb_file = os.path.join(RESOURCES_DIR, "knowledge", "past_rca.md")
    if not os.path.exists(kb_file):
        return "Knowledge base file not found."
        
    with open(kb_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split("\n")
    matches = []
    query_lower = query.lower()
    
    current_section = ""
    for line in lines:
        if line.startswith("## "):
            current_section = line
        if query_lower in line.lower():
            if current_section and current_section not in matches:
                matches.append(current_section)
            matches.append(line)
            
    if matches:
        return "\n".join(matches)
    return "No matching records found in the knowledge base."
