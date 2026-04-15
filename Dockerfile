# =========================
# Stage 1
# =========================
FROM python:3.10-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# =========================
# Stage 2
# =========================
FROM python:3.10-slim

WORKDIR /app

COPY --from=base /install /usr/local

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "testify.py", "--server.port=8501", "--server.address=0.0.0.0"]