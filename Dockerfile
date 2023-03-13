FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip git protobuf-compiler -y

RUN mkdir /config

RUN git clone https://github.com/asgardarchive/asgard_sdk.git /sdk
WORKDIR /sdk
RUN pip3 install -r requirements.txt
RUN pip3 install -e .

RUN git clone https://github.com/asgardarchive/asgard-metadata.git /api
WORKDIR /api

RUN pip3 install -r requirements.txt
# CMD python3 main.py -r -c /config/server_config.json
