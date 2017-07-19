FROM python:3.6

MAINTAINER Ulrich Petri <mail@ulo.pe>

ADD requirements.txt /requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD app.py /app.py

ENTRYPOINT ["/usr/local/bin/python3", "/app.py"]
