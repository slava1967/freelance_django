FROM python:3.11.4-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# copy entrypoint-prod.sh
# COPY ./entrypoint.prod.sh /usr/src/app/entrypoint.prod.sh

RUN sed -i 's/\r$//g'  /usr/src/app/entrypoint.sh
RUN chmod +x  /usr/src/app/entrypoint.sh


# run entrypoint.prod.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]