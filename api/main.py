# api/main.py

from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create FastAPI instance
app = FastAPI(
    title="Telegram Medical Analytics API",
    description="Exposes insights extracted from Ethiopian Telegram medical channels",
    version="1.0.0"
)

# Test route
@app.get("/")
def root():
    return {"message": "Telegram Analytics API is running!"}

# Example: Get Telegram API ID (for demo purposes only)
@app.get("/config")
def show_config():
    return {
        "TELEGRAM_API_ID": os.getenv("TELEGRAM_API_ID"),
        "POSTGRES_DB": os.getenv("POSTGRES_DB")
    }
