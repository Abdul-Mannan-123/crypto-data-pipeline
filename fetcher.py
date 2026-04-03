
import sqlite3
import requests
from datetime import datetime
from config import CRYPTO_URL, PARAMS

def fetch_crypto():
    response = requests.get(CRYPTO_URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        conn = sqlite3.connect("crypto.db")
        cursor = conn.cursor()

        for coin in data:
            cursor.execute("""
                INSERT INTO CRYPTO (NAME, SYMBOL, PRICE, CHANGE_24HR, FETCHED_AT)
                VALUES (?, ?, ?, ?, ?)
            """, (
                coin["name"],
                coin["symbol"],
                coin["current_price"],
                coin["price_change_percentage_24h"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

        conn.commit()
        conn.close()
        print(f"✅ Crypto prices stored — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    else:
        print(f"❌ Crypto API failed: {response.status_code}")