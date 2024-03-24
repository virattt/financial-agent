FROM python:3.12-bullseye

RUN pip install poetry==1.6.1

WORKDIR /code

COPY . /code/

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD poetry run langchain serve --host 0.0.0.0 --port 8000