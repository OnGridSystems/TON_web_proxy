FROM python:3.7-slim

WORKDIR /usr/src/app
RUN pip install pipenv==2018.11.26
COPY Pipfile Pipfile.lock ./
RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc python-dev && \
  pipenv install --system --deploy && \
  apt-get remove -y gcc python-dev && \
  apt-get autoremove -y

COPY . ./

ARG BRANCH=undefined
ARG COMMIT=undefined
ENV BRANCH=${BRANCH}
ENV COMMIT=${COMMIT}
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}

EXPOSE 8080
CMD ["python", "."]
