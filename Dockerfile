# Use the official Python image as the base image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY . /requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the Telegram bot code to the working directory
COPY . /app.py 


# Expose the port that the Telegram bot listens on
EXPOSE 8443

# Start the Telegram bot when the container starts
CMD ["python", "app.py"]
