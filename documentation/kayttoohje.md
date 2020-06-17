# Käyttöohje

## Sovelluksen käyttöönotto

Voit ottaa sovelluksen käyttöön useilla tavoilla:

* Siirry sovellukseen linkistä https://make-polls-app.herokuapp.com/.
  * Voit luoda sovelluksen oman käyttäjätunnuksen tai testata sovellusta [README.md](/README.md):stä löytyvillä testitunnuksilla.
* Asenna sovellus paikallisesti ja käynnistä se [asennusohjeen](/documentation/asennusohje.md) mukaisesti. 
  * Sovellukseen luotava ensimmäinen käyttäjä on aina admin-oikeuksilla varustettu käyttäjä. Ensimmäisen käyttäjän jälkeen luodut käyttäjät ovat tavallisia käyttäjiä.
* Voit myös asentaa sovelluksen Herokuun [asennusohjeen](/documentation/asennusohje.md) mukaisesti.
  * Myös Herokussa ensimmäinen sovellukseen rekisteröityvä käyttäjä on aina admin-käyttäjä. Tämän jälkeen luodut käyttäjät ovat oikeuksiltaan tavallisia käyttäjiä.
  
## Käyttäjätoiminnot

### Rekisteröityminen

Sovellukseen voi rekisteröityä painamalla oikean yläkulman *Sign up* linkkiä. Kirjoita kenttiin oma nimesi, käyttäjätunnus ja salasana sekä varmista salasana vielä viimeisessä kentässä. Nimen tulee olla vähintään yksi ja enintään 20 merkkiä pitkä, käyttäjätunnuksen 3-20 merkkiä pitkä ja salasanan 8-20 merkkiä pitkä. Lisäksi käyttäjätunnuksen tulee olla uniikki. Kun tiedot on täytetty, rekisteröityminen tapahtuu klikkaamalla *Create a new user* painiketta.

Pienillä näytöillä yläpalkin oikean yläkulman linkit katoavat, joten rekisteröitymislinkki löytyy myös vasemman ylänurkan valikkonapin (kolme viivaa päällekäin) takaa.

### Sisäänkirjautuminen

Sovellukseen kirjaudutaan sisään klikkaamalla oikean yläkulman tai vasemman ylänurkan valikkonapin takaa linkkiä *Login*. Syöttämällä käyttäjätunnuksen ja salasanan ja sen jälkeen painamalla *Login* nappia voit kirjautua sisään.

### Uloskirjautuminen

Uloskirjautuminen tapahtuu klikkaamalla oikean yläkulman tai vasemman ylänurkan valikosta löytyvää linkkiä *Logout*.

### Käyttäjätietojen muokkaamien

Käyttäjätunnusta ja salasanaa pääsee vaihtamaan klikkaamalla oikeasta ylänurkasta tai vasemman ylänurkan napista avautuvasta valikosta *Logged in as* tekstin osana olevaa omaa nimeäsi. Linkki johtaa niin sanotulle profiilisivulle, jossa näkyy käyttäjän nimi ja käyttäjätunnus sekä linkit *Change username* ja *Change password*. Linkin *Change username* takaa pääsee vaihtamaan käyttäjätunnusta ja linkin *Change password* takaa salasanaa.

## Perustoiminnot

### Kyselyn luominen

Kyselyn luominen tapahtuu klikkaamalla valikosta linkkiä *Add a new poll*. Avautuvalle lomakkeelle syötetään kyselyn tiedot ja päätetään, onko kysely anonyymi vai vaatiiko kyselyyn vastaaminen kirjautumisen. Kun tiedot on täytetty, kysely luodaan klikkaamalla alareunan *Create a new poll* painiketta.

### Kyselyssä äänestäminen

Voit tarkastella kyselyitä klikkaamalla valikosta linkkiä *List of polls*, joka avaa sivun, jossa kaikki kyselyt on listattu. Kyselyt on taulukoitu, ja ensimmäisessä sarakkeessa on kyselyn kysymys, joka on linkki, jota klikkaamalla pääsee tarkastelemaan kyseistä kyselyä. Seuraava sarake kertoo, vaatiiko kyselyssä äänestäminen sisäänkirjautumisen vai ei. Kolmannessa sarakkeessa näkyy kyselyn luontihetki, ja viimeisestä sarakkeesta näet, mitkä kyselyt ovat sinun luomiasi (olettaen, että olet kirjautunut sisään). Jos kyselyjä on yli 10, kyselyt listautuvat eri sivuille, joiden välillä pääsee liikkumaan taulukon alapuolella olevista painikkeista klikkaamalla.

Varsinainen äänestäminen tapahtuu avaamalla kysely ensimmäisen sarakkeen linkkiä painamalla ja valitsemalla sopivan vastausvaihtoehdon ja sen jälkeen painamalla *Vote* painiketta. Oletuksena viimeinen vaihtoehto on valittuna, mutta vaihtoehdon vaihtaminen onnistuu yksinkertaisesti valitsemalla jokin toinen annetusta vaihtoehdoista. Kyselyn luoja ei pysty äänestämään omassa kyselyssä.

### Kyselyn muokkaaminen

Kyselyn muokkaaminen on mahdollista vain sille käyttäjälle, joka on luonut kyselyn. Kyselyä pääsee muokkaamaan klikkaamalla kyselyn auki ja valitsemalla kyselyn kysymyksen alapuolelta linkkiä *Edit*. Avautuvalla lomakkeella voit muuttaa tietoja, ja tallentaa muutokset painamalla lopuksi sivun alalaidasta *Update poll* painiketta.

### Kyselyn poistaminen

Poistamistoiminnallisuus löytyy samasta näkymästä kuin kyselyn muokkaaminen. Painike on *Update poll* painikkeen alapuolella. Klikkaamalla painiketta *Delete poll* kysely ja siihen liittyvät muut tallennetut tiedot deletoituvat.

### Tulosten tarkastelu

Tuloksia voi tarkastella vain se käyttäjä, joka on luonut kyselyn. Tuloksia pääsee tarkastelemaan klikkaamalla kyselyn editoimiseen vievän painikkeen viereistä painiketta *Results*.

### Kyselyiden etsiminen hakutoiminnolla

Kyselyitä voi etsiä hakutoiminnon avulla. Haku löytyy valikon linkin *Search* takaa. Esille tulevaan kenttään voi kirjoittaa hakusanan, ja haku etsii kyselyitä sen perusteella, esiintyykö hakusana kyselyn kysymyksessä.

## Admin-toiminnot

Admin-käyttäjällä on lähes samat oikeudet kuin tavallisella käyttäjällä.

### Käyttäjän poistaminen

Admin käyttäjä kykenee poistamaan käyttäjän kokonaan. Tämän toiminnallisuuden löytää klikkaamalla valikon linkkiä *User management*, joka avaa näkymän, jossa käyttäjät on listattu. Jokaisen käyttäjän vieressä on *Delete* painike, jota klikkaamalla käyttäjä ja kaikki käyttäjään liittyvä tieto (myös käyttäjän luomiin kyselyihin liittyvät tiedot) poistetaan.

### Kyselyn poistaminen

Admin voi poistaa minkä tahansa kyselyn. Syy poistamiseen voi olla esimerkiksi epäasiallinen sisältö. Poistaminen onnistuu painamalla kyselyn äänestyspainikkeen alapuolelta painiketta *Delete poll*.

### Käyttäjien aktiivisuuden tarkasteleminen

Admin voi tarkastella käyttäjien aktiivisuutta kyselyihin vastaamisen suhteen siirtymällä valikosta *User activity* sivulle. Tätä tietoa voisi tulevaisuudessa hyödyntää esimerkiksi admin-oikeuksien myöntämisessä muille käyttäjille, katso [kehitysehdotukset]().
