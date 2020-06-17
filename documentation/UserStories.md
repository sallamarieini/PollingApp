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

**User story 4:** Tavallisena käyttäjä haluan, että voin muokata luomaani kyselyä.

**User story 5:** Tavallisena käyttäjänä haluan, että voin poistaa luomani kyselyn.

**User story 6:** Tavallisena käyttäjänä haluan, että voin tarkastella kyselyn tuloksia.

**User story 7:** Kyselyn luojana voin päättää, vaatiiko kyselyyn vastaaminen tunnistautumista.

**User story 8:** Tavallisena käyttäjänä haluan etsiä kyselyitä hakusanalla kysymyksen perusteella.

**User story 9:** Tavallisena käyttäjänä haluan tarkastella kaikkia kyselyitä.

**User story 10:** Tavallisena käyttäjänä haluan nähdä yksittäisen kyselyn tiedot tarkemmin.

**User story 11:** Tavallisena käyttäjänä haluan luoda uuden käyttäjätunnuksen.

**User story 12:** Kirjautumattomana käyttäjänä haluan äänestää kyselyissä, joissa se on mahdollista.

**User story 13:** Tavallisena käyttäjänä haluan kirjautua sisään.

**User story 14:** Tavallisena käyttäjänä haluan vaihtaa käyttäjätunnustani ja salasanaani.

**User story 15:** Admin-käyttäjänä haluan, että voin poistaa käyttäjiä sovelluksesta.

**User story 16:** Admin-käyttäjänä haluan poistaa epäasiallisia kyselyitä.

**User sotry 17:** Admin-käyttäjänä haluan tarkastella käyttäjien aktiivisuutta. (katso [kehitysideat]())
