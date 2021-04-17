import os

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True


@app.route("/")
def landing():
    """ Landing Page """

    rate = ["$ ##","$ ##","$ ##","$ ##","$ ##","$ ##","$ ##","$ ##","$ ##"]

    return render_template("index.html", rate=rate)
