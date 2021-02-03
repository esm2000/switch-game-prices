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
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py /home/app.py
ENTRYPOINT FLASK_APP=/home/app.py flask run --host=0.0.0.0