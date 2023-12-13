from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user_model import User
from flask_app.models.recipes_model import Recipe
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

# ? ========== LOGIN PAGE ==========


@app.route("/")
def show_form():

    return render_template("register_login.html")

@app.route("/users/register", methods=["post"])
def user_register():

    if not User.validate(request.form):
        return redirect("/")

    # hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': pw_hash
    }
    # Save the user in DB
    user_id = User.create(data)
    # store the user_id in session
    session["user_id"] = user_id
    return redirect("/recipes")
@app.route("/users/login", methods=["POST"])
def login():

    data = {
        "email": request.form["email"]
    }

    user_in_db = User.get_by_email(data)
    # if email not found
    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/")

    # check password hash
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid credentials", "log")
        return redirect("/")

    # All Good up to here
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.first_name
    return redirect("/recipes")
@app.route("/recipes")
def dash():

    #! route guard
    if 'user_id' not in session:
        return redirect("/")

    data = {
        "id":  session["user_id"]
    }
    logged_user = User.get_by_id(data)
    all_recip=Recipe.get_all()

    return render_template("dashboard.html", user=logged_user,recipes=all_recip)
@app.route("/logout")
def logout():

    # clear the session
    session.clear()
    return redirect("/")

