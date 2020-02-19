User stories

As a user:
- I can register as a user `INSERT INTO Account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)`
- I can login
- I can logout

- I can see a list of species `SELECT * FROM Species`
- I can add a new species with description, category and regions `INSERT INTO Species (name, description, category) VALUES (?, ?, ?)`
- I can go to the species' profile page where I can see the species' name, description and category
`SELECT * FROM Species WHERE species.id = ?`
- I can edit the species' information `UPDATE Species SET name=?, descpription=?, category=? WHERE species.id = ?`
- I can delete a species from the database `DELETE FROM Species WHERE species.id = ?`

- I can add an observation related to a certain species `INSERT INTO Observation (account_id, species_id) VALUES (?, ?)`
- I can add description, date and coordinates to the observation `UPDATE Observation SET descpription=?, date=?, ncoordinates=?, ecoordinates=? WHERE observation.id = ?`
- I can go to my profile page `SELECT * FROM Account WHERE account.id=?`
- I can view all my observations on my profile page `SELECT * FROM Observation LEFT JOIN Account ON Observation.account_id = Account.id WHERE Account.id = ?`

- I can add a new region `INSERT INTO Region (name, description) VALUES (?, ?)`


