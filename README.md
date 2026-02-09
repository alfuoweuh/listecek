# Rozšafný Python generátor lístečku
Doporučuje se používat ve WSL na Windows nebo přímo v Linuxu. Je třeba nainstalovat určité knihovny:

```bash
pip3 install jinja2 weasyprint Pillow pdf2image
```

Projekt je možno používat buďto jako Flaskovou webovou aplikaci spuštěním `app.py`, nebo spuštěním skriptu `generovani.py` přímo. 

Úkoly:
- [ ] přidat CSS, aby to celé nějak vypadalo
- [ ] přidat ikonu
- [ ] dát funkční betaverzi s CSS na Freda, poslat Márovi

Vylepšení:
- [ ] automatické zálohování databáze
- [ ] automatické přizpůsobení motivu (světlý/tmavý) podle nastavení zařízení
- [ ] při otevření šablony se nastaví aktuální rok
- [ ] okamžitý náhled při vyplňování formuláře (pomocí JavaScriptu)
- [ ] vyskakovací okno prohlížeče při zavírání neuloženého formuláře