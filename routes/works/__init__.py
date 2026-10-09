from flask import Blueprint

works_bp = Blueprint('works', __name__, url_prefix='/works')

from . import uppercase, circle, triangle, linked_list
