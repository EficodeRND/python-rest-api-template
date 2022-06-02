import logging as log

from flask_restx import Api
from flask_swagger_ui import get_swaggerui_blueprint

api = Api(version='1.0', title='Python REST API',
          description='Template for building Python REST APIs')


@api.errorhandler
def default_error_handler(_):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500


def init(app):
    # app.config['SERVER_NAME'] = server_name + ':' + str(cfg.get('port', 5000))
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['ERROR_404_HELP'] = False

    api_root = ''
    swagger_url = f"{api_root}/api/docs"  # URL for exposing Swagger UI (without trailing '/')
    log.debug("Registering swagger ui: {}".format(swagger_url))
    api_url = f"{api_root}/swagger.json"  # Our API url (can of course be a local resource)
    log.debug("Registering swagger api: %s", api_url)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        api_url,
        config={  # Swagger UI config overrides
            'app_name': "Python REST API"
        }
    )

    # Register blueprint at URL
    # (URL must match the one given to factory function above)
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)
