Tietokanta Itämeren lajeista, kuten makrolevistä ja vesikasveista. Etusivulla käyttäjä voi tarkastella lajilistoja lajiteltuna esimerkiksi lajityypin tai merialueen mukaan. Jokaisella lajilla on oma tietosivu, josta löytyy lajin tuntomerkit. Lajisivuille käyttäjät voivat lisätä omia havaintojaan kyseisestä lajista. Muut käyttäjät voivat kommentoida havaintoa, esimerkiksi sen luotettavuutta. Omalla profiilisivullaan käyttäjä voi tarkastella kaikkia tekemiään havaintoja. 

### Toimintoja:

- Kirjautuminen
- Lajilistojen näyttäminen eri kriteerein
- Uusien lajisivujen lisääminen (admin)
- Lajisivujen muokkaaminen ja poisto (admin)
- Havaintojen lisääminen lajisivulle 
- Havainnon kommentointi ja/tai peukuttaminen
- Merialueen lisääminen (admin)

![tietokantakaavio](https://github.com/LindaJT/merilajit/blob/master/documentation/tietokantakaavio_final.png)

Linkki Herokussa toimivaan sovellukseen: https://tsoha-merilajit.herokuapp.com/species

Linkki user storyihin: https://github.com/LindaJT/merilajit/blob/master/documentation/user_stories.md

Testitunnukset Herokussa: 
USER role: Käyttäjänimi: hello Salasana: world1
ADMIN role: Käyttäjänimi: admin Salasana: admin1

### Tietokantataulut:

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(20), 
	PRIMARY KEY (id)
)

CREATE TABLE species (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	description VARCHAR(300), 
	category VARCHAR(50), 
	PRIMARY KEY (id)
)

CREATE TABLE region (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	description VARCHAR(300), 
	PRIMARY KEY (id)
)

CREATE TABLE observation (
	id INTEGER NOT NULL, 
	description VARCHAR(300), 
	date DATE, 
	ncoordinates FLOAT, 
	ecoordinates FLOAT, 
	account_id INTEGER NOT NULL, 
	species_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE, 
	FOREIGN KEY(species_id) REFERENCES species (id) ON DELETE CASCADE
)

CREATE TABLE regionspecies (
	region_id INTEGER NOT NULL, 
	species_id INTEGER NOT NULL, 
	PRIMARY KEY (region_id, species_id), 
	FOREIGN KEY(region_id) REFERENCES region (id), 
	FOREIGN KEY(species_id) REFERENCES species (id)
)

```

