from flask import Flask, g, render_template, request, url_for, redirect
from note import Note
import datetime
'''
from os import environ
from flask_oidc import OpenIDConnect
from okta.client import Client as UsersClient
#Heroku database
import os
import psycopg2

import os


class Config(object):
    OIDC_CLIENT_SECRETS = "./openidconnect_secrets.json"
    OIDC_COOKIE_SECURE = False
    OIDC_CALLBACK_ROUTE = "/oidc/callback"
    OIDC_SCOPES = ["openid", "email", "profile"]
    OIDC_ID_TOKEN_COOKIE_NAME = "oidc_token"

DATABASE_URL = "postgres://yydekggijkpihj:75195cfed1455935c44a15fd86abae7726e6dcb54734eca16105c8983c635492@ec2-18-214-214-252.compute-1.amazonaws.com:5432/d63hvu45thv45v"

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
'''

global priority_level
global notes
priority_level = {"High":2, "Medium":1, "Low":0, None:0}
notes = []

app = Flask(__name__, static_folder='static')
'''
# instantiate OpenID client to handle user session
oidc = OpenIDConnect(app)
# Okta client will determine if a user has an appropriate account
okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
                          environ.get("OKTA_AUTH_TOKEN"))

@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None
'''
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
    current_note = 0
    if len(notes) == 0:
        notes.append(Note(data = new_note, priority = priority, tag = tag))
        return redirect(url_for("index"))
    else:
        while (priority_level[priority] < priority_level[notes[current_note].get_priority()]):
            print(priority, notes[current_note].get_priority())
            current_note += 1
        notes.insert(current_note, Note(data = new_note, priority = priority, tag = tag))
    return redirect(url_for("index"))

@app.route("/click/<int:idx>/", methods=["POST"])
def click(idx):
    #delete
    if request.form["submit_button"] == "Delete":
        print("Removing " + str(idx))
        if len(notes) > 0 :
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
