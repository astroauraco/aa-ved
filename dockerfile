# Use official Python 3.11 image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY app.py .

# Expose port
EXPOSE 10000

# Run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
