/* Instantiate abe_woycke_zone polling 'db' */
CREATE TABLE IF NOT EXISTS response (
	response_pk INTEGER PRIMARY KEY,
	crew TEXT NOT NULL,
	participant TEXT NOT NULL,
	month INTEGER NOT NULL,
	day INTEGER NOT NULL,
	year INTEGER NOT NULL,
	time_description TEXT NOT NULL,
	response INTEGER NOT NULL,
	submitted_dt TEXT NOT NULL);