from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint('auth', __name__)  # call same as variable is good practice


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    snap_email = r".*@snapfinance.co.uk"
    correct_password = "computer_password"
    correct_email = "snap@snapfinance.co.uk"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not re.match(snap_email, email):
            flash("You must login using your Snap Finance UK email address.", category="error")
        elif email != correct_email:
            flash("The email address is incorrect.", category="error")
        elif password != correct_password:
            flash("The password is incorrect.", category="error")
        else:
            flash('Login successful!', category="success")
    return render_template("login.html")


# return render_template("login.html", text="Testing", user="Phoebe", boolean=True)


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 2 characters.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            flash('Account created!', category="success")
    return render_template("sign_up.html")
