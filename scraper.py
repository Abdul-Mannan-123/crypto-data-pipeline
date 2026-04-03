
import sqlite3
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from config import NEWS_URL

def fetch_news():
    response = requests.get(NEWS_URL)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("div", class_="font-serif text-md font-medium leading-[22px] line-clamp-2 text-default mb-1")

    if headlines:
        conn = sqlite3.connect("crypto.db")
        cursor = conn.cursor()

        for headline in headlines:
            cursor.execute("""
                INSERT INTO NEWS (HEADLINE, SCRAPED_AT)
                VALUES (?, ?)
            """, (
                headline.text.strip(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

        conn.commit()
        conn.close()
        print(f"✅ {len(headlines)} headlines stored — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    else:
        print("❌ No headlines found — page structure may have changed")