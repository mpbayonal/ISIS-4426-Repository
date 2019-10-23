FROM python:3.6

WORKDIR /home/api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn


ENTRYPOINT ["gunicorn", "--timeout", "300", "-b", ":8080", "--access-logfile", "-", "--error-logfile", "-", "back.wsgi:application"]