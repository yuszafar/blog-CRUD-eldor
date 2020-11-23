FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN cd /code && poetry install --no-root
COPY . /code/
RUN poetry install

