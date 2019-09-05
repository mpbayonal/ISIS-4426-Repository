FROM python:3.6

WORKDIR /home/authapi

COPY .env .env
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY auth.py config.py run.sh ./
RUN chmod +x run.sh

ENTRYPOINT ["gunicorn", "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "back.wsgi"]