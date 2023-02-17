/* query to display poll results for a given poll
 * 
 * parameters:
 * 1. month (int)
 * 2. year (int)
 * 3. group_name (lower case str)
 */

WITH poll AS
-- filter by parameterized month and year
	(SELECT * FROM dim_poll
	WHERE month = ?
	AND year = ?),
-- filter by group name
dg AS
	(SELECT * FROM dim_group
	WHERE group_name = ?)
SELECT DISTINCT
	REPLACE(poll_option, '-', ' ') AS date,
	SUM(response.response) OVER (PARTITION BY response.poll_option) AS responses
FROM fact_response response
INNER JOIN poll
	ON response.poll_fk = poll.poll_pk
INNER JOIN dg
	ON response.group_fk = dg.group_pk
ORDER BY
	responses DESC