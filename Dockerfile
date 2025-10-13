FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade --index-url https://pypi.org/simple pip setuptools wheel
RUN pip install --no-cache-dir --index-url https://pypi.org/simple -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]