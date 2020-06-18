# Toteutus

Sovellus on toteutettu Python-kielellä Flaskia käyttäen. Muotoilussa on hyödynnetty Jinja2:sta ja tietokantoihin liittyvissä toiminnallisuuksissa SQLAlchemyä. Kaavakkeissa on hyödynnetty WTFormsia ja salasanat on suojattu bcryptillä.


## Ominaisuudet tiivistetysti
*Katso tarkempia tietoja [täältä](/documentation/UserStories.md)*

* Rekisteröityminen, kirjautuminen
* Oman käyttäjätunnuksen ja salasanan muokkaaminen
* Kyselyiden luominen
* Kyselyihin vastaaminen
* Oman kyselyn muokkaaminen, poistaminen ja tulosten tarkastelu
* Admin-käytäjä voi poistaa käyttäjiä ja kyselyitä sekä tarkastella käyttäjien aktiivisuutta
* Kyselyiden etsiminen hakusanalla

## Käyttäjäryhmät

Sovelluksessa on kaksi käyttäjäryhmää:
* tavallinen käyttäjä
* admin-käyttäjä

## Puutteet ja rajoitteet

### Kyselyt

* Kyselyt ovat aina käynnissä, eikä niille voi asettaa esimerkiki aikaa, jolloin niihin voi vastata. Kyselyä saatetaan siis muokata niin, että kysely muuttuu oleellisesti sen jälkeen, kun on jo antanut oman äänensä.
* Vastausvaihtoehtoja voi olla vain kolme, eikä käyttäjä voi päättää, montako vastausvaihtoehtoa kyselyssä on. Tämä olisi ilmeisesti vaatinut JavaScript osaamista, enkä ole siihen perehtynyt koskaan, ja tämän kurssin puitteissa en kokenut hyväksi ideaksi alkaa tutustumaan siihen.
* Omia kyselyitä ei näe erilliseltä sivulta.

### Hakutoiminnallisuus

* Haku on toteutettu SQL-kyselyllä, joka on melko yksinkertainen. Käyttäjän tulee siis tietää melko tarkasti, mitä etsii.
* Kun hakutuloksista avaa kyselyn, yksittäisen kyselyn näyttävällä sivulla oleva *Return*-linkki vie kaikkien kyselyiden listausnäkymään sen sijaan, että se veisi muut hakutulokset näyttävään näkymään.

### Sivutus

* Sivutus on käytössä vain kaikki kyselyt listaavassa näkymässä ja Adminin *User management*-näkymässä.

## Kehitysideat

Puutteiden ja rajoitteiden niin sanotun korjaamisen lisäksi sovellukseen voisi toteuttaa:

* Adminille mahdollisuus antaa admin-oikeudet tavalliselle käyttäjälle. Tässä voisi hyödyntää *User activity* näkymää, ja pitää yhtenä admin-oikeuksien ehtona sitä, että käyttäjä on riittävän aktiivinen sovelluksessa.
* Lisää mittareita käyttäjän aktiivisuudelle.
* Tietokannan *answer*-taluun talletetaan vastauksen ajankohta, mutta sitä ei käytetä mihinkään. Tämän avulla voisi esimerkiksi luoda kyselyn tulokset näyttävälle sivulle tilastoja.
* Havainnollistava kuvaaja kyselyn tuloksista.
* Kyselyn kuvauksesta vapaaehtoinen. Myös kyselyn vastausvaihtoehdoille voisi halutessaan asettaa kuvaukset.
* Kyselyn päätyttyä kaikki näkisivät kyselyn tulokset (olettaen, että kyselylle voi asettaa alkamis- ja loppumisajankohdan)

## Omat kokemukset

Kurssi oli mielenkiintoinen ja harjoitustyötä oli mukava tehdä. Kurssimateriaalin ohjeilla pääsi hyvin alkuun työn kanssa, mutta paljon tietoa piti silti etsiä itse. Harjoitustyötä tehdessäni koen oppineeni paljon uutta. Kurssi vei kuitenkin enemmän aikaa kuin olin aluksi ajatellut. Oman tekemisen aikatauluttamista voisi siis parantaa.

Minulla oli hieman ongelmia kurssin vaatimuksien hahmottamisessa, sillä materiaalissa oli osittain asiat esitetty aika pirstaleisesti. Esimerkiksi osassa 6 on listattu dokumentaation rakenne, mutta siitä puuttuu joitain Johdannossa mainittuja dokumentaation osia. Nekin kuitenkin on tarkistettavissa johdannosta. Kokonaisuudessaan harjoitustyötä oli mukava tehdä!
