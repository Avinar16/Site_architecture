FROM python:3.10-slim

WORKDIR /backend/factory

COPY factory/requirements.txt /backend/factory/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "python:8000"]