# Start from selenium/standalone-chrome
FROM selenium/standalone-chrome:latest

# Set working directory
WORKDIR /app

# Install pip and Python if missing
USER root
RUN apt-get update && apt-get install -y python3-pip

# Copy requirements first and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set the default command
CMD ["python3", "browser-test.py"]
