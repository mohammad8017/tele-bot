FROM python:latest

WORKDIR /usr/app/mhmd

COPY main.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]