FROM python:3.6
ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT celery worker -A back -l info -n %n