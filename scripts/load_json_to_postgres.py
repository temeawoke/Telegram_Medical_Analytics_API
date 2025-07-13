# scripts/load_json_to_postgres.py

import os
import json
import psycopg2
from glob import glob
from datetime import datetime

conn = psycopg2.connect(
    host="localhost", dbname="telegram", user="postgres", password="yourpassword", port=5432
)
cur = conn.cursor()

RAW_DIR = "data/raw/telegram_messages/"

def load_json_file(filepath, channel):
    with open(filepath, "r", encoding="utf-8") as f:
        messages = json.load(f)

    for msg in messages:
        cur.execute("""
            INSERT INTO raw.telegram_messages (message_id, channel_name, timestamp, text, media_type)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (message_id) DO NOTHING;
        """, (
            msg["id"],
            channel,
            msg["date"],
            msg.get("message", ""),  # fallback for missing text
            msg["media"].get("_", None) if msg.get("media") else None
        ))

    conn.commit()

for date_dir in os.listdir(RAW_DIR):
    date_path = os.path.join(RAW_DIR, date_dir)
    for json_file in glob(f"{date_path}/*.json"):
        channel = os.path.basename(json_file).replace(".json", "")
        load_json_file(json_file, channel)

cur.close()
conn.close()
