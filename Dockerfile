FROM python:3.9.7-alpine3.14

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

ENV GOOGLE_API_KEY=""

CMD ["gunicorn", "--bind", ":8000", "application.wsgi:app"]