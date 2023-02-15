FROM python:3.10

MAINTAINER Ulrich Petri <mail@ulo.pe>

ADD requirements.txt /requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD app.py /app.py

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python3", "/app.py"]
CMD ["--bind-host", "0.0.0.0"]
