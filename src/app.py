# Flask 
from flask import Flask, render_template, request, url_for, redirect
# Helper File
import datetime
from src.note import Note
from src.notes import Notes


priority_level = {"High":2, "Medium":1, "Low":0, None:0}
notes = Notes()
app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    user = {'username' : 'Aidan' }
    time = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
    time = time.strftime("%B %d, %Y %I:%M %p")
    # print("note size: ", len(notes))
    return render_template("base.html", title="home", user=user, notes = notes.get_all(), time = time)


@app.route("/add", methods=["POST"])
def add():
    new_note = request.form.get("Note")
    priority = request.form.get("Priority")
    tag = request.form.get("Tag")
    current_note = 0
    if notes.get_size() == 0:
        # notes.append(Note(data = new_note, priority = priority, tag = tag))
        notes.add(Note(data = new_note, priority = priority, tag = tag))
        return redirect(url_for("index"))
    else:
        while current_note < notes.get_size() and (priority_level[priority] < priority_level[notes.get_one(current_note).get_priority()]):
            current_note += 1
        notes.insert(current_note, Note(data = new_note, priority = priority, tag = tag))
    return redirect(url_for("index"))

@app.route("/click/<int:idx>/", methods=["POST"])

def click(idx):
    #delete
    if request.form["submit_button"] == "Delete" and idx > len(notes) and idx >= 0 and len(notes) >= 1:
        print("Removing " + str(idx))
        notes.remove(idx)
        return redirect(url_for("index"))
    #status
    elif request.form["submit_button"] == "Done" and idx > len(notes) and idx >= 0 and len(notes) >= 1:
        print("changing status " + str(idx))
        notes.get_one(idx).set_status(not notes.get_one(idx).get_status())
        notes.add(notes.get_one(idx))
        notes.remove(idx)

        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
