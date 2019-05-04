from . import routes
from flask import redirect
from run import auth_service


@routes.route('/')
def index():
    authorization_url = auth_service.authorization_url()
    return redirect(authorization_url)

