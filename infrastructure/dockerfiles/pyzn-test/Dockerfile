#
FROM python:3.11 AS requirements-stage

#
WORKDIR /tmp

#
RUN pip install pipenv

#
COPY ./Pipfile* /tmp/

#
RUN pipenv requirements --dev > requirements.txt

#
FROM python:3.11 AS pyzn-test

#
WORKDIR /code

#
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


#
COPY ./tests /code/tests