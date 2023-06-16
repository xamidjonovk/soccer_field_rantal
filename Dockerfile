# Pull official base image
FROM python:3.10-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential binutils libproj-dev gdal-bin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory in the Docker container
WORKDIR /usr/src/app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the source code of the Django application into the Docker container
COPY . .

# Run the application
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
