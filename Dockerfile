FROM python:3.7-slim-stretch

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /twitterapp

COPY requirements.txt /twitterapp/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /twitterapp/

EXPOSE 7000

CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]