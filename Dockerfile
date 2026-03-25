FROM python:3.9-slim
WORKDIR /app
COPY app/main.py .
CMD ["python", "main.py"]
