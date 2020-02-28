from application import app, db, login_required
from flask_login import current_user
from flask import redirect, render_template, request, url_for
from application.region.models import Region
from application.region.forms import RegionForm
from application.obs.models import Observation
from application.obs.forms import ObsForm
from application.auth.models import User

@app.route("/region/new")
@login_required(role="ADMIN")
def region_form():
    return render_template("region/new.html", form = RegionForm())

@app.route("/region/", methods=["POST"])
@login_required(role="ADMIN")
def region_create():
    form = RegionForm(request.form)

    if not form.validate():
        return render_template("region/new.html", form = form)

    reg = Region(form.name.data)

    reg.description = form.description.data
    db.session().add(reg)
    db.session().commit()

    user_id = current_user.id

    return redirect(url_for("user_profile", user_id = user_id))

@app.route("/region/<region_id>/", methods=["GET"])
def region_profile(region_id):
    return render_template("region/profile.html", region = Region.query.get(region_id))

@app.route("/region/<region_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def region_delete(region_id):
    reg = Region.query.get(region_id)

    db.session.delete(reg)
    db.session.commit()

    return redirect(url_for("species_index"))