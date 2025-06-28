# Use Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your bot
CMD ["python", "-m", "bot.ui"]
