# Tietokanta (kesken)

## CREATE TABLE-lauseet

### Poll

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


### Account

    CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (admin IN (0, 1))
    );

### Users_answered

    CREATE TABLE users_answered (
	id INTEGER NOT NULL, 
	poll_id INTEGER, 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(poll_id) REFERENCES poll (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
    );

### Answer_option

    CREATE TABLE answer_option (
	id INTEGER NOT NULL, 
	option VARCHAR NOT NULL, 
	poll_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(poll_id) REFERENCES poll (id)
    );

### Answer

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

![Tietokantakaavio](/documentation/Tietokantakaavio.png)
