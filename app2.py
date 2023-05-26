from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ancestry.sqlite'

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app

# reflection - can only read data

ancestry = db.Table("ancestry", db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
def table():
    results = db.session.query(ancestry).all()
    for r in results:
        print(r.Name)


    return ''