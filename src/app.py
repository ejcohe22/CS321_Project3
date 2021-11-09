# Flask + DB
from flask import Flask, render_template, request, url_for, redirect
# Helper File
from src.note import * # Note, OS, datetime, timezone

global priority_level
global notes
priority_level = {"High":2, "Medium":1, "Low":0, None:0}
notes = [] 

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    user = {'username' : 'Aidan' }
    time = datetime.now(timezone('US/Eastern'))
    time = time.strftime("%B %d, %Y %I:%M %p")
    print("note size: ", len(notes))
    return render_template("base.html", title="home", user=user, notes = notes, time = time)


@app.route("/add", methods=["POST"])
def add():
    
    new_note = request.form.get("Note")
    priority = request.form.get("Priority")
    tag = request.form.get("Tag")
    current_note = 0
    if len(notes) == 0:
        notes.append(Note(data = new_note, priority = priority, tag = tag))
        return redirect(url_for("index"))
    else:
        while current_note < len(notes) and (priority_level[priority] < priority_level[notes[current_note].get_priority()]):
            current_note += 1
        notes.insert(current_note, Note(data = new_note, priority = priority, tag = tag))
    return redirect(url_for("index"))

@app.route("/click/<int:idx>/", methods=["POST"])

def click(idx):
    #delete
    if request.form["submit_button"] == "Delete":
        print("Removing " + str(idx))
        notes.pop(idx)
        return redirect(url_for("index"))
    #status
    elif request.form["submit_button"] == "Done":
        print("changing status " + str(idx))
        notes[idx].set_status(not notes[idx].get_status())
        notes.append(notes[idx])
        notes.pop(idx)

        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
