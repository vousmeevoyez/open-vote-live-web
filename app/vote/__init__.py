from flask import Blueprint

blueprint = Blueprint(
    'vote_blueprint',
    __name__,
    url_prefix='/',
    template_folder='templates',
)
