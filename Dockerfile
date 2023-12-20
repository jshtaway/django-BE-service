FROM python:3.9-alpine3.13
LABEL maintainer="https://github.com/jshtaway"

# print python output to the console
ENV PYTHONUNBUFFERED 1

# Set the working directory
COPY ./app /app
WORKDIR /app

# Expose the port for the app
EXPOSE 8000

# Copy the requirements.txt file to the container
COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt

ARG DEV=false

# create venv, update pip, install dependencies, remove tmp (to keep docker lightweight),
# create user so we're not opporating in root for security
# install dev dependencies and give user own access if dev = true
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt && \
        chown -R django-user /app/app/tests; \
    fi && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"

USER django-user


