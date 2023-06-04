from flask import Blueprint, render_template, request

conversion_rate = 0.0073

usd_blueprint = Blueprint("usd", __name__)

@usd_blueprint.route("/", methods=["GET"])
def get_usd():
    return render_template("form.html", title="Money Converter | Convert to US Dollars", url="/usd", currency="US Dollars", value=0)

@usd_blueprint.route("/", methods=["POST"])
def post_usd():
    amount = float(request.form["amount_dz"])
    value = conversion_rate * amount
    
    return render_template("form.html", title="Money Converter | Convert to US Dollars", url="/usd", currency="US Dollars", value=value)