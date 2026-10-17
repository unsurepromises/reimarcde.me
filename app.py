import os
from flask import Flask
from routes.general import general_bp
from routes.works import works_bp
from routes.works.shuntingyard import shuntingyard_bp
from routes.works.queue_deque import queue_bp

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-queue-deque')

app.register_blueprint(general_bp)
app.register_blueprint(works_bp)
app.register_blueprint(shuntingyard_bp)
app.register_blueprint(queue_bp)

if __name__ == '__main__':
    app.run(debug=True)
