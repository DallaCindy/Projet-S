from flask import Flask, render_template, request

app = Flask(__name__)



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

    informations = {}
    data = request.form
    for key, value in data.items():
        informations[key] = value

    # calcul(informations)
    print(informations)
    return render_template('Apercu.html')