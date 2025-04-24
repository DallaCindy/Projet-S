from flask import Flask, render_template, request

from Core import Core

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


@app.route("/")
def App() :
    return render_template('Acceuil.html')

@app.route("/apercu", methods=['POST'])
def Apercu() :

    # user_name
    # user_age
    # user_revenue

    # logement
    # alimentation
    # transport
    # sante
    # epargnes

    # priorites_logement
    # priorites_alimentation
    # priorites_transport
    # priorites_sante
    # priorites_epargnes

    # user_old_logement
    # user_old_alimentation
    # user_old_transport
    # user_old_sante
    # user_old_epargnes

    informations = {}
    data = request.form
    for key, value in data.items():
        informations[key] = value

    print(informations)
    core = Core(informations)
    regle50_30_20 = core.regle50_30_20()
    print(regle50_30_20)

    return render_template('Apercu.html', resultat=regle50_30_20)