#
FROM python:3.9

#
WORKDIR /web_api

#
ENV env=PROD

#
COPY ./app/ /web_api/app/
COPY ./img/ /web_api/img/
COPY ./routers/ /web_api/routers/
COPY ./services/ /web_api/services/
COPY ./.env /web_api/.env
COPY ./config.py /web_api/config.py
COPY ./database.py /web_api/database.py
COPY ./main.py /web_api/main.py
COPY ./requirements.txt /web_api/requirements.txt


RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

#
RUN pip install --no-cache-dir --upgrade -r /web_api/requirements.txt

#
 CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7999"]
