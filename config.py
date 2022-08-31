import yaml


config = {}


def load():
    with open('./config.yml') as f:
        global config
        config = yaml.load(f, Loader=yaml.FullLoader)


def get(key: str):
    try:
        value = config
        keys = key.split('.')
        for segment in keys:
            value = value[segment]
        return value
    except KeyError as error:
        print('Config key does not exist: ', error)
    return None


