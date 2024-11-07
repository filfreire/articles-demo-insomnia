FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:3000", "app:app"]