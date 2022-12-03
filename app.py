from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200))
  complete = db.Column(db.Boolean)

@app.route("/")
def hello_world():
    return render_template('base.html')

if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)
