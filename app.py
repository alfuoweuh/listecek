from flask import Flask, render_template, request, send_file
from datetime import datetime
from tinydb import TinyDB, Query
from generovani import generate

app = Flask(__name__)
db = TinyDB('listecky.json')

# Globální proměnné pro uložené soubory
listecek_png_cache = None
listecek_pdf_cache = None


@app.route('/', methods=['GET', 'POST'])
def home():
    action = request.form.get('action')
    if request.method == 'POST' and action == 'yes_delete': # Delete was confirmed
        id = request.form.get('id', '').strip()
        if id:
            db.remove(Query().id == int(id))
    return render_template('index.html')


@app.route('/vyber', methods=['GET'])
def vyber():
    action = request.args.get('action')  # What button was pressed?
    return render_template('vyber.html', action=action, listecky=db.all())


@app.route('/listecek', methods=['GET', 'POST'])
def listecek():
    global listecek_png_cache, listecek_pdf_cache
    
    if request.method == 'GET': # Button on the welcome page was pressed
        action = request.args.get('action')  # What button was pressed?

        if action == 'template' or action == 'open':
            id = int(request.args.get('id', ''))
            data = db.get(Query().id == id)

            if action == 'template':
                data['id'] = ''
            
            
        elif action == 'new':
            data = {
                "rok": str(datetime.now().year)
            }

        return render_template('listecek.html', **data)


    elif request.method == 'POST':
        action = request.form.get('action')
        
        data = {
            "id": request.form.get('id', ''),
            "nazev_vypravy": request.form.get('nazev_vypravy', ''),
            "rok": request.form.get('rok', ''),
            "sraz_cas": request.form.get('sraz_cas', ''),
            "sraz_misto": request.form.get('sraz_misto', ''),
            "rozchod_cas": request.form.get('rozchod_cas', ''),
            "rozchod_misto": request.form.get('rozchod_misto', ''),
            "s_sebou": request.form.get('s_sebou', ''),
            "kdo_ma": request.form.get('kdo_ma', ''),
            "jidlo": request.form.get('jidlo', ''),
            "penize": request.form.get('penize', ''),
            "poznamka": request.form.get('poznamka', ''),
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

        if action == 'save' or action == 'generate':
            if data['id'] == '':
                data['id'] = max([int(item.get('id', 0)) for item in db.all() if item.get('id')]) + 1
            else:
                data['id'] = int(data['id'])
            db.upsert(data, Query().id == data['id'])
        if action == 'generate':
            listecek_png_cache, listecek_pdf_cache = generate(data)
        if action == 'delete':
            return render_template('smazat.html', **data)
        else:
            return render_template('listecek.html', action=action, **data)


@app.route('/download/<file_type>')
def download(file_type):
    global listecek_png_cache, listecek_pdf_cache
    
    if file_type == 'png' and listecek_png_cache:
        listecek_png_cache.save('listecek_stranky.png')
        return send_file('listecek_stranky.png', as_attachment=True, download_name='listecek_stranky.png')
    elif file_type == 'pdf' and listecek_pdf_cache:
        listecek_pdf_cache.seek(0)
        return send_file(listecek_pdf_cache, as_attachment=True, download_name='listecek_tisk.pdf', mimetype='application/pdf')
    else:
        return "Soubor není k dispozici", 404


if __name__ == '__main__':
    app.run(debug=True)