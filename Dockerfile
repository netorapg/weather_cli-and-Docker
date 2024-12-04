FROM python:3.9.20-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
ENTRYPOINT ["python", "/app/src/weather_cli.py"]