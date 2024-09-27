FROM python:3.9.20-slim

WORKDIR /app

COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]