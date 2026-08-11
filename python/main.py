import os
import logging
from typing import Dict, Any
import requests
from dotenv import load_dotenv

# Set up standard logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Constants (UPPER_CASE)
DEFAULT_TIMEOUT_SECONDS: int = 10

def trigger_n8n_event(payload: Dict[str, Any]) -> bool:
    """Triggers an n8n workflow using environment configuration."""
    load_dotenv()
    webhook_url: str | None = os.getenv("N8N_WEBHOOK_URL")

    if not webhook_url:
        logger.error("Missing required environment variable: N8N_WEBHOOK_URL")
        return False

    # Use context manager for network connections
    try:
        with requests.Session() as session:
            response = session.post(webhook_url, json=payload, timeout=DEFAULT_TIMEOUT_SECONDS)
            response.raise_for_status()
            logger.info("Successfully triggered n8n workflow: status %d", response.status_code)
            return True
    except requests.RequestException as exc:
        logger.error("Failed to trigger n8n workflow: %s", exc)
        return False

if __name__ == "__main__":
    test_payload: Dict[str, Any] = {"event": "test_run", "status": "active"}
    trigger_n8n_event(test_payload)
