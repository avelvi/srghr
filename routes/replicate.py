from . import routes
from run import config
from flask import redirect
from run import auth_service
from core.logger import logger


@routes.route('/replicate/<code>')
def replicate(code):
    if code not in config.get_cache():
        logger.error('You are not authorized')
        return redirect('/failed')

    response = auth_service.forks(config.get_cache()[code])

    if response.status_code == 404:
        error_message = 'Repository not found.'
        logger.error(error_message)
        return error_message
    if not response.ok:
        logger.error('Response status code = %s' % response.status_code)
        return redirect('/failed')

    config.get_cache().pop(code)
    logger.info('Repository was copied successfully')
    return redirect('/success')
