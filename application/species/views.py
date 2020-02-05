from application import app, db
from flask_login import login_required
from flask import redirect, render_template, request, url_for
from application.species.models import Species
from application.species.forms import SpeciesForm

@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new")
@login_required
def species_form():
    return render_template("species/new.html", form = SpeciesForm())

@app.route("/species/", methods=["POST"])
@login_required
def species_create():
    form = SpeciesForm(request.form)

    if not form.validate():
        return render_template("species/new.html", form = form)

    s = Species(form.name.data)

    s.description = form.description.data
    s.category = form.category.data
    db.session().add(s)
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/<species_id>/", methods=["GET"])
def species_profile(species_id):
    return render_template("species/profile.html", species = Species.query.get(species_id))

@app.route("/species/<species_id>/edit/", methods=["GET"]) 
@login_required
def species_edit(species_id):
    return render_template("species/edit.html", species = Species.query.get(species_id))   

@app.route("/species/<species_id>/", methods=["POST"])
@login_required
def species_edit_form(species_id):

    s = Species.query.get(species_id)
    s.name = request.form.get("name")
    s.description = request.form.get("description") 
    s.category = request.form.get("category")

    db.session().commit()

    return redirect(url_for("species_index"))


@app.route("/species/<species_id>/delete", methods=["POST"])
@login_required
def species_delete(species_id):
    s = Species.query.get(species_id)
    db.session.delete(s)
    db.session.commit()

    return redirect(url_for("species_index"))

