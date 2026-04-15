# =========================
# Stage 1 (builder)
# =========================
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt


# =========================
# Stage 2 (runtime)
# =========================
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages
COPY --from=builder /root/.local /root/.local

# Copy app code
COPY . .

# Make sure Python sees user packages
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8501

CMD ["streamlit", "run", "testify.py", "--server.port=8501", "--server.address=0.0.0.0"]