from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def App() :
    return render_template('Acceuil.html')

@app.route("/apercu")
def Apercu() :

    logement = request.get('logement')
    return render_template('Apercu.html')