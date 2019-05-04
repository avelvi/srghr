from . import routes


@routes.route('/success')
def success():
    return 'The repository was copied'
