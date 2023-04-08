FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV LANG ru_RU.UTF-8

RUN apt-get update &&  \
    apt-get install --no-install-recommends -y \
    git \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . /code

RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "/code/.dockerinit.sh" ]
EXPOSE 8000
