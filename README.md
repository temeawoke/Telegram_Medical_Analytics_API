# Telegram_Medical_Analytics_API
An end-to-end data product that scrapes public Telegram channels for Ethiopian medical-related content, extracts and enriches product data using object detection (YOLO), transforms it via dbt, and serves it through an analytical API.


# Telegram Analytics API

This project provides a backend system to collect, store, and analyze Telegram chat data using Python, PostgreSQL, and Docker.

---

## 🚀 Features

- Telegram Bot integration for data collection
- PostgreSQL database for storing analytics
- Environment management using `.env`
- Fully containerized with Docker and Docker Compose
- Secrets managed securely and excluded from Git

---

## 📁 Project Structure

```
telegram-medical-analytics-api/
├── api
│   └── main.py
├── .env
├── .dockerfile
├── .docker-composer.yml
├── .requirements.txt
├── .gitignore
├── scrape_telegram.py
├── telegram_scraping_task1.ipynb
├── notebooks/
│   └── data/
│       ├── telegram_messages/
│       │   └── YYYY-MM-DD/
│       │       └── channel_name.json
│       └── images/
│           └── channel_name_msgid.jpg
│   └── telegram_scraping_task1.ipynb
├── telegram_scraper
│   └── main.py
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/temeawoke/Telegram_Medical_Analytics_API.git
cd telegram-analytics-api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# On Windows
env\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
TELEGRAM_API_KEY=23786461
DB_USER=admin
DB_PASSWORD=secret
DB_NAME=medical_data
DB_HOST=db
DB_PORT=5432
```

**Note:** The `.env` file is added to `.gitignore` to avoid committing sensitive info.

---

### 5. Run the Project Using Docker

```bash
docker-compose up --build
```

---

## 🔌 Technologies Used

- Python 3.10+
- PostgreSQL 15
- Docker & Docker Compose
- python-dotenv
- SQLAlchemy (or your DB ORM)
- Telegram Bot API

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
```

---

## ▶️ Running the Scraper

```bash
python scrape_telegram.py
```

Or use the provided Jupyter notebook:
```
telegram_scraping_task1.ipynb
---

