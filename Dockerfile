FROM python:3.9

WORKDIR /web_api

COPY ./requirements.txt /web_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web_api/requirements.txt
