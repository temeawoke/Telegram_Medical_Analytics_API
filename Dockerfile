# Dockerfile

# Use a lightweight base image with Python
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependencies list first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Default command (can be overridden by docker-compose)
CMD ["python", "telegram_scraper/main.py"]
