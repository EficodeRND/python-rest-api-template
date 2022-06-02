from flask_restx import Namespace, Resource

ns = Namespace('', description='Status reporting')


@ns.route('/')
class StatusController(Resource):

    @ns.response(200, 'OK')
    def get(self):  # pylint: disable=no-self-use
        return "OK", 200
