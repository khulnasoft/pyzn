#
FROM python:3.11 AS requirements-stage

#
WORKDIR /tmp

#
RUN pip install pipenv

#
COPY ./Pipfile* /tmp/

#
RUN pipenv requirements > requirements.txt

#
FROM python:3.11 AS pyzn

#
WORKDIR /code

#
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
EXPOSE 8080
ENV PORT=8080


#
COPY ./infrastructure/dockerfiles/pyzn/gunicorn.conf.py /code
COPY ./pyzn /code/pyzn

#
CMD ["newrelic-admin", "run-program", "gunicorn", "-c", "gunicorn.conf.py", "pyzn.infrastructure.web.__init__:app"]