/* Instantiate abe_woycke_zone polling db */

CREATE TABLE IF NOT EXISTS dim_group (
	group_pk INTEGER PRIMARY KEY,
	group_name TEXT NOT NULL,
	UNIQUE(group_name)
);

CREATE TABLE IF NOT EXISTS dim_participant (
	participant_pk INTEGER PRIMARY KEY,
	submitted_name TEXT NOT NULL,
	UNIQUE(submitted_name)
);

CREATE TABLE IF NOT EXISTS dim_poll (
	poll_pk INTEGER PRIMARY KEY,
	group_fk INTEGER NOT NULL,
	month INTEGER NOT NULL,
	year INTEGER NOT NULL,
	UNIQUE(month,year,group_fk)
	FOREIGN KEY (group_fk)
		REFERENCES dim_group (group_pk)
			ON DELETE CASCADE
			ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_response (
	response_pk INTEGER PRIMARY KEY,
	participant_fk INTEGER NOT NULL,
	poll_fk INTEGER NOT NULL,
	group_fk INTEGER NOT NULL,
	poll_option TEXT NOT NULL,
	response INTEGER DEFAULT 0,
	FOREIGN KEY (participant_fk)
		REFERENCES dim_participant (participant_pk)
			ON DELETE CASCADE
			ON UPDATE CASCADE
	FOREIGN KEY (poll_fk)
		REFERENCES dim_poll (poll_pk)
			ON DELETE CASCADE
			ON UPDATE CASCADE
	FOREIGN KEY (group_fk)
		REFERENCES dim_group (group_pk)
			ON DELETE CASCADE
			ON UPDATE CASCADE
);