FROM python:3.12-alpine
WORKDIR /app

ENV PYTHONUNBUFFERED=1 PORT=5000

ARG IMAGE_VERSION
LABEL version=$IMAGE_VERSION

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data

EXPOSE 5000

RUN adduser -D appuser && mkdir -p /data && chown appuser:appuser /data
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "src.app:app"]
