# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy app source code
COPY . .

# Expose port and run Flask app
EXPOSE 5001

CMD ["python", "app.py"]
