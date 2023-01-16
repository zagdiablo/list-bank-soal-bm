from flask import Blueprint, redirect, render_template


views = Blueprint("views", __name__)


@views.route("/")
def kelas_page():
    return render_template("index.html")
