from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  complete = db.Column(db.Boolean)

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
  name = request.form.get('name')
  new_task = Todo(name=name, complete=False)
  db.session.add(new_task)
  db.session.commit()

if __name__ == "__main__":
  with app.app_context():
    db.create_all()

    new_todo = Todo(title='hey', complete=False)
    db.session.add(new_todo)
    db.session.commit()

  app.run(debug=True)
