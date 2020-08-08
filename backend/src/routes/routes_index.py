from .. import app
from flask import render_template, url_for

# SPA Template 페이지
@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def home(path):
  return render_template("index.html")
