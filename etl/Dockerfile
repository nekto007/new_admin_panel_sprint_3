FROM python:3.10.2-alpine

WORKDIR /app

RUN  \
    apk update && \
    apk upgrade && \
    pip install --upgrade pip

COPY app/requirements.txt .

# install dependencies with additional dependencies for psycopg2
RUN   \
     apk add --no-cache postgresql-libs &&  \
     apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
     python3 -m pip install -r /app/requirements.txt --no-cache-dir &&  \
     apk --purge del .build-deps


# copy project
COPY ./app /app

CMD python manage.py migrate && python manage.py collectstatic --noinput && \
    gunicorn config.wsgi:application --bind 0.0.0.0:8000