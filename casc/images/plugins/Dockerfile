FROM python:3.6.8

ADD ./files/requirements.txt /usr/local/docker/requirements.txt

RUN pip install --no-cache-dir -r /usr/local/docker/requirements.txt

WORKDIR /usr/local/docker
