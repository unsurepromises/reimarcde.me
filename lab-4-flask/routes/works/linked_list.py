from flask import render_template, request
from models.linked_list import linked_list
from . import works_bp


@works_bp.route('/linkedlist', methods=['GET', 'POST'])
def linked_list_view():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            val = request.form.get('node_value', '').strip()
            if val:
                linked_list.append(val)
        elif action == 'delete':
            val = request.form.get('delete_value', '').strip()
            if val:
                found = linked_list.delete(val)
                if not found:
                    message = f"Node '{val}' not found in the list."
        elif action == 'clear':
            linked_list.clear()
    return render_template('linkedlist.html', nodes=linked_list.to_list(), message=message)
