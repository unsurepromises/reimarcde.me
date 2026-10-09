from flask import render_template, request
from . import works_bp


@works_bp.route('/area/circle', methods=['GET', 'POST'])
def area_circle():
    result = None
    if request.method == 'POST':
        r = float(request.form.get('radius', 0))
        result = 3.14159 * (r ** 2)
    return render_template('circle.html', result=result)
