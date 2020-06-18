# Tietokanta

Paikallisesti sovelluksessa on käytössä SQLite-tietokantahallintajärjestelmä ja Herokussa PostgreSQL.

## CREATE TABLE-lauseet

En kokenut tarvetta tehdä abstraktia luokkaa tietokannalle, sillä vain kunkin taulun id toistuu kaikissa tauluissa.

### poll
Taulu *poll* sisältää kyselyn kysymyksen, kuvauksen, tiedon kyselyn anonyymiydestä, luomispäivämäärän sekä kyselyn luojan id:n.

    CREATE TABLE poll (
	id INTEGER NOT NULL, 
	question VARCHAR NOT NULL, 
	description VARCHAR, 
	anonymous BOOLEAN NOT NULL, 
	created_date DATETIME, 
	creator_id INTEGER, 
	PRIMARY KEY (id), 
	CHECK (anonymous IN (0, 1)), 
	FOREIGN KEY(creator_id) REFERENCES account (id)
    );


### account
Taulu *account* sisältää käyttäjään liittyvät tiedot.

    CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (admin IN (0, 1))
    );

### users_answered
Taulu *users_answered* sisältää tiedot siitä, mihin kyselyyn kukin (kirjautunut) käyttäjä on jo vastannut.

    CREATE TABLE users_answered (
	id INTEGER NOT NULL, 
	poll_id INTEGER, 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(poll_id) REFERENCES poll (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
    );

### answer_option
Taulu *answer_option* sisältää kyselyiden vastausvaihtoehdot.

    CREATE TABLE answer_option (
	id INTEGER NOT NULL, 
	option VARCHAR NOT NULL, 
	poll_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(poll_id) REFERENCES poll (id)
    );

### answer
Taulu *answer* sisältää käyttäjien antamat vastaukset kyselyihin.

    CREATE TABLE answer (
	id INTEGER NOT NULL, 
	answer_option_id INTEGER NOT NULL, 
	poll_id INTEGER NOT NULL, 
	date DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(answer_option_id) REFERENCES answer_option (id), 
	FOREIGN KEY(poll_id) REFERENCES poll (id)
    );
    
## Indeksit
    
Pääavaimissa on automaattisesti indeksöinti. Lisäksi indeksointi lisätään seuraaviin sarakkeisiin nopeuttamaan hakuja:

    CREATE UNIQUE INDEX ix_poll_question ON poll (question);
    CREATE UNIQUE INDEX ix_account_username ON account (username);
    CREATE INDEX ix_users_answered_user_id ON users_answered (user_id);
    CREATE INDEX ix_users_answered_poll_id ON users_answered (poll_id);
    CREATE INDEX ix_answer_option_poll_id ON answer_option (poll_id);
    CREATE INDEX ix_answer_poll_id ON answer (poll_id);
    CREATE INDEX ix_answer_answer_option_id ON answer (answer_option_id);

## Tietokantakaavio

Viiteavaimet on korostettu vaaleansinisellä värillä. Pääavaimet on tummennettu.

![Tietokantakaavio](/documentation/Dbdiagram.png)
