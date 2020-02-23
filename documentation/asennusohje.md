## Merilajit-sovelluksen asennusohje

- Lataa ohjelma gitistä.

- Lataa virtuaaliympäristö komennolla 

```
python3 -m venv venv
```

- Käynnistä virtuaaliympäristö komennolla

```
source venv/bin/activate
```

- Asenna kaikki tarvittavat kirjastot komennolla

```
pip install -r requirements.txt
```

- Käynnistä sovellus komennolla

```
python run.py
```

- Avaa selaimessa osoite http://localhost:5000

## Sovelluksen siirto Herokuun

- Lisää projekti Herokuun:

```
heroku config:set HEROKU=1
```

- Lisää postgre-SQL heroku-projektiin.

```
heroku addons:add heroku-postgresql:hobby-dev
```



