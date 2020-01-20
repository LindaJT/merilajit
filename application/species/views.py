from application import app, db
from flask import redirect, render_template, request, url_for
from application.species.models import Species

@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new")
def species_form():
    return render_template("species/new.html")

@app.route("/species/", methods=["POST"])
def species_create():
    name = request.form.get("name")
    cat = request.form.get("category")
    des = request.form.get("description")
    s = Species(name)
    s.description = des
    s.category = cat
    db.session().add(s)
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/<species_id>/", methods=["GET"])
def species_profile(species_id):
    return render_template("species/profile.html", species = Species.query.get(species_id))

@app.route("/species/<species_id>/edit/", methods=["GET"]) 
def species_edit(species_id):
    return render_template("species/edit.html", species = Species.query.get(species_id))   

@app.route("/species/<species_id>/", methods=["POST"])
def species_edit_form(species_id):

    s = Species.query.get(species_id)
    s.name = request.form.get("name")
    s.description = request.form.get("description") 
    s.category = request.form.get("category")

    db.session().commit()

    return redirect(url_for("species_index"))
