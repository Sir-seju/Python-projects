from flask import render_template, Blueprint, jsonify, request
from flask.templating import render_template_string
main = Blueprint('main', __name__)

WORDS = []
with open("words.txt", "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())
    

@main.route("/")
@main.route("/home")
def home():    
    return render_template("index.html")

@main.route("/search")
def search():
    q = request.args.get("q")
    words = [word for word in WORDS if q and word.startswith(q)]
    return render_template("search.html", words=words)