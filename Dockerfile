FROM python:3.12

ENV POETRY_HOME="/opt/poetry"

ENV PATH="${POETRY_HOME}/bin:$PATH"

RUN apt-get update \ 
  && apt-get install -y \
  && curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . .

CMD ["python", "-u", "app.py"]
