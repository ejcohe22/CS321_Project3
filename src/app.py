from flask import Flask, render_template, request, url_for, redirect
from src.note import Note
import datetime


notes = []


app = Flask(__name__)
@app.route("/")
def index():
    user = {'username' : 'Aidan' }
    return render_template("base.html", title="home", user=user, notes = notes, timeObj = datetime.datetime)


@app.route("/add", methods=["POST"])
def add():
    new_note = request.form.get("Note")
    priority = request.form.get("Priority")
    notes.append(Note(data = new_note, priority = priority, tag = None))
    
    print(notes[-1].get_data())
    return redirect(url_for("index"))

@app.route("/delete/<int:idx>/", methods=["POST"])

def delete(idx):
    print("Removing" + str(idx))
    notes.pop(idx)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
