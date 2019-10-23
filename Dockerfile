FROM python:3.6

WORKDIR /home/api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn


ENTRYPOINT ["gunicorn", "-b", ":8080", "--timeout", "1200", "--access-logfile", "-", "--error-logfile", "-", "back.wsgi:application"]