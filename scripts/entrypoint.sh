#!/bin/bash

# Wait for database
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database started"

# Run migrations
python manage.py migrate

# Start the application
python manage.py runserver 0.0.0.0:8001
