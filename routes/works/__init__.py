from flask import Blueprint, render_template

works_bp = Blueprint('works', __name__, url_prefix='/works')


@works_bp.route('/', endpoint='index')
def index():
    return render_template('works.html')


from . import uppercase, circle, triangle, linked_list, shuntingyard, queue_deque
from .shuntingyard import shuntingyard_bp, shunting_yard_bp
from .queue_deque import queue_bp
