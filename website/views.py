# Storing standard routes for our website, aka pages user can anvigate to

from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # call same a s variable is good practice


# function will run whenever we go to url and type in / @symbole line is called a decorator
@views.route('/')
def home():
    return render_template("home.html")
