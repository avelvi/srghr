from flask import Blueprint

routes = Blueprint('routes', __name__)


from .callback import *
from .failed import *
from .index import *
from .replicate import *
from .success import *

