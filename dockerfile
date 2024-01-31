FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

COPY . .

EXPOSE 8000

CMD [ "python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]

