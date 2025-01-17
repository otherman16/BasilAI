import os
import yaml
import json


def read_json(path):
    with open(path, 'rt') as f:
        return json.load(f)


def read_yaml(path):
    assert os.path.exists(path)
    with open(path, 'r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)


def write_yaml(data, path):
    with open(path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
