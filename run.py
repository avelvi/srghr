from flask import Flask
from routes import *
from core.config import Config
from core.auth_service import AuthService
from core.logger import logger

config = Config()
config.parse()

auth_service = AuthService()

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    host = config.get('app.host')
    port = config.get('app.port')

    logger.info('Starting application')
    app.run(host=host, port=port)
