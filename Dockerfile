# Base image - slim keeps it lightweight
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (layer caching trick!)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]