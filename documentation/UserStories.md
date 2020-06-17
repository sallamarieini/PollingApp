# User stories

## Tavallisena käyttäjänä haluan vastata kyselyyn.
    INSERT INTO answer (answer_option_id, poll_id, date) 
    VALUES (?, ?, ?);
    
    INSERT INTO users_answered (poll_id, user_id) 
    VALUES (?, ?);
    
Edellisistä kyselyistä ensimmäiseen *answer_option_id* saadaan kyselyllä

    SELECT answer_option.id 
    FROM answer_option 
    WHERE answer_option.poll_id = ? AND answer_option.option = ? 
    LIMIT 1;
    
## Tavallisena käyttäjänä haluan, että minuun ei voi yhdistää, mitä vaihtoehtoa äänestin.
Tässä tapauksessa tieto äänestä lisätään niin, että tietty käyttäjä yhdistetään kyselyyn, johon tämä vastasi, eikä valittuun vastausvaihtoehtoon. Kyselyissä, joissa kirjautumista ei vaadita, tätä tietoa ei talleteta ollenkaan.
    
    INSERT INTO users_answered (poll_id, user_id) 
    VALUES (?, ?);

## Tavallisena käyttäjänä haluan, että voin luoda kyselyn.
Ensin tarkistetaan, että ei jo ole saman nimistä kyselyä

    SELECT poll.question 
    FROM poll 
    WHERE poll.question = ? 
    LIMIT 1;
    
Jos ei ole, kysely lisätään tietokantaan

    INSERT INTO poll (question, description, anonymous, created_date, creator_id)
    VALUES (?, ?, ?, ?, ?);
    
Lisätään myös vastausvaihtoehdot tietokantaan. Haetaan ensin luodun kyselyn id

    SELECT poll.id
    FROM poll
    WHERE poll.question = ?
    LIMIT 1;
    
    INSERT INTO answer_option (option, poll_id)
    VALUES (?, ?);

## Tavallisena käyttäjä haluan, että voin muokata luomaani kyselyä.
Ensin haetaan muokattava kysely ja kyselyn vastausvaihtoehdot

    SELECT *
    FROM poll
    WHERE poll.id = ?
    LIMIT 1;
    
    SELECT *
    FROM answer_option
    WHERE answer_option.poll_id = ?;

Sitten päivitetään haettuja tietoja

    UPDATE poll
    SET question = ?, description = ?
    WHERE poll.id = ?;
    
    UPDATE answer_option
    SET option = ?
    WHERE answer_option.id = ?;

## Tavallisena käyttäjänä haluan, että voin poistaa luomani kyselyn.
Ennen varsinaisen kyselyn poistamista poistetaan muut siihen liittyvät tiedot

    DELETE FROM answer WHERE poll_id = ?;
    DELETE FROM answer_option WHERE poll_id = ?;
    DELETE FROM users_answered WHERE poll_id = ?;
    DELETE FROM poll WHERE poll.id = ?;

## Tavallisena käyttäjänä haluan, että voin tarkastella kyselyn tuloksia.
Aluksi tarkistetaan, että tulosten katsomista yrittävä käyttäjä on kyselyn luoja

    SELECT poll.creator_id
    FROM poll
    WHERE poll.id = ?;
    
Jos käyttäjä on kyselyn luoja, haetaan tulokset

    SELECT answer_option.option, COUNT(answer.answer_option_id)
    FROM answer_option
    LEFT JOIN answer ON answer.answer_option_id = answer_option.id
    WHERE answer_option.poll_id = ?
    GROUP BY answer_option.id;

## Kyselyn luojana voin päättää, vaatiiko kyselyyn vastaaminen tunnistautumista.
Tämä päätetään kyselyä luodessa valitsemalla *anonymous*:n arvoksi True tai False

    INSERT INTO poll (question, description, anonymous, created_date, creator_id)
    VALUES (?, ?, ?, ?, ?);

## Tavallisena käyttäjänä haluan etsiä kyselyitä hakusanalla kysymyksen perusteella.

    SELECT *
    FROM poll
    WHERE poll.question LIKE '% ? %';

## Tavallisena käyttäjänä haluan tarkastella kaikkia kyselyitä.

    SELECT *
    FROM poll;

## Tavallisena käyttäjänä haluan nähdä yksittäisen kyselyn tiedot tarkemmin.

    SELECT *
    FROM poll
    WHERE poll.id = ?
    LIMIT 1;

## Tavallisena käyttäjänä haluan luoda uuden käyttäjätunnuksen.
Ensin tarkistetaan, onko käyttäjätunnus jo varattu

    SELECT *
    FROM account
    WHERE account.username = ?
    LIMIT 1;
    
Jos käyttäjätunnusta ei ole varattu, luodaan uusi käyttäjä
 
    INSERT INTO account (name, username, password, admin)
    VALUES (?, ?, ?, ?);
    
Admin-status määräytyy sen mukaan, onko luotava käyttäjä ensimmäinen sovellukseen luotava käyttäjä. Tämä voidaan tarkistaa seuraavalla kyselyllä

    SELECT COUNT(*)
    FROM account;

## Kirjautumattomana käyttäjänä haluan äänestää kyselyissä, joissa se on mahdollista.

    INSERT INTO answer (answer_option_id, poll_id, date) 
    VALUES (?, ?, ?);
    
Edellisen kyselyn answer_option_id saadaan jälleen kyselyllä

    SELECT answer_option.id 
    FROM answer_option 
    WHERE answer_option.poll_id = ? AND answer_option.option = ? 
    LIMIT 1;

## Tavallisena käyttäjänä haluan kirjautua sisään.
Tarkistetaan, onko käyttjätunnus ja salasana oikein eli haetaan käyttäjä tietokannasta käyttäjätunnuksen perusteella

    SELECT *
    FROM account
    WHERE account.username = ?
    LIMIT 1;

## Tavallisena käyttäjänä haluan vaihtaa käyttäjätunnustani ja salasanaani.
Sovelluksessa päivitykset tapahtuvat eri sivuilla.

    UPDATE account 
    SET username = ?
    WHERE account.id = ?;
    
    UPDATE account
    SET password = ?
    WHERE account.id = ?;

## Admin-käyttäjänä haluan, että voin poistaa käyttäjän sovelluksesta.
Ennen varsinaisen käyttäjän poistamista poistetaan kaikki siihen liittyvä tieto. Ensin etsitään käyttäjän luomat kyselyt

    SELECT * 
    FROM poll
    WHERE poll.creator_id = ?;
    
Sitten poistetaan löytyneisiin kyselyihin liittyvät tiedot

    DELETE FROM answer WHERE poll_id = ?;
    DELETE FROM answer_option WHERE poll_id = ?;
    DELETE FROM users_answered WHERE poll_id = ?;
    
Sitten poistetaan kyseisen käyttäjän tiedot kyselyistä, joissa tämä on äänestänyt ja itse kyselyt

    DELETE FROM users_answered WHERE user_id = ?;
    DELETE FROM poll WHERE creator_id = ?;
    
Lopuksi poistetaan käyttäjä

    DELETE FROM account WHERE account.id = ?;

## Admin-käyttäjänä haluan poistaa epäasiallisia kyselyitä.

    DELETE FROM answer WHERE poll_id = ?;
    DELETE FROM answer_option WHERE poll_id = ?;
    DELETE FROM users_answered WHERE poll_id = ?;
    DELETE FROM poll WHERE poll.id = ?;

## Admin-käyttäjänä haluan tarkastella käyttäjien aktiivisuutta.
Katso [kehitysideat]()

    SELECT account.username, COUNT(users_answered.user_id)
    FROM account
    LEFT JOIN users_answered ON users_answered.user_id = account.id
    GROUP BY account.id;
