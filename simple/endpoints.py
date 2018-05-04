import logging
from flask_restful import Resource

__all__ = ["PingEndpoint"]
logger = logging.getLogger(__name__)


class PingEndpoint(Resource):
    def get(self):
        logger.debug("Handled ping")
        return "pong"


class FaultEndpoint(Resource):
    def get(self):
        logger.warn("Incoming fault...")
        raise RuntimeError("Fault details")


class RareFaultEndpoint(Resource):
    def get(self):
        raise RuntimeError("A needle in a haystack")
