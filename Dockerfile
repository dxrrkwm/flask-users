FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .

RUN mkdir -p instance && chown -R root:root instance

ENV FLASK_APP=app.py
ENV FLASK_CONFIG=production
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "app.py"] 