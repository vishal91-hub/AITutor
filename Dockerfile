# Use a lightweight Python base image
FROM python:3.11-slim

# Install OS-level dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    tesseract-ocr \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Expose the port Streamlit uses
EXPOSE 7860

# Start Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=7860", "--server.enableCORS=false"]
