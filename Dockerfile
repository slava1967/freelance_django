FROM python:3.10-alpine

RUN pip install --upgrade pip

COPY . .

#COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/freelance_django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/freelance_django/entrypoint.sh
RUN chmod +x /usr/src/freelance_django/entrypoint.sh

ENTRYPOINT ["/usr/src/freelance_django/entrypoint.sh"]