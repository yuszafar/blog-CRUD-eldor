FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY pyproject.toml /code/
RUN poetry install
COPY . /code/
