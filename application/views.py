from flask import render_template
from application import app
from application.auth.models import User
from application.species.models import Species

@app.route("/")
def index():
    return render_template("index.html", obs_count_user = User.count_observations_by_user(), obs_count_species = Species.count_observations_by_species())
