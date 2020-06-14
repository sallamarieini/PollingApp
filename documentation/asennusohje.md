# Asennusohje

**Asennusohjeet on kirjoitettu Linux-käyttöjärjestelmälle.**

## Tarvittavat työvälineet

* [Pythonin](https://www.python.org/downloads/) versio 3.5 tai uudempi.
* Pakettienhallintajärjestlemä [pip](https://packaging.python.org/key_projects/#pip). Pip asentunee Pythonin asennuksen yhteydessä oletuksena.
* Kirjasto [venv](https://docs.python.org/3/library/venv.html) tarjoaa tuen virtuaaliympäristöjen luomiseen. Kirjasto asentunee edellä asennetun Python-ympäristön yhteydessä.
* [Git](https://git-scm.com/downloads/)-versionhallintajärjestelmä.
* [SQLite](https://www.sqlite.org/download.html)-tietokantahallintajärjestelmä.
* [PostgreSQL](https://www.postgresql.org/)-tietokannanhallintajärjestelmä.
* [Työvälineet](https://devcenter.heroku.com/articles/heroku-cli) Herokun käyttöön sekä tunnukset [Herokuun](https://www.heroku.com/).

## Sovelluksen asentaminen paikallisesti

1. Lataa sovellus omalle tietokoneellesi osoitteesta https://github.com/sallamarieini/PollingApp. Lataaminen tehdään klikkaamalla sivun oikeassa laidassa olevaa nappia *Clone or download* ja valitsemalla avautuvasta valikosta *Download ZIP*.

2. Luo sovellukselle oma kansio. Etsi sitten lataamisen jälkeen sovellus koneeltasi (usein se löytyy *Downloads* nimisestä kansiosta) ja siirrä se sille luomaasi kansioon, ja pura ZIP-tiedosto kyseisessä kansiossa.

3. Avaa tietokoneen komentorivi, ja navigoi sovelluksen kansioon eli siihen kansioon, joka syntyi purettuasi lataamasi ZIP-tiedosto. 

4. Asenna Python-virtuaaliympäristö komentoriviltä komennolla `python -m venv venv`.

5. Aktivoi virtuaaliympäristö komennolla `source venv/bin/activate`. Nyt komentorivillä pitäisi ennen muuta tekstiä (mm. nykyisen kansiosi polkua) näkyä teksti *(venv)*.

6. Seuraavaksi asennetaan sovelluksen tarvitsemat riippuvuudet komennolla `pip install -r requirements.txt`.

7. Ohjelman voi käynnistää komennolla `python run.py`. Ohjelmaa voi nyt käyttää osoitteissa http://localhost:5000/ ja http://127.0.0.1:5000/.

## Sovelluksen asentaminen Herokuun

Asenna sovellus ensin omalle tietokoneellesi yllä olevilla ohjeilla. Sen jälkeen kirjaudu [GitHub](https://github.com/)iin ja luo sinne uusi repositorio sovellukselle ilman README.md tiedostoa. Tämän jälkeen seuraa seuraavia ohjeita:

1. Lisää sovellukselle versionhallinta komennolla `git init`.

2. Yhdistetään sovelus GitHubiin luomaasi repositorioon komennolla `git remote add origin https://github.com/käyttäjätunnus/projektin-nimi.git`, missä komennon lopussa oleva osoite on projektin osoite, joka löytyy githubista.

3. Sovellus lisätään GitHubiin komennoilla `git add .`, `git commit -m "Initial commit"` ja `git push -u origin master`.

4. Luo sovellukselle paikka Herokuun komennolla `heroku create sovelluksennimi`, jossa *sovelluksennimi* on sovelluksen nimi. Jos komennon ajaa ilman sovelluksen nimeä, Heroku luo sovellukselle satunnaisen nimen.

5. Lisää paikalliseen versionhallintaan tieto Herokusta komennolla `git remote add heroku https://git.heroku.com/sovelluksennimi.git`, jossa *sovelluksennimi* on sovelluksellesi edellisessä kohdassa antama nimi.

6. Sovellus voidana nyt laittaa Herokuun ajamalla komennot `git add .`, `git commit -m "Initial commit"` ja lopuksi `git push heroku master`. Sovellusta voi nyt tarkastella osoitteessa *https://sovelluksennimi.herokuapp.com/*.
