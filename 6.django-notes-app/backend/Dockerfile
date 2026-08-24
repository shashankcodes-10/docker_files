#----------------------builder--------------------------------
FROM python:3.9-slim AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir  --prefix=/install -r requirements.txt 

COPY . .

#-----------------------runner----------------------------------
FROM python:3.9-slim 

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libmariadb3 curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 notesapp.wsgi:application"]
