from flask import render_template, request
from . import works_bp


@works_bp.route('/area/triangle', methods=['GET', 'POST'])
def area_triangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        result = 0.5 * base * height
    return render_template('triangle.html', result=result)
