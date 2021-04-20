FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

ENV PROJECT_DIR /ecommerce

WORKDIR ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

RUN pip install -r requirements.txt
RUN apt update && apt install -y libpq-dev gcc

RUN pip install psycopg2
