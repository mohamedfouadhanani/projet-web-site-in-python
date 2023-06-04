from flask import Blueprint, render_template, request

conversion_rate = 1.03 

yen_blueprint = Blueprint("yen", __name__)

@yen_blueprint.route("/", methods=["GET"])
def get_yen():
    return render_template("form.html", title="Money Converter | Convert to Yen", url="/yen", currency="Yen", value=0)

@yen_blueprint.route("/", methods=["POST"])
def post_yen():
    amount = float(request.form["amount_dz"])
    value = conversion_rate * amount
    
    return render_template("form.html", title="Money Converter | Convert to Yen", url="/yen", currency="Yen", value=value)