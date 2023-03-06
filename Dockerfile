FROM ubuntu:latest

# env vars for mongo ip

RUN apt-get update
# check these
RUN apt-get install python3 python3-pip git

RUN mkdir /config

RUN git clone https://github.com/asgardarchive/asgard-sdk.git /sdk && cd /sdk
RUN pip3 install -r requirements.txt
# check these
RUN cd /sdk/asgard-sdk/asgard_sdk && pip3 install -e .

RUN git clone https://github.com/asgardarchive/asgard-metadata.git /api
WORKDIR /api

RUN pip3 install -r requirements.txt
CMD ./main.py -r -c /config/server_config.json
