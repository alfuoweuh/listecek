from flask import Flask, render_template, request
from datetime import datetime
from tinydb import TinyDB, Query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vyber', methods=['GET'])
def vyber():
    action = request.args.get('action')  # What button was pressed?
    if action == 'open':
        pass
    elif action == 'template':
        pass
    return render_template('vyber.html' , action=action)

@app.route('/listecek', methods=['GET', 'POST'])
def listecek():
    if request.method == 'GET': # Button on the welcome page was pressed
        action = request.args.get('action')  # What button was pressed?

        if action == 'template' or action == 'open':
            ## Here we would load existing data from the database
            # For demonstration, we use hardcoded data
            id = 1
            název_výpravy = "Nejen autodráha v klubovně"
            sraz_čas = "v sobotu 20. 9. v 10:00"
            sraz_místo = "v klubovně"
            rozchod_čas = "v neděli 21. 9. v 17:00"
            rozchod_místo = "tamtéž"

            s_sebou = "výbornou náladu, věci dle seznamu věcí na vícedenní výpravu na našich stránkách (půjdeme na výlet, starší budou venku i spát)"
            kdo_ma = ""
            jidlo = "dvě snídaně, dva obědy, jedna večeře; k volnému užití bude varná konvice a mikrovlnka, akorát sobotní oběd mladších / sobotní večeře a nedělní snídaně i oběd starších musí být studený"
            penize = "100 Kč; možná půjde dělat autíčka, to byste za něj zaplatili něco navíc; kolik, se ještě uvidí"
            poznamka = "Bude zima, tak se oblečte, jak vám je po chuti. Klidně můžete zmrznout, ale mrazák nechte doma."
            kontakty = [
                {"jmeno": "Vojta (starší)", "telefon": "739 287 724", "email": "vevebot123@gmail.com"},
                {"jmeno": "Myšák (mladší)", "telefon": "731 192 036", "email": "mysak@ctrnactka.cz"}
            ]
            data = {
                "id": id,
                "nazev_vypravy": název_výpravy,
                "sraz_cas": sraz_čas,
                "sraz_misto": sraz_místo,
                "rozchod_cas": rozchod_čas,
                "rozchod_misto": rozchod_místo,
                "s_sebou": s_sebou,
                "kdo_ma": kdo_ma,
                "jidlo": jidlo,
                "penize": penize,
                "poznamka": poznamka,
                "kontakty": kontakty,
            }
        
        elif action == 'new':
            data = {"kontakty": []}

        return render_template('listecek.html', action=action, current_year=datetime.now().year, **data)
    
    elif request.method == 'POST': # Form was submitted
        data = {
            "nazev_vypravy": request.form.get('nazev_vypravy', ''),
            "sraz_cas": request.form.get('sraz_cas', ''),
            "sraz_misto": request.form.get('sraz_misto', ''),
            "rozchod_cas": request.form.get('rozchod_cas', ''),
            "rozchod_misto": request.form.get('rozchod_misto', ''),
            "s_sebou": request.form.get('s_sebou', ''),
            "kdo_ma": request.form.get('kdo_ma', ''),
            "jidlo": request.form.get('jidlo', ''),
            "penize": request.form.get('penize', ''),
            "poznamka": request.form.get('poznamka', ''),

            "kontakty": []
        }
        for i in range(3):
            jmeno = request.form.get(f'kontakt_jmeno_{i}', '').strip()
            telefon = request.form.get(f'kontakt_telefon_{i}', '').strip()
            email = request.form.get(f'kontakt_email_{i}', '').strip()
            if jmeno or telefon or email:
                data["kontakty"].append({"jmeno": jmeno, "telefon": telefon, "email": email})

        return render_template('listecek.html', action='edit', current_year=datetime.now().year, **data)

if __name__ == '__main__':
    app.run(debug=True)