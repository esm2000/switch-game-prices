# FROM python:3.8

# WORKDIR /app 

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . . 

# CMD [ "python3", "app.py" ]


# FROM ubuntu:16.04
# RUN apt-get update -y
# RUN apt-get install python -y
# RUN apt-get install python-pip -y
FROM python:3.8

RUN mkdir -p /app
WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app/
ENV FLASK_APP=app.py

CMD flask run -h 0.0.0.0 -p 5000