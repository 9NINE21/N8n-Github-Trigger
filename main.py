from generator import MRDataGen

def main():
    print("--- Running GitHub MR Automation Test ---")
    
    authors = ["dev-alice", "dev-bob", "ci-bot"]
    branches = ["feat/docs-update", "fix/pipeline-bug", "chore/deps"]
    
    gen = MRDataGen(authors=authors, branches=branches)
    mr_event = gen.generate_mr()
    
    # Process simulated MR metadata
    print(f"MR #{mr_event['mr_id']} created by @{mr_event['author']}")
    print(f"Branch: {mr_event['source_branch']} -> {mr_event['target_branch']}")
    print(f"Pipeline Status: {mr_event['status'].upper()}")

if __name__ == "__main__":
    main()
