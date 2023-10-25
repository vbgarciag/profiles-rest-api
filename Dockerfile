# Use an Ubuntu base image with Python 3.8
FROM ubuntu:20.04

# Set environment variables to prevent interactive installation prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Update package lists and install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libpq-dev \
    tzdata \
    && apt-get clean

# Create and set the working directory
WORKDIR /app

# use python instead of python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your Django application code into the container
COPY . /app/

# Expose the port your Django app will run on (change if needed)
EXPOSE 8000

# Run your Django application (customize this based on your project's needs)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]