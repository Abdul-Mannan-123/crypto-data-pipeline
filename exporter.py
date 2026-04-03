
import csv
import sqlite3

def export_to_csv():
    conn = sqlite3.connect("crypto.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM CRYPTO")
    rows = cursor.fetchall()
    with open("crypto_prices.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Symbol", "Price", "Change_24HR", "Fetched_At"])
        writer.writerows(rows)
    print(f"✅ Exported {len(rows)} rows to crypto_prices.csv")

    cursor.execute("SELECT * FROM NEWS")
    rows = cursor.fetchall()
    with open("crypto_news.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Headline", "Scraped_At"])
        writer.writerows(rows)
    print(f"✅ Exported {len(rows)} headlines to crypto_news.csv")

    conn.close()