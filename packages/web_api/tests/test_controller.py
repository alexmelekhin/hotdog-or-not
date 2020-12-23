import json

from cnn_model import config as model_config
from cnn_model import __version__ as model_version

from web_api import __version__ as api_version


def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200

