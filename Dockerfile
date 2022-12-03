#
FROM python:3.9

#
WORKDIR /web_api

#
COPY ./requirements.txt /web_api/requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

#
RUN pip install --no-cache-dir --upgrade -r /web_api/requirements.txt

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
