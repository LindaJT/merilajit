from application import app, db, login_required, login_manager
from flask_login import current_user
from flask import redirect, render_template, request, url_for
from application.species.models import Species
from application.obs.models import Observation
from application.obs.forms import ObsForm
from datetime import *

@app.route("/observations", methods=["GET"])
def obs_index():
    return render_template("obs/list.html", obs = Observation.query.all())


@app.route("/observations/<obs_id>/edit", methods=["GET"])
@login_required
def obs_form(obs_id):
    return render_template("obs/edit.html", obs = Observation.query.get(obs_id), form = ObsForm())

@app.route("/species/<species_id>/newobs", methods=["POST"])
@login_required
def obs_create(species_id):
    
    obs = Observation("uusi")
    obs.account_id = current_user.id
    obs.species_id = species_id
    db.session().add(obs)
    db.session().commit()

    return redirect(url_for("obs_form", obs_id = obs.id))

@app.route("/observations/<obs_id>/editobs", methods=["POST"])
@login_required
def obs_edit(obs_id):
    obs = Observation.query.get(obs_id)
    if obs.account_id != current_user.id:
        return login_manager.unauthorized()
    form = ObsForm(request.form)
    if not form.validate():
        return render_template("obs/edit.html", obs = Observation.query.get(obs_id), form = form)

    obs.description = request.form.get("description")
    dfrom = request.form.get("date") 
    obs.date = datetime.strptime(dfrom, '%Y-%m-%d').date()
    obs.ncoordinates = request.form.get("ncoordinates")
    obs.ecoordinates = request.form.get("ecoordinates")


    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/observation/<obs_id>/delete", methods=["POST"])
@login_required
def obs_delete(obs_id):
    obs = Observation.query.get(obs_id)
    if obs.account_id != current_user.id:
        return login_manager.unauthorized()
    db.session.delete(obs)
    db.session.commit()

    return redirect(url_for("user_profile", user_id = current_user.id))