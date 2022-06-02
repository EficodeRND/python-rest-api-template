import logging as log

from flask import request
from flask_restx import Namespace, Resource, fields

from app.service import hello_world_service
from app.util.flask_decorators import require_auth

ns = Namespace('api', description='Hello api')

resource_fields = ns.model('Resource', {
    'name': fields.String(example="John")
})


@ns.route('/')
class HelloController(Resource):

    @ns.response(200, 'OK')
    def get(self):  # pylint: disable=no-self-use
        try:
            return hello_world_service.say_hello(), 200
        except Exception:  # pylint: disable=broad-except
            log.exception("Error calling service")
            return "Bad Request", 400


@ns.route('/<string:api_key>')
class ProtectedHelloController(Resource):

    @ns.response(200, 'OK')
    @ns.doc(body=resource_fields)
    @require_auth()
    def post(self, api_key: str):  # pylint: disable=no-self-use
        try:
            payload = request.get_json()
            name = payload.get('name', None)
            if name is None:
                return "No name defined in request body", 400
            return f"Hello {name}!", 200
        except Exception:  # pylint: disable=broad-except
            log.exception("Error echoing name")
            return "Bad Request", 400
