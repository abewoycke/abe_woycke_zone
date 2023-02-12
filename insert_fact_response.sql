/* inserts records into fact_response
* parameters:
* 1. submitted_name
* 2. group_name
* 3. month
* 4. year
* 5. group_name
* 6. submitted_dt
* 7. poll_option
* 8. response
*/

INSERT INTO fact_response (participant_fk,poll_fk,group_fk,submitted_dt, poll_option, response)
VALUES (
-- participant_fk
(SELECT participant_pk FROM dim_participant dp
WHERE submitted_name = ?),
-- poll_fk
(SELECT poll_pk FROM dim_poll
WHERE group_fk = (SELECT group_pk FROM dim_group dg
WHERE group_name = ?) AND month = ? AND year = ?),
-- group_fk	
(SELECT group_pk FROM dim_group dg
WHERE group_name = ?),
-- submitted_dt, poll_option, response	
?, ?, ?);