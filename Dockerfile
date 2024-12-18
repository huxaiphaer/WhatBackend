FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt pytest pytest-django

COPY . /app/

EXPOSE 8001

# We'll use a shell script to handle startup
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]