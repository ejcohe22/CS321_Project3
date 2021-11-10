# Flask 
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# Helper File
import datetime
from src.note import Note
import os


global priority_level
priority_level = {"High":2, "Medium":1, "Low":0, None:0}

app = Flask(__name__, static_folder='static')
env = ''
if env == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.PickleType, nullable=False)


s = Todo(notes = [])
db.session.add(s)
db.session.commit()

@app.route("/")
def index():
    user = {'username' : 'Aidan' }
    time = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
    time = time.strftime("%B %d, %Y %I:%M %p")
    todo = db.session.query(Todo).first()
    return render_template("base.html", title="home", user=user, notes = todo.notes, time = time)

@app.route("/add", methods=["POST"])
def add():
    new_note = request.form.get("Note")
    priority = request.form.get("Priority")
    tag = request.form.get("Tag")
    current_note = 0
    todo = db.session.query(Todo).first()
    notes = todo.notes
    if len(notes) == 0:
        notes.append(Note(data = new_note, priority = priority, tag = tag))
        db.session.query(Todo).delete()
        db.session.add(Todo(notes = notes))
        db.session.commit()
        return redirect(url_for("index"))
    else:
        while current_note < len(notes) and (priority_level[priority] < priority_level[notes[current_note].get_priority()]):
            current_note += 1
        notes.insert(current_note, Note(data = new_note, priority = priority, tag = tag))
        db.session.query(Todo).delete()
        db.session.add(Todo(notes = notes))
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/click/<int:idx>/", methods=["POST"])

def click(idx):
    todo = db.session.query(Todo).first()
    notes = todo.notes
    #delete
    if request.form["submit_button"] == "Delete" and idx < len(notes) and idx >= 0 and len(notes) >= 1:
        print("Removing " + str(idx))
        notes.pop(idx)
        db.session.query(Todo).delete()
        db.session.add(Todo(notes = notes))
        db.session.commit()
        return redirect(url_for("index"))
    #status
    elif request.form["submit_button"] == "Done" and idx < len(notes) and idx >= 0 and len(notes) >= 1:
        print("changing status " + str(idx))
        notes[idx].set_status(not notes[idx].get_status())
        db.session.query(Todo).delete()
        db.session.add(Todo(notes = notes))
        db.session.commit()
        return redirect(url_for("index"))
    else:
        db.session.commit()
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
