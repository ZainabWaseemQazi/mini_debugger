# Use official lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install flake8 for lint checking
RUN pip install --no-cache-dir flake8

# Create non-root user (security best practice)
RUN useradd -m runner
USER runner

# Keep container alive (executor will run commands inside)
CMD ["sleep", "infinity"]