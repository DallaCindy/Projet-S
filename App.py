from flask import Flask, make_response, render_template, request
from weasyprint import HTML
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

    core = Core(informations)
    regle50_30_20 = core.regle50_30_20()
    regle75_15_10 = core.regle75_15_10()
    personnaliser = core.personnaliser()
    return render_template('apercu.html',
        informations=informations,
        resultat=regle50_30_20,
        resultat2=regle75_15_10,
        resultat3=personnaliser
    )

@app.route('/pdf')
def pdf():

    informations = {
        "alimentation": request.args.get('alimentation'),
        "epargnes": request.args.get('epargnes'),
        "logement": request.args.get('logement'),
        "priorites_logement": request.args.get('priorites_logement'),
        "priorites_sante": request.args.get('priorites_sante'),
        "sante": request.args.get('sante'),
        "transport": request.args.get('transport'),
        "user_age": request.args.get('user_age'),
        "user_name": request.args.get('user_name'),
        "user_old_alimentation": request.args.get('user_old_alimentation'),
        "user_old_epargnes": request.args.get('user_old_epargnes'),
        "user_old_logement": request.args.get('user_old_logement'),
        "user_old_sante": request.args.get('user_old_sante'),
        "user_old_transport": request.args.get('user_old_transport'),
        "user_revenue": request.args.get('user_revenue')
    }

    core = Core(informations)
    regle50_30_20 = core.regle50_30_20()
    regle75_15_10 = core.regle75_15_10()
    personnaliser = core.personnaliser()

    html = render_template('apercu.html',
        informations=informations,
        resultat=regle50_30_20,
        resultat2=regle75_15_10,
        resultat3=personnaliser
    )

    pdf = HTML(string=html).write_pdf()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response


if __name__ == '__main__':
    app.run(debug=True)