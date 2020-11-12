from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Azure web app using python ... agp.sat.gob.mx"
