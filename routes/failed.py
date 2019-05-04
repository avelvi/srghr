from . import routes


@routes.route('/failed')
def failed():
    return 'Something went wrong'
