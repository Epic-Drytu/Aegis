import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / '.env'

if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)

API_GATEWAY_URL = os.getenv('API_GATEWAY_URL', 'https://example.com/api/telemetry')
API_KEY = os.getenv('API_KEY', '')
SCHEDULE_INTERVAL_MINUTES = int(os.getenv('SCHEDULE_INTERVAL_MINUTES', '10'))
