-- (if new submitted name) inserts records into dim_participant
-- parameter: submitted_name
INSERT OR IGNORE INTO dim_participant (submitted_name)
VALUES (?);