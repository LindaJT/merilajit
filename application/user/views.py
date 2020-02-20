from application import app, db
from flask import redirect, render_template, request, url_for
from application.auth.models import User
from application.user.forms import UserForm
from application.species.models import Species
from application.obs.models import Observation
@app.route("/user/signin")
def user_form():
    return render_template("users/signin.html", form = UserForm())

@app.route("/user/", methods=["POST"])
def user_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("users/signin.html", form = form)
    
    name = form.name.data
    username = form.username.data
    password = form.password.data
    role = form.role.data

    print("!!!!!!!!!!!!!!!!!!" + role + "!!!!!!!!!!!!!!!!!1")

    user = User(name, username, password, role)

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/user/<user_id>/", methods=["GET"])
def user_page(user_id):
    return render_template("users/profile.html", user = User.query.get(user_id))