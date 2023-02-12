
-- (if new polling group) inserts records into dim_group
INSERT OR IGNORE INTO dim_group (group_name)
VALUES (?);

-- (if new submitted name) inserts records into dim_participant
INSERT OR IGNORE INTO dim_participant (submitted_name)
VALUES (?);

-- (if new poll) inserts records into dim_poll
INSERT OR IGNORE INTO dim_poll (group_fk,month,year)
VALUES ((SELECT group_pk FROM dim_group dg
	 WHERE group_name = ?),2,2023);

-- inserts new records into fact_response
INSERT INTO fact_response (submitted_dt, poll_option, response)
VALUES ({},{},{})


---------------------------



INSERT INTO fact_response (participant_fk,poll_fk,group_fk,submitted_dt, poll_option, response)
VALUES (
-- participant_fk
(SELECT participant_pk FROM dim_participant dp
WHERE submitted_name = 'Zac'),
-- poll_fk
(SELECT poll_pk FROM dim_poll
WHERE group_fk = (SELECT group_pk FROM dim_group dg
WHERE group_name = 'sandwich') AND month = 2 AND year = 2023),
-- group_fk	
(SELECT group_pk FROM dim_group dg
WHERE group_name = 'sandwich'),
-- submitted_dt, poll_option, response	
2023, 'March 6th 7pm', 1);