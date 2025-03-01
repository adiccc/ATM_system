FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make port 8080 available (Cloud Run expects this port)
ENV PORT=8080

# Run the application
CMD exec gunicorn --bind :$PORT server.main:app -k uvicorn.workers.UvicornWorker