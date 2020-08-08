from .. import app
from flask import render_template, url_for

# SPA Template 페이지
@app.route("/")
def home():
  return render_template("index.html")

# SPA Virtual Router 대응 (FailBack Route를 index.html로 설정)
@app.errorhandler(404)
def failback():
  home()
