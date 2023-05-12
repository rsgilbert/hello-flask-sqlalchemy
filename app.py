from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'
db.init_app(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)

with app.app_context():
    db.create_all()


@app.route("/employees")
def employee_list():
    emp = Employee(name="Jonathan", email="Matthew@m.co")
    db.session.add(emp)
    db.session.commit()
    # bugs below!
    # employees = db.session.execute(db.select(Employee)).scalars()
    # print(employees)
    # return employees


# not a good idea
app.run(port=4000)
