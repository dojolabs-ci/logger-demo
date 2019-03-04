import json_logging,logging,sys,os
from random import randint
import time
LOG_LEVEL = 'DEBUG'
LOG_FILE = '/var/log/dojo/app.log'

json_logging.ENABLE_JSON_LOGGING = True
json_logging.COMPONENT_ID = 'test'
json_logging.COMPONENT_NAME = 'dojo logger test'
json_logging.init()

logger = logging.getLogger("dojo-logger")
logger.setLevel(LOG_LEVEL)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.addHandler(logging.FileHandler(LOG_FILE))


lst = [
    "logger message 1",
    "logger message 2",
    "logger message 3",
    "logger message 4",
]

extras = [
    {"title": "this is json data example", "src": "box", "dest": "backend", "child" : {"os" : "linux"}},
    {"title": "this is json data example", "src": "backend", "dest": "box"},
    {"title": "this is json data example", "src": "mobile", "dest": "backend"}
]

while True:
    logger.info(lst[randint(0, len(lst)) -1],extra={'props': extras[randint(0, len(extras)) -1]})
    time.sleep(2)

