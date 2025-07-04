
import json
import os

class AgentMemory:
    def __init__(self, filename='memory.json'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def save_interaction(self, agent_id, content, project_id, interaction_type):
        with open(self.filename, 'r+') as f:
            data = json.load(f)
            data.append({
                "agent": agent_id,
                "project_id": project_id,
                "type": interaction_type,
                "content": content
            })
            f.seek(0)
            json.dump(data, f, indent=2)

    def get_context(self):
        with open(self.filename, 'r') as f:
            return json.load(f)
