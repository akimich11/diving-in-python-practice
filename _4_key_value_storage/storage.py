import os
import tempfile
import argparse
import json


def get_args():
    """Parses program arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help="set Key")
    parser.add_argument('--val', help="set Value")
    return parser.parse_args()


def read_data(path):
    """Reads storage data from JSON file and returns a dict"""
    if os.path.exists(path):
        with open(path) as f:
            return json.loads(f.read())
    return {}


def add_value(args, path):
    """Adds value to dict and writes it in JSON file"""
    my_data = read_data(path)
    if args.key not in my_data:
        my_data[args.key] = [args.val]
    else:
        my_data[args.key].append(args.val)

    with open(storage_path, 'w') as f:
        f.write(json.dumps(my_data))


def print_value(key, path):
    """Finds and prints all values by key"""
    my_data = read_data(path)
    if key in my_data:
        print(', '.join(my_data[key]))


if __name__ == "__main__":
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    args = get_args()

    if args.key is not None and args.val is not None:
        add_value(args, storage_path)

    elif args.key is not None:
        print_value(args.key, storage_path)
