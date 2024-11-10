# Use a lightweight Python image
FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
