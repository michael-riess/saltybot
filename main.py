import config
import saltybet


def setup():
    config.load()
    saltybet.setup()


def teardown():
    saltybet.teardown()


setup()
