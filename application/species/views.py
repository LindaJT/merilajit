from application import app, db, login_required
from flask_login import current_user
from flask import redirect, render_template, request, url_for
from application.species.models import Species
from application.species.forms import SpeciesForm
from application.obs.models import Observation
from application.obs.forms import ObsForm
from application.auth.models import User
from application.region.models import Region

@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all(), regions = Region.query.all())

@app.route("/species/select/", methods=["POST"])
def species_select():
    region_name = request.form.get("region")
    if region_name == "Kaikki":
        species = Species.query.all()
    else:
        region = Region.query.filter_by(name=region_name).first()
        species = Region.query.get(region.id).regionspecies

    return render_template("species/list.html", species = species, regions = Region.query.all())

@app.route("/species/new")
@login_required
def species_form():
    return render_template("species/new.html", form = SpeciesForm(), regions = Region.query.all())

@app.route("/species/", methods=["POST"])
@login_required(role="ADMIN")
def species_create():
    form = SpeciesForm(request.form)

    if not form.validate():
        return render_template("species/new.html", form = form)

    species = Species(form.name.data)

    species.description = form.description.data
    species.category = form.category.data
    regions = request.form.getlist('my_checkbox')
    for id in regions:
        reg = Region.query.get(id)
        reg.regionspecies.append(species)
    
    db.session().add(species)
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/<species_id>/", methods=["GET"])
def species_profile(species_id):
    species = Species.query.get(species_id)
    regions = Region.query.with_parent(species)
    return render_template("species/profile.html", species = species, regions = regions )

@app.route("/species/<species_id>/edit/", methods=["GET"]) 
@login_required(role="ADMIN")
def species_edit(species_id):
    return render_template("species/edit.html", species = Species.query.get(species_id), regions = Region.query.all(), form = SpeciesForm())   

@app.route("/species/<species_id>/", methods=["POST"])
@login_required(role="ADMIN")
def species_edit_form(species_id):

    form = SpeciesForm(request.form)

    if not form.validate():
        return render_template("species/edit.html", form = form)

    species = Species.query.get(species_id)
    all_regions = Region.query.all()
    
    for reg in all_regions:
        if species in reg.regionspecies:
            reg.regionspecies.clear()
    
    species.name = form.name.data
    species.description = form.description.data
    species.category = form.category.data
    regions = request.form.getlist('my_checkbox')
    
    for id in regions:
        reg = Region.query.get(id)
        reg.regionspecies.append(species)

    db.session().commit()

    return redirect(url_for("species_index"))


@app.route("/species/<species_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def species_delete(species_id):
    species = Species.query.get(species_id)

    db.session.delete(species)
    db.session.commit()

    return redirect(url_for("species_index"))

