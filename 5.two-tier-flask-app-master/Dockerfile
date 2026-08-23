#-------------------Builder stage----------------
FROM python:3.9-slim AS builder

WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir  -r requirements.txt --target=/app/deps

COPY . .

#----------------------Runner stage----------------
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \ 
    apt-get install -y --no-install-recommends libmariadb3 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app /app

ENV PYTHONPATH=/app/deps

CMD ["python","app.py"]


