## User stories

### As a user:
- I can register as a user `INSERT INTO Account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)`
- I can login
- I can logout

- I can see a list of species `SELECT * FROM Species`
- I can see a list of species by region `SELECT * FROM Species LEFT JOIN RegionSpecies ON RegionSpecies.species_id = Species.id LEFT JOIN Region ON Region.id = RegionSpecies.region_id WHERE Region.id = ?`
- I can go to the species' profile page where I can see the species' name, description and category
`SELECT * FROM Species WHERE species.id = ?`


- I can add an observation related to a certain species `INSERT INTO Observation (account_id, species_id) VALUES (?, ?)`
- I can add description, date and coordinates to the observation `UPDATE Observation SET descpription=?, date=?, ncoordinates=?, ecoordinates=? WHERE observation.id = ?`
- I can go to my profile page 
- I can view all my observations on my profile page `SELECT Species.name, Observation.description, Observation.date, Observation.ncoordinates, Observation.ecoordinates, Observation.id  FROM Species INNER JOIN Observation ON Observation.species_id = Species.id INNER JOIN Account ON Observation.account_id = Account.id WHERE Account.id = ? `


### As an admin:

Same as a user plus:

- I can add a new species with description, category and regions `INSERT INTO Species (name, description, category) VALUES (?, ?, ?)`
- I can add a new region `INSERT INTO Region (name, description) VALUES (?, ?)`
- I can edit the species' information `UPDATE Species SET name=?, descpription=?, category=? WHERE species.id = ?`
- I can delete a species from the database `DELETE FROM Species WHERE species.id = ?`



