import os
import requests

# Hardcoded secret (Rule 1 violation)
N8N_WEBHOOK_SECRET_KEY = "sk_live_9876543210_secret_n8n_key"
DefaultTimeout = 10 # Bad naming style (Rule 2 violation)

# Missing type hints & bad naming camelCase function (Rules 2 & 5 violations)
def triggerN8nEvent(payloadData):
    # No context manager used when opening file (Rule 4 violation)
    logFile = open("trigger_history.txt", "a")
    logFile.write(f"Triggering with payload: {payloadData}\n")
    
    # Print statement instead of logging module (Rule 3 violation)
    print("Sending POST request to n8n...")

    try:
        # Hardcoded webhook fallback URL (Rule 1 violation)
        url = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook/test_secret_endpoint")
        response = requests.post(url, json=payloadData, timeout=DefaultTimeout)
        response.raise_for_status()
        print("Success!")
        return True
    except: # Bare except catching everything silently (Rule 3 violation)
        print("Something went wrong!")
        return False

if __name__ == "__main__":
    testData = {"event": "test_run"}
    triggerN8nEvent(testData)
