# Zadání dat
if True == True:
    zadat = input("Vlastní data (Y/n)? ")
else:
    zadat = "n"
if zadat in ['y', 'Y', 'yes', 'YES']:
    print("Pro přeskočení položky stiskněte Enter.")
    nazev_vypravy = input("Název výpravy: ")
    sraz_cas = input("Čas srazu: ")
    sraz_misto = input("Místo srazu: ")
    rozchod_cas = input("Čas rozchodu: ")
    rozchod_misto = input("Místo rozchodu: ")

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
    volba = int(input("Testovací data (0–4): "))
    if volba == 0:
        data = {
            "nazev_vypravy": "Nejen autodráha v klubovně",
            "sraz_cas": "v sobotu 20. 9. v 10:00",
            "sraz_misto": "v klubovně",
            "rozchod_cas": "v neděli 21. 9. v 17:00",
            "rozchod_misto": "tamtéž",
            "s_sebou": "výbornou náladu, věci dle seznamu věcí na vícedenní výpravu na našich stránkách (půjdeme na výlet, starší budou venku i spát)",
            "kdo_ma": "",
            "jidlo": "dvě snídaně, dva obědy, jedna večeře; k volnému užití bude varná konvice a mikrovlnka, akorát sobotní oběd mladších / sobotní večeře a nedělní snídaně i oběd starších musí být studený",
            "penize": "100 Kč; možná půjde dělat autíčka, to byste za něj zaplatili něco navíc; kolik, se ještě uvidí",
            "poznamka": "Bude zima, tak se oblečte, jak vám je po chuti. Klidně můžete zmrznout, ale mrazák nechte doma.",
            "kontakty": [
                {"jmeno": "Vojta (starší)", "telefon": "739 287 724", "email": "vevebot123@gmail.com"},
                {"jmeno": "Myšák (mladší)", "telefon": "731 192 036", "email": "mysak@ctrnactka.cz"}
            ]
        }
    elif volba == 1:
        data = {
            "nazev_vypravy": "Výprava na hrad",
            "sraz_cas": "v pátek 5. 10. v 9:00",
            "sraz_misto": "u klubovny",
            "rozchod_cas": "v neděli 6. 10. v 16:00",
            "rozchod_misto": "u klubovny",
            "s_sebou": "děsivou náladu",
            "kdo_ma": "lékárničku (starší)",
            "jidlo": "",
            "penize": "",
            "poznamka": "Jídlo netřeba, v lese je ho dost.",
            "kontakty": [
                {"jmeno": "Petr Novák", "telefon": "123 456 789", "email": "petr.novak@gmail.com"}
            ]
        }
    elif volba == 2:
        data = {
            "nazev_vypravy": "Pepa má narozeniny",
            "sraz_cas": "v pátek 15. 7. v 18:00",
            "sraz_misto": "na Hlaváku",
            "rozchod_cas": "v neděli 17. 7. v 14:00",
            "rozchod_misto": "tam, kde to nikdo nečeká",
            "s_sebou": "věci dle seznamu na vícedenní výpravu na našich stránkách, plus něco na překvapení pro Pepu, dobré boty a pláštěnku, protože nevíme, kde to bude, může pršet, může být bláto, může tam být i medvěd, ale pepřák s sebou neberte",
            "kdo_ma": "gril, nejlépe na solární pohon, výkon minimálně 5 kW, rošt pro 10 osob, přenosný stolík a skládací židličky, plus nádobí pro 10 osob, varhany přijdou vhod, stejně tak zvon",
            "jidlo": "pokud někdo přinese gril, budeme grilovat, jinak smůla, žádné sladkosti ani fastfoody, prosím, Pepa je na dietě",
            "penize": "1000–5000 Kč, Pepa je pěkný gurmán a žrout",
            "poznamka": "Nezapomeňte, že Pepa má rád překvapení, takže ať je to něco originálního!",
            "kontakty": [
                {"jmeno": "Jana Svobodová", "telefon": "987 654 321", "email": ""}
            ]
        }
    elif volba == 3:
        data = {
            "nazev_vypravy": "Bruslení se Čtrnáctkou",
            "sraz_cas": "v sobotu 17. 1. v 14:50",
            "sraz_misto": "Škoda Icerink Strašnice (poblíž metra Skalka)",
            "rozchod_cas": "táž sobota v 17:00",
            "rozchod_misto": "tamtéž",
            "s_sebou": "rukavice, pití, kdyžtak svačinu",
            "kdo_ma": "brusle",
            "jidlo": "",
            "penize": "150 Kč (případně dalších 120 Kč za půjčení bruslí + 1000 Kč na vratnou zálohu)",
            "poznamka": "Pokud chcete (anebo si na bruslích nevěříte), vezměte si helmu.",
            "kontakty": [
                {"jmeno": "Milan", "telefon": "734 584 285", "email": "verrdeta@gmail.com"}
            ]
        }
    elif volba == 4:
        data = {
            "nazev_vypravy": "Běžkovací výprava do Neratova (Orlické hory)",
            "sraz_cas": "ve čtvrtek 29. 1. v 15:42",
            "sraz_misto": "na Hlavním nádraží",
            "rozchod_cas": "v neděli 1. 2. v 18:43",
            "rozchod_misto": "tamtéž",
            "s_sebou": "věci na vícedenní výpravu (karimatku stačí, když si vezme ¼ z nás), běžky, hůlky, běžkovací boty, malý batůžek, případně termosku, teplé oblečení na dovnitř",
            "kdo_ma": "lakrosku, vosky",
            "jidlo": "čtvrteční večeři, dva obědy na výlety",
            "penize": "zaplatíte po výpravě (bude to cca 600 Kč)",
            "poznamka": "Dejte si běžkovací boty apod. do batohu nahoru, poněvadž z autobusu půjdeme nějakých 5 km na běžkách (když nebude sníh, tak pěšky). <p></p> Když přijedeme, bude v chalupě teplota jak venku a jen tak se celá nevytopí.",
            "kontakty": [
                {"jmeno": "Fred", "telefon": "778 597 126", "email": "fred@ctrnactka.cz"}
            ]
        }

# Import knihoven
import jinja2
from weasyprint import HTML, CSS
import io

# Načtení předgenerovaných base64 obrázků
with open('header_obrazek.b64', 'r') as f:
    image_data = f.read()
    image_path = f"data:image/jpeg;base64,{image_data}"
with open('header_nazev.b64', 'r') as f:
    header_data = f.read()
    header_path = f"data:image/jpeg;base64,{header_data}"

# Přidání obrázků do slovníku data
data["image_path"] = image_path
data["header_path"] = header_path

# Jinja2 jde do akce!
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

# Generování HTML lístečků do paměti
vystupní_html_stranky = env.get_template('sablona_stranky.html').render(data)
vystupní_html_tisk = env.get_template('sablona_tisk.html').render(data)

# Generování PNG obrázku ze stránkového HTML
try:
    # Vygenerování PDF do paměti
    pdf_bytes = io.BytesIO()
    HTML(string=vystupní_html_stranky).write_pdf(
        pdf_bytes,
        stylesheets=[CSS(string='@page { size: auto; margin: 0; }')])
    pdf_bytes.seek(0)
    # Konvertování PDF na PNG
    from pdf2image import convert_from_bytes
    images = convert_from_bytes(pdf_bytes.read(), first_page=1, last_page=1, dpi=150)
    # Automatické oříznutí bílého místa)
    image = images[0]
    from PIL import ImageChops
    inverted_image = ImageChops.invert(image.convert('L'))
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