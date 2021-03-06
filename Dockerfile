FROM python:3.6-alpine
MAINTAINER Pulkit Kumar <ispulkitkr@gmail.com>
ENV PS1="\[\e[0;33m\]|> stocksense <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /src
COPY . /src
RUN apk update && \
    apk add git && \
    pip install --no-cache-dir -r requirements.txt \
    && rm -f /usr/local/lib/python3.6/site-packages/cement.egg-link \
    && cd src/cement \
    && python setup.py install \
    && cd /src \
    && rm -rf src/cement \
    && python setup.py install
RUN rm -rf /src
WORKDIR /
ENTRYPOINT ["stocksense"]
