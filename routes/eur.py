from flask import Blueprint, render_template, request

conversion_rate = 0.0069

eur_blueprint = Blueprint("eur", __name__)

@eur_blueprint.route("/", methods=["GET"])
def get_eur():
    return render_template("form.html", title="Money Converter | Convert to EURO", url="/eur", currency="EURO", value=0)

@eur_blueprint.route("/", methods=["POST"])
def post_eur():
    amount = float(request.form["amount_dz"])
    value = conversion_rate * amount
    
    return render_template("form.html", title="Money Converter | Convert to EURO", url="/eur", currency="EURO", value=value)