import json
import random

class MRDataGen:
    def __init__(self, authors: list = None, branches: list = None):
        self.authors = authors or ["dev-alice", "dev-bob", "ci-bot"]
        self.branches = branches or ["feat/docs-update", "fix/pipeline-bug", "chore/deps"]

    def generate_event() -> dict:
        """Generates a GitHub-compliant pull_request event payload."""
        return {
            "action": random.choice(["opened", "synchronize", "closed"]),
            "number": random.randint(10, 99),
            "pull_request": {
                "id": random.randint(1000, 9999),
                "title": "Update test documentation for PR automation",
                "user": {"login": random.choice(self.authors)},
                "head": {"ref": random.choice(self.branches)},
                "base": {"ref": "main"},
                "merged": random.choice([True, False])
            }
        }


def main():
    print("Generating mock GitHub PR payload...")
    gen = MRDataGen()
    event_data = gen.generate_event()
    
    # Save payload to event.json for local testing
    filename = "event.json"
    with open(filename, "w") as f:
        json.dump(event_data, f, indent=2)
        
    print(f"✓ Created '{filename}' for PR #{event_data['number']} ({event_data['action']})")


if __name__ == "__main__":
    main()
