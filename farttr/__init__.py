import flask_login
import flask
import pathlib
import os.path
import sys
from flask import Flask, render_template, request, abort

import farttr.forms as forms

ALLOWED_MODULES = ("js-cookie",)


def node_modules_path():
    self_path = pathlib.PurePath(sys.modules[__name__].__file__)
    self_dir = self_path.parent
    return self_dir / "node_modules/"


NODE_MODULES_PATH = node_modules_path()

app = Flask(__name__)
app.secret_key = b"G#Z\x17\x8b\xb4\x8b\xe9\x89c\xdb\x1b%2\xbdy\x84\xe9'\x11L\xf6*\xb0\xf1\xf9aM\xd7\xc6\xc5\xff"
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(id):
    return None


@app.route("/", methods=("GET",))
def index():
    return render_template("index.html")


@app.get("/static/node_modules/<path:path>")
def node_modules(path):
    if path.split("/")[0] not in ALLOWED_MODULES:
        abort(401)
    return flask.send_from_directory("./static/node_modules/", path)


@app.route(
    "/join",
    methods=(
        "GET",
        "POST",
    ),
)
def join():
    form = forms.JoinForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        return request.form.to_dict()
    return render_template("join.html", form=form)


@app.post("/fart")
def fart():
    return render_template("fart.html")
