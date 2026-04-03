# Crypto Data Pipeline 🚀

An automated data pipeline that fetches live cryptocurrency prices and scrapes crypto news headlines, stores them in a database, and exports to CSV — all running automatically every hour.

## Features
- Fetches live BTC, ETH, SOL prices from CoinGecko API
- Scrapes latest crypto news headlines from CoinDesk
- Stores all data in SQLite database with timestamps
- Auto exports to CSV every run
- Runs automatically every hour

## Tech Stack
- Python
- SQLite
- BeautifulSoup4
- Requests

## Setup
pip install -r requirements.txt

## Run
py main.py

## Project Structure
- main.py — entry point
- fetcher.py — crypto price fetching
- scraper.py — news scraping
- database.py — db setup
- exporter.py — csv export
- config.py — settings
