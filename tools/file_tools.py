import os

def read_incident_email(file_path: str) -> str:
    """Reads the content of an incident email file from the local filesystem.

    Args:
        file_path: The relative or absolute path to the incident email file.

    Returns:
        The text content of the email file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Email file not found at path: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
