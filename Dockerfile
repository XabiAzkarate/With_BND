FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "where_is_the_rocket.wsgi:application", "--bind", "0.0.0.0:8000"]