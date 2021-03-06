# Polling App

Sovellus on tehty Helsingin yliopiston [Tietokantasovellus](https://materiaalit.github.io/tsoha-20/)-kurssilla.

## Aihekuvaus

Sovellus äänestyksiä varten. Kirjautuneena käyttäjänä sovelluksessa voi luoda äänestyksiä. Äänestyksille 
voi asettaa vastausvaihtoehtoja, ja äänestäjä voi äänestää vain yhtä niistä. 
Äänestykselle asetetaan kuvaus, joka kertoo äänestyksestä hieman pelkkää kysymystä tarkemmin. Äänestäjän 
on mahdollista kirjautua sisään, mikä mahdollistaa sellaisien äänestysten 
luomisen, joihin tietty henkilö voi vastata vain kerran. Anonyymien kyselyiden tekeminen on myös mahdollista, jolloin kyselyyn voi vastata myös kirjautumatta sisään. Anonyymeihin kyselyihin sama henkilö voi vastata useita kertoja.

Sovelluksessa on kaksi käyttäjärymää, tavallinen käyttäjä ja admin käyttäjä. Tavallinen käyttäjä voi suorittaa kaikki edellä mainitut toiminnot. Admin käyttäjä voi lisäksi poistaa käyttäjiä, ja käyttäjän poistamisen yhteydessä poistuvat myös tämän luomat kyselyt ja niihin liittyvät vastaukset ja vastausvaihtoehdot. Admin voi myös poistaa epäasiallisia kyselyitä. Käyttäjät voivat vaihtaa käyttäjätunnusta ja salasanaa.

## Dokumentaatio

[Asennusohje](/documentation/asennusohje.md)

[Käyttöohje](/documentation/kayttoohje.md)

[User stories](/documentation/UserStories.md)

[Kuvaus tietokannasta](/documentation/tietokanta.md)

[Tietokantakaavio](/documentation/Dbdiagram.png)

[Toteutus](/documentation/toteutus.md) (sitältää puutteet ja rajoitteet, kehitysideat sekä omat kokemukset)

## Sovellus Herokussa

[https://make-polls-app.herokuapp.com/](https://make-polls-app.herokuapp.com/)

Testitunnuksia Herokussa olevaan sovellukseen:
|                     | Käyttäjätunnus      | Salasana           |
|---------------------| ------------------- |--------------------| 
|Tavallinen käyttäjä  | hello               | hellohello         |
|Tavallinen käyttäjä  | testi               | testi1234          |
| Admin käyttäjä      | admin               | adminadmin         |

