import logging as log
import sys

from flask import Flask

from app.controller import restx

app = Flask(__name__)

root = log.getLogger()
root.setLevel(log.DEBUG)
log_handler = log.StreamHandler(sys.stdout)
log_handler.setLevel(log.DEBUG)
formatter = log.Formatter('%(asctime)s %(levelname)s (%(filename)s:%(lineno)d) - %(message)s')
log_handler.setFormatter(formatter)
root.addHandler(log_handler)
