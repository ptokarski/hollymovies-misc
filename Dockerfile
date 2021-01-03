FROM python:3.9-alpine3.12

ENV WORKSPACE ${HOME}/workspace
RUN mkdir ${WORKSPACE}
WORKDIR ${WORKSPACE}

RUN apk update && apk add gcc postgresql-dev musl-dev

COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY ./app.py ./app.py
COPY ./hollymovies ./hollymovies
COPY ./templates ./templates

# WARNING: Database must be upgraded before running this image as a container!
CMD flask run -h 0.0.0.0
