FROM python:3.8.7-alpine3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
#exposing port 5000 for flask
ENV FLASK_APP=Flask_app.py
#creating enviroment variable to flask to use and this way flask knows which app to run
CMD flask run --host=0.0.0.0
#making the app run through all the available networks


