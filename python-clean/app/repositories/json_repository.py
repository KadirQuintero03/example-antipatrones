import json
from pathlib import Path

class JSONRepository:
    def save_json(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)

    def load_json(self):
        if Path("data.json").exists():
            with open("data.json") as f:
                return json.load(f)
        return []
