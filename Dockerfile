FROM python:3.10-slim-buster

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 8000

CMD ["uvicorn", "app.v1.endpoints.api:app","--host","0.0.0.0"]
