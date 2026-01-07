from constants import DATA_PATH
import json
from pprint import pprint

# convenience/utility function to read a json file
def read_json(filename):
    with open(DATA_PATH / filename) as file:
        data = json.load(file)

    return data

pprint(read_json("library.json"))
