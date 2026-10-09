from flask import Flask
from routes.general import general_bp
from routes.works import works_bp

app = Flask(__name__)

app.register_blueprint(general_bp)
app.register_blueprint(works_bp)

if __name__ == '__main__':
    app.run(debug=True)
