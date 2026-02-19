# Rozšafný generátor lístečků

### Popis:
Tento projekt byl stvořen pro generování lístečků pro výpravy oddílu Skarabeus. 

Lístečky jsou generovány z HTML šablon pomocí Jinja2 a následně převáděny do PDF pomocí WeasyPrint, lísteček na stránky je dále z PDF převeden na PNG, jež je pak oříznuto pro odstranění okrajů z A4 PDF. 

Projekt také obsahuje flaskovou webovou aplikaci pro jejich snadné vytváření a díky jednoduché TinyDB databázi i správu.

### Použití:
Doporučuje se generátor spouštět ve WSL na Windows nebo přímo v Linuxu. 

Lístečku je možno generovat buďto spuštěním skriptu `generovani.py` přímo, nebo jako webovou aplikaci spuštěním `app.py`. 

Knihovny je doporučeno instalovat do vytvořeného virtuálního prostředí, které je možno nainstalovat, aktivovat a nainstalovat knihovny následovně:

```bash
python3 -m venv .venv
source .venv/bin/activate  # na Windows: .venv\Scripts\activate
pip install -r requirements.txt # Flask a TinyDB jsou potřeba pouze pro webovou aplikaci
```

### Současný stav:
- momentálně je aplikováno dočasné CSS v branch `temporary-css`, stav bez CSS je uložen v `master`
    - v plánu je totiž vytvořit design znovu od začátku, nejspíš pomocí JavaScriptu, třeba pomocí frameworků Vue nebo React

### Plány na vylepšení:
- [x] automatické zálohování databáze
- [x] při otevření šablony se nastaví aktuální rok
- [x] udělat web indexovatelný pro vyhledávače (DuckDuckGo, Google)
- [ ] vylepšit (spíš udělat nový) design webu
- [x] automatické přizpůsobení motivu (světlý/tmavý) podle nastavení zařízení
- [ ] okamžitý náhled při vyplňování formuláře (pomocí JavaScriptu)
- [ ] vyskakovací okno prohlížeče při zavírání neuloženého formuláře