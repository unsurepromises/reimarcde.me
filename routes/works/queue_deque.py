from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models.queue_deque import LinkedDeque, LinkedQueue

queue_bp = Blueprint('queue', __name__, url_prefix="/works/queue-deque")

@queue_bp.route("/", methods=["GET", "POST"])
def index():
    if 'queue' not in session:
        session['queue'] = []
    if 'deque' not in session:
        session['deque'] = []

    if request.method == "POST":
        action = request.form.get("action")

        # queue actions
        if action == "enqueue":
            value = request.form.get("value", "").strip()
            if value:
                q = LinkedQueue()
                for item in session['queue']:
                    q.enqueue(item)
                q.enqueue(value)
                session['queue'] = q.to_list()
                flash(f"Enqueued: {value}", "success")
            else:
                flash("Please provide a value to enqueue.", "error")

        elif action == "dequeue":
            q = LinkedQueue()
            for item in session['queue']:
                q.enqueue(item)
            try:
                removed = q.dequeue()
                session['queue'] = q.to_list()
                flash(f"Dequeued: {removed}", "success")
            except (IndexError, Exception):
                flash("Queue is empty. Cannot dequeue.", "error")

        # deque actions
        elif action == "add_front":
            value = (request.form.get("value_front") or request.form.get("value") or "").strip()
            if value:
                dq = LinkedDeque()
                for item in session['deque']:
                    dq.add_rear(item)
                dq.add_front(value)
                session['deque'] = dq.to_list()
                flash(f"Added to front: {value}", "success")
            else:
                flash("Please provide a value to add to the front.", "error")

        elif action == "add_rear":
            value = (request.form.get("value_rear") or request.form.get("value") or "").strip()
            if value:
                dq = LinkedDeque()
                for item in session['deque']:
                    dq.add_rear(item)
                dq.add_rear(value)
                session['deque'] = dq.to_list()
                flash(f"Added to rear: {value}", "success")
            else:
                flash("Please provide a value to add to the rear.", "error")

        elif action == "remove_front":
            dq = LinkedDeque()
            for item in session['deque']:
                dq.add_rear(item)
            try:
                removed = dq.remove_front()
                session['deque'] = dq.to_list()
                flash(f"Removed from front: {removed}", "success")
            except (IndexError, Exception):
                flash("Deque is empty. Cannot remove from front.", "error")

        elif action == "remove_rear":
            dq = LinkedDeque()
            for item in session['deque']:
                dq.add_rear(item)
            try:
                removed = dq.remove_rear()
                session['deque'] = dq.to_list()
                flash(f"Removed from rear: {removed}", "success")
            except (IndexError, Exception):
                flash("Deque is empty. Cannot remove from rear.", "error")

        # reset
        elif action == "clear_queue":
            session['queue'] = []
            flash("Queue cleared.", "info")

        elif action == "clear_deque":
            session['deque'] = []
            flash("Deque cleared.", "info")

        return redirect(url_for('queue.index'))

    return render_template(
        "queue_deque.html",
        queue=session['queue'],
        deque=session['deque']
    )
