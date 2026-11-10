FROM python:3.12-slim

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HF_HUB_DISABLE_XET=1

WORKDIR /app

# Install system packages
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for Docker layer caching
COPY requirements.txt .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install CPU version of PyTorch
RUN python -m pip install \
    torch \
    --index-url https://download.pytorch.org/whl/cpu

# Install project dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Pre-download reranker model during image build
RUN python -c "from sentence_transformers import CrossEncoder; CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')"

# Copy project files
COPY . .

# Cloud Run port
EXPOSE 8080

# Start application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]