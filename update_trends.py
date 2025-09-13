import os
import requests
import json
from datetime import datetime

# Получаем API ключ из переменной окружения
API_KEY = os.getenv("APIFY_KEY")
DATASET_ID = "your_dataset_id"  # замени на реальный Dataset ID из Apify

URL = f"https://api.apify.com/v2/datasets/{DATASET_ID}/items?format=json&token={API_KEY}"

OUTPUT_FILE = "weekly-trends.json"

def fetch_trends():
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        trends = {
            "updated_at": datetime.now().isoformat(),
            "items": data
        }
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(trends, f, ensure_ascii=False, indent=2)
        print(f"[OK] Updated {OUTPUT_FILE} with {len(data)} items")
    except Exception as e:
        print("Error fetching trends:", e)

if __name__ == "__main__":
    fetch_trends()
