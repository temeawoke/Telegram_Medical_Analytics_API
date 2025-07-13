from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv
import os
import json

# Load secrets
load_dotenv()
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

# Target channels
channels = [
    'https://t.me/lobelia4cosmetics',
    'https://t.me/tikvahpharma',
]

# Create Telegram client session
with TelegramClient('session_name', api_id, api_hash) as client:
    for channel in channels:
        print(f"📥 Scraping channel: {channel}")
        for message in client.iter_messages(channel, limit=100):  # Adjust limit as needed
            print("Message:", message.text)
            if message.media:
                print("🖼 Media type:", type(message.media).__name__)
