# Pulled Nov 27, 2022
FROM --platform=linux/amd64 python:3.8@sha256:89986864f936860f6e74a7540ab98b23586011e90482b09125aa6792f2ea0195
RUN pip install --upgrade pip && pip install gunicorn==20.1.0
WORKDIR /srv
COPY gunicorn_conf.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY setup.py ./
COPY gamal ./gamal
RUN pip install -e .
ARG VERSION=local-docker
RUN echo "VERSION = '${VERSION}'" > gamal/version.py
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_conf.py", "gamal.main:app"]
