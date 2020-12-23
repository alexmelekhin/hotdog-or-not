from flask import Blueprint, request, jsonify
from cnn_model.predict import make_prediction
from cnn_model import __version__ as model_version

from web_api import __version__ as api_version
from web_api.config import get_logger

import json


_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status ok')
        return 'ok'

