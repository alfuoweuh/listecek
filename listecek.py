#import sqlite3
#conn = sqlite3.connect('výpravy.db')

# Zadání dat
if True == False:
    zadat = input("Vlastní data (Y/n)? ")
else:
    zadat = "n"
if zadat in ['y', 'Y', 'yes', 'YES']:
    volba = 20
    print("Pro přeskočení položky stiskněte Enter.")
    název_výpravy = input("Název výpravy: ")
    sraz_čas = input("Čas srazu: ")
    sraz_místo = input("Místo srazu: ")
    rozchod_čas = input("Čas rozchodu: ")
    rozchod_místo = input("Místo rozchodu: ")

    s_sebou = input("Co s sebou: ")
    kdo_ma = input("Co s sebou jen ti, co mají: ")
    jidlo = input("Jaké jídlo s sebou: ")
    penize = input("Kolik peněz s sebou: ")
    poznamka = input("Poznámka: ")
    kontakty = []
    while True:
        jmeno = input("Jméno kontaktu (nebo prázdné pro konec): ")
        if jmeno == "":
            break
        telefon = input("Telefon: ")
        email = input("Email: ")
        kontakty.append({"jmeno": jmeno, "telefon": telefon, "email": email})

elif zadat in ['n', 'N', 'no', 'NO']:
    volba = int(input("Testovací data (0-2): "))
    if volba == 0:
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
    elif volba == 1:
        název_výpravy = "Výprava na hrad"
        sraz_čas = "v pátek 5. 10. v 9:00"
        sraz_místo = "u klubovny"
        rozchod_čas = "v neděli 6. 10. v 16:00"
        rozchod_místo = "u klubovny"

        s_sebou = "děsivou náladu"
        kdo_ma = "lékárničku (starší)"
        jidlo = ""
        penize = ""
        poznamka = "Jídlo netřeba, v lese je ho dost."
        kontakty = [
            {"jmeno": "Petr Novák", "telefon": "123 456 789", "email": "petr.novak@gmail.com"}
        ]
    elif volba == 2:
        název_výpravy = "Pepa má narozeniny"
        sraz_čas = "v pátek 15. 7. v 18:00"
        sraz_místo = "na Hlaváku"
        rozchod_čas = "v neděli 17. 7. v 14:00"
        rozchod_místo = "tam, kde to nikdo nečeká"

        s_sebou = "věci dle seznamu na vícedenní výpravu na našich stránkách, plus něco na překvapení pro Pepu, dobré boty a pláštěnku, protože nevíme, kde to bude, může pršet, může být bláto, může tam být i medvěd, ale pepřák s sebou neberte"
        kdo_ma = "gril, nejlépe na solární pohon, výkon minimálně 5 kW, rošt pro 10 osob, přenosný stolík a skládací židličky, plus nádobí pro 10 osob, varhany přijdou vhod, stejně tak zvon"
        jidlo = "pokud někdo přinese gril, budeme grilovat, jinak smůla, žádné sladkosti ani fastfoody, prosím, Pepa je na dietě"
        penize = "1000–5000 Kč, Pepa je pěkný gurmán a žrout"
        poznamka = "Nezapomeňte, že Pepa má rád překvapení, takže ať je to něco originálního!"
        kontakty = [
            {"jmeno": "Jana Svobodová", "telefon": "987 654 321", "email": ""}
        ]

# Import knihoven
import jinja2
from weasyprint import HTML, CSS
import io
import base64

# Převod obrázků na base64 datový URL
with open('header_obrazek.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')
    image_path = f"data:image/jpeg;base64,{image_data}"
with open('header_nazev.jpg', 'rb') as f:
    header_data = base64.b64encode(f.read()).decode('utf-8')
    header_path = f"data:image/jpeg;base64,{header_data}"

# Příprava dat pro šablonu
data = {
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
    "image_path": image_path,
    "header_path": header_path
}

# Jinja2 jde do akce!
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

# Generování HTML lístečku na stránky
vystupní_html_stranky = env.get_template('sablona_stranky.html').render(data)
with open("listecek_stranky.html", "w", encoding="utf-8") as f:
    f.write(vystupní_html_stranky)
print("Lísteček na stránky: 'listecek_stranky.html'")

# Generování HTML lístečku pro tisk
vystupní_html_tisk = env.get_template('sablona_tisk.html').render(data)
with open("listecek_tisk.html", "w", encoding="utf-8") as f:
    f.write(vystupní_html_tisk)
print("Lísteček pro tisk: 'listecek_tisk.html'")

# Generování PNG obrázku ze stránkového HTML
try:
    # Nejprve vygenerujeme PDF do paměti s minimálními okraji
    pdf_bytes = io.BytesIO()
    HTML(string=vystupní_html_stranky).write_pdf(
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
    print("PNG na stránky vytvořen: 'listecek_stranky.png'")
except Exception as e:
    print(f"Chyba při vytváření PNG: {e}")

# Generování A4 PDF pro tisk
try:
    HTML(string=vystupní_html_tisk).write_pdf("listecek_tisk.pdf")
    print("PDF pro tisk vytvořen: 'listecek_tisk.pdf'")
except Exception as e:
    print(f"Chyba při vytváření PDF: {e}")

#conn.close()