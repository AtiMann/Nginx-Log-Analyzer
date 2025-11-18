# Nginx Log Analyzer

Ez a Python-script egy Nginx logfájlt elemez, és statisztikákat készít a következőkről:

- Top 5 IP cím
- Top 5 lekért útvonal
- Top 5 HTTP státuszkód
- Top 5 User-Agent
- Az eredményeket konzolra írja és `stat.csv` fájlba menti

## Projekt Felépítése

project/
│── analyzer.py
│── stat.csv (futás után jön létre)
│── README.md
└── .gitignore


## ⚙️ Telepítés

1. **Python 3.8+ szükséges**
2. A repository klónozása:
   ```bash
   git clone https://github.com/felhasználó/projekt-neve.git
   cd projekt-neve

## Futtatás
**python analyzer.py**
