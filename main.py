from sys import exit
from os import getenv
from os.path import exists, isfile

from argparse import ArgumentParser
from json import load
from google.protobuf.json_format import ParseDict

from asgard_sdk.models.config_pb2 import ServerConfig 

# pip packages are getting installed under the wrong name asgard-sdk instead of asgard_sdk

from api.api import Rest

HOME = getenv("HOME")
CONFIG_PATH = "{}/.config/asgard/server_config.json".format(HOME)


def get_config(config_path: str):
    if config_path.startswith("~"):
        config_path = config_path.replace("~", HOME)
    
    if exists(config_path) is False:
        print("[error] Failed to find config file: ", config_path)
        exit(1)
    
    if isfile(config_path) is False:
        print("[error] Config must be a file: ", config_path)
        exit(1)

    if config_path.endswith('.json') is False:
        print("[error] Config must be a json file: ", config_path)
        exit(1)

    with open(config_path, "r") as file:
        document = load(file)
        model = ServerConfig()
        
        config = ParseDict(document, model)

    return config

parser = ArgumentParser()

parser.add_argument("-c", "--config", action="store", default=CONFIG_PATH)
parser.add_argument("-r", "--run", action="store_true")

if __name__ == "__main__":
    args = parser.parse_args()

    if args.config:
        config = get_config(args.config)

    if args.run:
        rest = Rest(config)
        rest.run()