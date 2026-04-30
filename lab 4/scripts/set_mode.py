import json
import sys


def set_storage(mode):
    with open('config.json', 'r') as f:
        config = json.load(f)

    config['storage_type'] = mode

    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
    print(f"The mode has been changed to: {mode}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        set_storage(sys.argv[1])
    else:
        print("Using: python set_mode.py [console|redis|kafka]")