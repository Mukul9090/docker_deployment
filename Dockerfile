# Use the official Python image as the base
FROM python:3.8-slim

# Set up a working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and input file
COPY . .

# Run the Python script to generate the PDF
CMD ["python3", "app.py"]
