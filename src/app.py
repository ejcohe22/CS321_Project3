from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
@app.route("/")
def index():
    user = {'username' : 'Aidan' }
    return render_template("base.html", title="home", user=user)

notes = []

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("Note")
    notes.append(note)
    print(notes[-1])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
