FROM python:3.12.2

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./api /code/api

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.server:app"]
