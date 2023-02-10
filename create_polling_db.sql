/* Instantiate abe_woycke_zone polling db
 */
CREATE TABLE IF NOT EXISTS dim_participant (
	participant_pk INTEGER PRIMARY KEY,
	submitted_name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS dim_poll (
	poll_pk INTEGER PRIMARY KEY,
	month INTEGER NOT NULL,
	year INTEGER NOT NULL,
	squad TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS fact_response (
	response_pk INTEGER PRIMARY KEY,
	participant_fk INTEGER NOT NULL,
	poll_fk INTEGER NOT NULL,
	submitted_dt INTEGER NOT NULL,
	poll_option TEXT NOT NULL,
	response INTEGER DEFAULT 0,
	FOREIGN KEY (participant_fk)
		REFERENCES dim_participant (participant_pk)
			ON DELETE CASCADE
			ON UPDATE NO ACTION
	FOREIGN KEY (poll_fk)
		REFERENCES dim_poll (poll_pk)
			ON DELETE CASCADE
			ON UPDATE NO ACTION
);