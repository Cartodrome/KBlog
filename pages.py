from flask import Flask, render_template

from utils import get_logger
from collections import OrderedDict

app = Flask(__name__)
log = get_logger("pages")


@app.route("/")
def home_page():
    archives = OrderedDict({
        "January": ["I've got a fabulous winter coat", "It was my Birthday!"],
        "February": ["Valentines Favourites", "My Favourite Apres Ski"],
        "March": ["What to buy your boy friend for his Birthday", "Spring treats"],
        "April": ["Favourite Summer outfits", "It's all about yellow in April."],
        })
    active_archives = ["February"]
    return render_template("home2.html",
                           archives=archives,
                           active_archives=active_archives)

@app.route("/cover")
def cover_page():
    return render_template("cover.html")

@app.route("/test")
def test_page():
    return render_template("test.html")
    
@app.route("/test2")
def test_page2():
    return render_template("test2.html")