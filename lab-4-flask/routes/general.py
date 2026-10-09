from flask import Blueprint, render_template

general_bp = Blueprint('general', __name__)


@general_bp.route('/')
def home():
    return render_template('index.html')


@general_bp.route('/profile')
def profile():
    return render_template('profile.html')


@general_bp.route('/contact')
def contact():
    return render_template('contact.html')


@general_bp.route('/works')
def works():
    return render_template('works.html')
