#!/usr/bin/env python
import sys

from flask import Blueprint

from app import app
from app.controller import restx, hello_controller, status_controller
from app.controller.restx import api

restx.init(app=app)
blueprint = Blueprint('api', __name__, url_prefix=None)
api.init_app(blueprint)
api.add_namespace(status_controller.ns)
api.add_namespace(hello_controller.ns)
app.register_blueprint(blueprint)


def start_dev_server():
    app.run("0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: server.py [command]")
        print("Commands:")
        print("\tdevserver")
        print("\t\t run Flask server in debug mode")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "devserver":
        start_dev_server()
    else:
        raise Exception(f"Unknown command '{sys.argv[1]}'")
