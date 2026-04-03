
import time
from datetime import datetime
from database import setup_db
from fetcher import fetch_crypto
from scraper import fetch_news
from exporter import export_to_csv

def run_pipeline():
    print(f"\n--- Pipeline running at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    fetch_crypto()
    fetch_news()
    export_to_csv()

setup_db()
run_pipeline()

print("\nScheduler started — Press Ctrl+C to stop.")
while True:
    time.sleep(3600)      # every 1 hour
    run_pipeline()