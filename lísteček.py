# import sqlite3
# conn = sqlite3.connect('výpravy.db')
import jinja2
from weasyprint import HTML, CSS
from PIL import Image
import io

# Zadání dat
zadat = input("Vlastní data (y/n)? ")
if zadat in ['y', 'Y', 'yes', 'YES']:
    název_výpravy = input("Název výpravy:")
    sraz_čas = input("Čas srazu:")
    sraz_místo = input("Místo srazu:")
    rozchod_čas = input("Čas rozchodu:")
    rozchod_místo = input("Místo rozchodu:")

    s_sebou = input("Co s sebou:")
    jidlo = input("Jaké jídlo s sebou:")
    penize = input("Kolik peněz s sebou:")
    kontakty = []
    while True:
        jmeno = input("Jméno kontaktu (nebo prázdné pro konec): ")
        if jmeno == "":
            break
        telefon = input("Telefon: ")
        email = input("Email: ")
        kontakty.append({"jmeno": jmeno, "telefon": telefon, "email": email})
else:
    název_výpravy = "Nejen autodráha v klubovně"
    sraz_čas = "v sobotu 20. 9. v 10:00"
    sraz_místo = "v klubovně"
    rozchod_čas = "v neděli 21. 9. v 17:00"
    rozchod_místo = "tamtéž"

    s_sebou = "výbornou náladu, věci dle seznamu věcí na vícedenní výpravu na našich stránkách (půjdeme na výlet, starší budou venku i spát)"
    jidlo = "dvě snídaně, dva obědy, jedna večeře; k volnému užití bude varná konvice a mikrovlnka, akorát sobotní oběd mladších / sobotní večeře a nedělní snídaně i oběd starších musí být studený"
    penize = "100 Kč; možná půjde dělat autíčka, to byste za něj zaplatili něco navíc; kolik, se ještě uvidí"
    kontakty = [
        {"jmeno": "Vojta (starší)", "telefon": "739 287 724", "email": "xhurfr01@gjk.cz"},
        {"jmeno": "Myšák (mladší)", "telefon": "731 192 036", "email": "fred@ctrnactka.cz"},
        {"jmeno": "Fred (starší)", "telefon": "778 597 126", "email": "frederik.hurrle@gmail.com"}
    ]

# Příprava dat pro tvorbu HTML lístečku
import os
import base64

# Převeď obrázek na base64 datový URL
with open('header_skarabeus.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')
    header_path = f"data:image/jpeg;base64,{image_data}"

data = {
    "nazev_vypravy": název_výpravy,
    "sraz_cas": sraz_čas,
    "sraz_misto": sraz_místo,
    "rozchod_cas": rozchod_čas,
    "rozchod_misto": rozchod_místo,
    "s_sebou": s_sebou,
    "jidlo": jidlo,
    "penize": penize,
    "kontakty": kontakty,
    "header_path": header_path
}

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

# Generování HTML lístečku na stránky
výstupní_html_stranky = env.get_template('sablona_stranky.html').render(data)
with open("listecek_stranky.html", "w", encoding="utf-8") as f:
    f.write(výstupní_html_stranky)
print("Lísteček jako obrázek: 'listecek_stranky.html'")

# Generování HTML lístečku pro tisk
výstupní_html_tisk = env.get_template('sablona_tisk.html').render(data)
with open("listecek_tisk.html", "w", encoding="utf-8") as f:
    f.write(výstupní_html_tisk)
print("Lísteček pro tisk: 'listecek_tisk.html'")

# Generování PNG obrázku ze stránkového HTML
try:
    # Nejprve vygenerujeme PDF do paměti s minimálními okraji
    pdf_bytes = io.BytesIO()
    HTML(string=výstupní_html_stranky).write_pdf(
        pdf_bytes,
        stylesheets=[CSS(string='@page { size: auto; margin: 0; }')])
    pdf_bytes.seek(0)
    # Konvertujeme PDF na PNG pomocí pdf2image
    from pdf2image import convert_from_bytes
    images = convert_from_bytes(pdf_bytes.read(), first_page=1, last_page=1, dpi=150)
    
    # Automatické oříznutí bílého místa
    image = images[0]
    # Převedeme na odstíny šedi a invertujeme barvy (bílá -> černá, obsah -> bílá)
    from PIL import ImageChops
    inverted_image = ImageChops.invert(image.convert('L'))
    # Získáme "bounding box" obsahu (všeho, co není černé)
    bbox = inverted_image.getbbox()
    if bbox:
        image = image.crop(bbox)
    image.save("listecek_stranky.png")
    print("PNG obrázek vytvořen: 'listecek_stranky.png'")

except Exception as e:
    print(f"Chyba při vytváření PNG: {e}")

# Generování A4 PDF pro tisk
try:
    HTML(string=výstupní_html_tisk).write_pdf("listecek_tisk.pdf")
    print("PDF pro tisk vytvořen: 'listecek_tisk.pdf'")
except Exception as e:
    print(f"Chyba při vytváření PDF: {e}")

# conn.close()