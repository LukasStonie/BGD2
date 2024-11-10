FROM python:3.12

WORKDIR /usr/src/app
COPY onlineshop.py .

RUN pip install Flask redis

ENV FLASK_APP=onlineshop.py
ENV FLASK_ENV=development

CMD flask run --host 0.0.0.0

