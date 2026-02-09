import os
import io
from flask import Flask, render_template, request, send_file, redirect, url_for
from datetime import datetime
from tinydb import TinyDB, Query
from generovani import generate

# Flask app and TinyDB setup with absolute path for the DB file
app = Flask(__name__)
dir_abs_path = os.path.dirname(os.path.abspath(__file__))
db_abs_path = os.path.join(dir_abs_path, 'listecky.json')
db = TinyDB(db_abs_path)


# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # Deleting an entry from DB
    action = request.form.get('action')
    if request.method == 'POST' and action == 'yes_delete':
        id = request.form.get('id', '').strip()
        if id:
            db.remove(Query().id == int(id))

    return render_template('index.html')


# Selection page
@app.route('/vyber', methods=['GET'])
def vyber():
    action = request.args.get('action')
        
    # Sort by year (descending) and then by ID (descending)
    listecky = db.all()
    listecky.sort(key=lambda x: (int(x.get('rok', 0)) if str(x.get('rok', '')).isdigit() else 0, int(x.get('id', 0))), reverse=True)
    
    return render_template('vyber.html', action=action, listecky=listecky)


# Form page
@app.route('/listecek', methods=['GET', 'POST'])
def listecek():
    # The user comes from an selection or home page (open, template, new)
    if request.method == 'GET': 

        # What button was pressed?
        action = request.args.get('action')

        # Preparing data for the form
        if action == 'template' or action == 'open':
            id = int(request.args.get('id', ''))
            data = db.get(Query().id == id)
            if action == 'template':
                data['id'] = ''
        
        # New empty form with current year
        else:
            data = {
                "rok": str(datetime.now().year)
            }
        
        # Rendering form
        return render_template('listecek.html', **data)

    # The user comes from the form
    elif request.method == 'POST':

        # Getting form data from user
        data = {
            "id": request.form.get('id', ''),
            "nazev_vypravy": request.form.get('nazev_vypravy', ''),
            "rok": request.form.get('rok', ''),
            "sraz_cas": request.form.get('sraz_cas', ''),
            "sraz_misto_1": request.form.get('sraz_misto_1', ''),
            "sraz_misto_2": request.form.get('sraz_misto_2', ''),
            "navrat_cas": request.form.get('navrat_cas', ''),
            "navrat_misto_1": request.form.get('navrat_misto_1', ''),
            "navrat_misto_2": request.form.get('navrat_misto_2', ''),
            "s_sebou": request.form.get('s_sebou', ''),
            "kdo_ma": request.form.get('kdo_ma', ''),
            "jidlo": request.form.get('jidlo', ''),
            "cena": request.form.get('cena', ''),
            "poznamka": request.form.get('poznamka', ''),
            "label_vlastni_1": request.form.get('label_vlastni_1', ''),
            "vlastni_1": request.form.get('vlastni_1', ''),
            "label_vlastni_2": request.form.get('label_vlastni_2', ''),
            "vlastni_2": request.form.get('vlastni_2', ''),
            "kontakt_jmeno_0": request.form.get('kontakt_jmeno_0', ''),
            "kontakt_telefon_0": request.form.get('kontakt_telefon_0', ''),
            "kontakt_email_0": request.form.get('kontakt_email_0', ''),
            "kontakt_jmeno_1": request.form.get('kontakt_jmeno_1', ''),
            "kontakt_telefon_1": request.form.get('kontakt_telefon_1', ''),
            "kontakt_email_1": request.form.get('kontakt_email_1', ''),
            "kontakt_jmeno_2": request.form.get('kontakt_jmeno_2', ''),
            "kontakt_telefon_2": request.form.get('kontakt_telefon_2', ''),
            "kontakt_email_2": request.form.get('kontakt_email_2', '')
        }

        # What button was pressed?
        action = request.form.get('action')

        # Saving data to DB
        if action in ['save', 'home', 'download_png', 'download_pdf']:
            if any(value.strip() for key, value in data.items() if key != 'rok'):
                if data['id'] == '':
                    all_ids = [int(item.get('id', 0)) for item in db.all() if item.get('id')]
                    data['id'] = max(all_ids) + 1 if all_ids else 1
                else:
                    data['id'] = int(data['id'])
                db.upsert(data, Query().id == data['id'])

        # Generating files
        if action == 'download_png':
            listecek_png = generate(data, 'png')
            return stahnout('png', listecek_png)
        elif action == 'download_pdf':
            listecek_pdf = generate(data, 'pdf')
            return stahnout('pdf', listecek_pdf)

        # Going home
        elif action == 'home':
            return redirect(url_for('home'))
        
        # Deleting data from DB
        elif action == 'delete':
            return render_template('smazat.html', **data)

        # Rendering the form again
        else:
            return render_template('listecek.html', action=action, **data)

# Downloading files
@app.route('/stahnout')
def stahnout(file_type, listecek_bytes):
    if file_type == 'png' and listecek_bytes:
        img_io = io.BytesIO()
        listecek_bytes.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, as_attachment=True, download_name='listecek_stranky.png', mimetype='image/png')
    
    elif file_type == 'pdf' and listecek_bytes:
        listecek_bytes.seek(0)
        return send_file(listecek_bytes, as_attachment=True, download_name='listecek_tisk.pdf', mimetype='application/pdf')

# Error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('chyba.html', error_code=404, error_message='stránka nenalezena'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('chyba.html', error_code=500, error_message='vnitřní chyba serveru'), 500

@app.errorhandler(400)
def bad_request(error):
    return render_template('chyba.html', error_code=400, error_message='špatný požadavek'), 400

# Running the Flask app directly
if __name__ == '__main__':
    app.run(debug=True)