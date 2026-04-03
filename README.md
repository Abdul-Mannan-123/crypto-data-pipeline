# 🚀 Crypto Data Pipeline  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Automation](https://img.shields.io/badge/Automation-Cron%20Ready-success)
![API](https://img.shields.io/badge/API-CoinGecko-orange)
![Scraping](https://img.shields.io/badge/Scraping-BeautifulSoup-yellow)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📊 Overview

A fully automated backend pipeline that collects **live cryptocurrency prices** and **breaking crypto news**, processes the data, and stores it in a structured database — while generating clean CSV reports.

Built to run **hands-free every hour**, making it ideal for analytics systems, trading tools, and data-driven applications.

---

## 🖼️ System Flow

```
        ┌──────────────┐
        │ CoinGecko API│
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Price Fetcher│
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Data Cleaner │
        └──────┬───────┘
               │
               ▼
┌──────────────┴──────────────┐
│                             │
▼                             ▼
Database (SQLite)        CSV Export
│
▼
Scheduler (Runs Every Hour)
```

---

## ⚙️ Features

- 📊 Real-time crypto price tracking (BTC, ETH, SOL)  
- 📰 Live scraping of latest crypto news  
- 🗄️ Structured storage with timestamps  
- 📁 Automatic CSV report generation  
- ⏱️ Fully automated hourly execution  
- 🛡️ Clean and modular architecture  

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Core backend logic |
| Requests | API communication |
| BeautifulSoup4 | Web scraping |
| SQLite3 | Data storage |
| CSV | Data export |

---

## 🧠 How It Works

1. Fetch crypto market data via API  
2. Scrape latest news headlines  
3. Clean and structure the data  
4. Store results in database  
5. Export processed data to CSV  
6. Automatically repeat every hour  

---

## 📂 Project Structure

```
crypto-pipeline/
│── main.py              # Pipeline orchestrator
│── fetch_prices.py      # API data fetching
│── scrape_news.py       # News scraping
│── database.py          # Database logic
│── export_csv.py        # CSV export
│── scheduler.py         # Automation logic
│── requirements.txt     # Dependencies
```

---

## ▶️ Getting Started

```bash
git clone https://github.com/Abdul-Mannan-123/crypto-pipeline.git
cd crypto-pipeline
pip install -r requirements.txt
python main.py
```

---

## 📊 Use Cases

- 📈 Crypto tracking dashboards  
- 🤖 Trading bots & signals  
- 📰 News aggregation systems  
- 📊 Data analytics pipelines  

---

## 🔮 Future Improvements

- Add more coins & APIs  
- Deploy on cloud (AWS / VPS)  
- Build web dashboard (FastAPI / Flask)  
- Add alerts (Telegram / Email)  

---

## 💼 Real-World Value

This project demonstrates:

- Backend Automation  
- API Integration  
- Web Scraping  
- Data Pipelines  
- Database Management  

Exactly the kind of systems used in **fintech and data-driven businesses**.

---

## ⭐ Support

If you like this project, consider giving it a star ⭐
