from flask import Flask, render_template,request,redirect,url_for
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
  return redirect(url_for('home'))

@app.route('/update/<int:id>')
def update(id):
  todo=Todo.query.get(id)
  todo.complete=not todo.complete
  db.session.commit()
  return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
  todo=Todo.query.get(id)
  db.session.delete(todo)
  db.session.commit()
  return redirect(url_for('home'))

if __name__ == "__main__":

  app.run(debug=True)
