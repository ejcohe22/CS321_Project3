from flask import Flask, render_template, request, url_for, redirect
from note import Note
import datetime


notes = []

app = Flask(__name__, static_folder='static')
@app.route("/")
def index():
    user = {'username' : 'Aidan' }
    time = datetime.datetime.now()
    time = time.strftime("%B %d, %Y %I:%M %p")
    return render_template("base.html", title="home", user=user, notes = notes, time = time, audio_file="Pagodes.mp3")


@app.route("/add", methods=["POST"])
def add():
    new_note = request.form.get("Note")
    priority = request.form.get("Priority")
    tag = request.form.get("Tag")
    notes.append(Note(data = new_note, priority = priority, tag = tag))

    med_idx = 0
    low_idx = 0
    for i in range(len(notes)):
        if notes[i].get_priority() == "High":
            notes[0], notes[i]= notes[i], notes[0]
            med_idx += 1
            low_idx += 1
        elif notes[i].get_priority() == "Medium":
            notes[med_idx], notes[i]= notes[i], notes[med_idx]
            low_idx += 1
        else:
            notes[low_idx], notes[i]= notes[i], notes[low_idx]
    print(notes)
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
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
