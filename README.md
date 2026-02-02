# Rozšafný Python generátor lístečku
Doporučuje se používat ve WSL na Windows nebo přímo v Linuxu. Je třeba nainstalovat určité knihovny:

```bash
pip3 install jinja2 weasyprint Pillow
```

Potřebuji přejmenovat pár proměnných, nějaké přidat. 

- rozchod_cas a rozchod_misto se přejmenuje na navrat_cas atd.
- penize se přejmenuje na cena
- sraz_misto a navrat_misto se přejmenuje na sraz_misto_1 a navrat_misto_1
- 

Úkoly:
- opravit cenu a návrat
- přidat tlačítko domů
- zkrátit text u šablony na: „Nechť si vyberou nějaký starý lísteček jako šablonu a vdechnou mu zpět život.“
- přejmenovat na „Rozšafný generátor lístečků“
- přejmenovat formulář, aby onikal
- přidat ikonu
- přidat varování, aby nebyl zavírán neuložený formulář
- dát funkční betaverzi s CSS na Freda, poslat Márovi
- [ ] přidat položky do formuláře (dva labely dle vlastního výběru, druhý řádek pro místo)
- [ ] upravit formulace v listecek.html (aby odpovídaly těm na lístečku + čas a místo nadepsat )
- [ ] sjednotit stejně tak názvy proměnných s názvy položek v lístečku
- lístečky se v seznamu řadí podle roku a pak až podle id (pokud moc složité, popřeházíme id v databázi)
- [ ] přidat CSS, aby to celé nějak vypadalo

Vylepšení:
- [ ] při otevření šablony se nastaví aktuální rok
- [ ] přidat náhled na web (rovnou pomocí JavaScriptu)