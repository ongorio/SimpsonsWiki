from pathlib import Path
import json

def get_secrets(config_file: Path) -> dict:
    secrets = json.loads(config_file.read_text())
    return secrets