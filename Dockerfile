FROM python:3.6
ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1

RUN mkdir /app
WORKDIR /app

COPY . .
RUN cd back
RUN ls -lrt

RUN pip install -r requirements.txt

EXPOSE 8000

RUN ./entry.sh