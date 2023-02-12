from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String

app = Flask(__name__)
# TODO move elsewhere ?
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin@localhost:5432/main'

db = SQLAlchemy(app)


class Apartment(db.Model):
    __tablename__ = "apartments"

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(255), nullable=False)
    locality = db.Column(String(255))
    price = db.Column(Integer)
    image_url = db.Column(String(255))


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    apartments = Apartment.query.all()
    return render_template('index.html', apartments=apartments)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
