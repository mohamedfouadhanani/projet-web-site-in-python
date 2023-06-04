from flask import Flask, render_template

from routes.usd import usd_blueprint
from routes.yen import yen_blueprint

app = Flask(__name__)

app.register_blueprint(usd_blueprint, url_prefix="/usd")
app.register_blueprint(yen_blueprint, url_prefix="/yen")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Money Converter")

if __name__ == "__main__":
    app.run(debug=True)