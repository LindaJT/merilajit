from application import app, db
from flask_login import login_required, current_user
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
    form = ObsForm(request.form)
    if not form.validate():
        return render_template("obs/edit.html", obs = Observation.query.get(obs_id), form = form)
    o = Observation.query.get(obs_id)
    o.description = request.form.get("description")
    dfrom = request.form.get("date") 
    o.date = datetime.strptime(dfrom, '%Y-%m-%d').date()
    o.ncoordinate = request.form.get("ncoordinate")
    o.ecoordinate = request.form.get("ecoordinate")


    db.session().commit()

    return redirect(url_for("species_index"))