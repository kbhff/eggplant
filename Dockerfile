FROM python:3.4

WORKDIR /app

RUN apt-get install -y libjpeg62-turbo-dev libfreetype6 libfreetype6-dev

COPY . /app

RUN pip install -r ./requirements/development.txt
RUN pip install -r ./requirements/production.txt

CMD python manage.py runserver 
