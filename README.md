# Telegram Medical Analytics API

This project extracts and transforms Telegram messages and media from Ethiopian medical-related Telegram channels using dbt and Python. It supports analytics and ML use cases like object detection and sentiment analysis.

---

## ✅ Features

- Scrape raw Telegram messages and images
- Store unprocessed JSON files in a data lake
- Load raw data into PostgreSQL (raw schema)
- Transform data using dbt into a clean star schema:
  - `dim_channels`
  - `dim_dates`
  - `fct_messages`
- Built-in dbt tests and documentation

---

## 📁 Project Structure

```
telegram-medical-analytics-api/
├── data/
│   └── raw/
│       ├── telegram_messages/
│       │   └── YYYY-MM-DD/
│       │       └── channel_name.json
│       └── images/
│           └── channel_msgid.jpg
├── telegram_scraping_task1.ipynb
├── load_json_to_postgres.py
├── telegram_dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_telegram_messages.sql
│   │   ├── marts/
│   │   │   ├── dim/
│   │   │   │   └── dim_channels.sql
│   │   │   │   └── dim_dates.sql
│   │   │   └── fct/
│   │   │       └── fct_messages.sql
│   │   └── schema.yml
├── .env
├── .gitignore
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Virtual Environment
```bash
python -m venv env
env\Scripts\activate      # Windows

```

### 2. Install Python Requirements
```bash
pip install -r requirements.txt
```

### 3. Install dbt
```bash
pip install dbt-postgres
```

### 4. Create `.env`
```env
TELEGRAM_API_ID=23786461
TELEGRAM_API_HASH=a442d356a70cb78b21df5af9a84dffb7
DB_NAME=medical_data
DB_USER=admin
DB_PASSWORD=secret
DB_HOST=localhost
DB_PORT=5432
```


---

## 🧪 Run Scripts

### Load Raw JSON into PostgreSQL
```bash
python load_json_to_postgres.py
```

### dbt Workflow
```bash
cd telegram_dbt
dbt run
dbt test
dbt docs generate
dbt docs serve
```

---

## ✅ Tests in dbt

- `unique` and `not_null` on message IDs and timestamps
- Custom test: no future-dated messages

---

## 📬 Contact

For suggestions or issues, please open a GitHub issue or submit a pull request.
