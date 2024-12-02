# Pull official base image
FROM python:3.11.4-slim-buster

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy project
COPY . .

# Open port for Django
EXPOSE 8000

# Run migrations and load fixtures before starting the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py loaddata core/fixtures/directors.json core/fixtures/movies.json && python manage.py runserver 0.0.0.0:8000"]
