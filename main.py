from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soft.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    is_deleted = db.Column(db.Boolean, default=False)

    @staticmethod
    def get_active():
        return Item.query.filter_by(is_deleted=False)

with app.app_context():
    db.create_all()

    i1 = Item(name="Book")
    i2 = Item(name="Pen")

    db.session.add_all([i1, i2])
    db.session.commit()

    # delete (soft)
    i1.is_deleted = True
    db.session.commit()

    active_items = Item.get_active().all()
    for i in active_items:
        print(i.name)
