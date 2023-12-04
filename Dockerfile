# BASE
FROM python:3.11-slim as base
# install gcc
RUN apt-get update \
	&& apt-get -y install gcc \
	&& rm -rf /var/lib/apt/lists/* 

# DEVELOPMENT
FROM base as development
ENV \
	PIP_NO_CACHE_DIR=off \
	PIP_DISABLE_PIP_VERSION_CHECK=on \
	PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	VIRTUAL_ENV=/pybay-venv 
ENV \
	POETRY_VIRTUALENVS_CREATE=true \
	POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_PROMPT={"python_version"} \
	POETRY_NO_INTERACTION=1 \
	POETRY_VERSION=1.4.2

# install poetry 
RUN pip install "poetry==$POETRY_VERSION"
# copy requirements
COPY poetry.lock pyproject.toml ./

# add venv to path 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python packages
RUN python -m venv $VIRTUAL_ENV \
	&& . $VIRTUAL_ENV/bin/activate \
	&& poetry install --no-root

# BUILDER
FROM development as builder
WORKDIR /app/project
COPY . ./ 
RUN poetry install --without dev
# export build
EXPOSE 8000
