import atexit
import logging
import logging.config
import os
import yaml
from flask import Flask, jsonify
from flask_restful import Api
from http import HTTPStatus
from simple import endpoints


def handle_error(logger, error):
    logger.error("Application Error: {0}".format(error))
    return jsonify(error), HTTPStatus.INTERNAL_SERVER_ERROR


def handle_exception(logger, exception):
    logger.exception("Application Exception: {0}".format(exception))
    return jsonify(exception.args), HTTPStatus.INTERNAL_SERVER_ERROR


def create_app(test_config=None):
    with open("logging.yml", "r") as configuration_file:
        log_configuration = yaml.safe_load(configuration_file)
        logging.config.dictConfig(log_configuration)
        logger = logging.getLogger(__name__)

    logger.info("Starting application")

    atexit.register(lambda: logger.info("Stopping application"))

    app = Flask(__name__, instance_relative_config=True)

    app.register_error_handler(
        HTTPStatus.INTERNAL_SERVER_ERROR,
        lambda error: handle_error(logger, error))
    app.register_error_handler(
        Exception,
        lambda exception: handle_exception(logger, exception))

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app)
    api.add_resource(endpoints.PingEndpoint, "/ping")
    api.add_resource(endpoints.FaultEndpoint, "/fault")
    api.add_resource(endpoints.RareFaultEndpoint, "/rarefault")

    return app
