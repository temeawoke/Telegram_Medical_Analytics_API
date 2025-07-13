# Step 1: Import dotenv and os
from dotenv import load_dotenv
import os

# Step 2: Load variables from .env file
load_dotenv()

# Step 3: Access those variables using os.getenv
telegram_api_id = os.getenv("TELEGRAM_API_ID")
telegram_api_hash = os.getenv("TELEGRAM_API_HASH")

# Step 4: (Optional) Print or use them
print("Telegram API ID:", telegram_api_id)
