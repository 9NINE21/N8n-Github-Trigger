import random

class MRDataGen:
    def __init__(self, authors: list, branches: list):
        self.authors = authors
        self.branches = branches

    def generate_mr(self) -> dict:
        return {
            "mr_id": random.randint(100, 999),
            "author": random.choice(self.authors) if self.authors else "bot",
            "source_branch": random.choice(self.branches) if self.branches else "patch-1",
            "target_branch": "main",
            "status": random.choice(["opened", "merged", "closed"])
        }