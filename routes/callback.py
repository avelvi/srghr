from . import routes
from run import auth_service
from flask import redirect, request
from run import config


@routes.route('/auth/callback')
def auth_callback():
    code = request.args.get('code')
    if code is not None:
        token_dict = auth_service.fetch_token(code)
        config.get_cache()[code] = token_dict
        return redirect('/replicate/%s' % code)
    else:
        return redirect('/failed')
