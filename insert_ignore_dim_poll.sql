/* (if new poll) inserts records into dim_poll
 * 
* parameters: 
* 1. group_name
* 2. month
* 3. year
*/
INSERT OR IGNORE INTO dim_poll (group_fk,month,year)
VALUES ((SELECT group_pk FROM dim_group dg
	 WHERE group_name = ?),?,?);