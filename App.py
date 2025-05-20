from flask import Flask, render_template, request
from Core import Core

app = Flask(__name__)

@app.route("/")
def accueil() :
    return render_template('accueil.html')

@app.route("/apercu", methods=['POST'])
def apercu() :

    informations = {}
    data = request.form
    for key, value in data.items():
        informations[key] = value

    print(informations)
    core = Core(informations)
    regle50_30_20 = core.regle50_30_20()
    regle75_15_10 = core.regle75_15_10()
    personnaliser = core.personnaliser()

    print(regle50_30_20)
    print(regle75_15_10)
    print(personnaliser)

    print(informations)

    return render_template('apercu.html',
        informations=informations,
        resultat=regle50_30_20,
        resultat2=regle75_15_10,
        resultat3=personnaliser
    )