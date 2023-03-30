/* Top Poll Results
 * Parameters: group, month, year
*/

WITH
raw AS (
	SELECT * FROM response
	WHERE crew = ? --parameter: crew
	AND month = ? --parameter: month
	AND year = ? --parameter: year
	),
most_recent AS (
	SELECT DISTINCT
		participant,
		MAX(submitted_dt) OVER (PARTITION BY participant) AS max_subm_dt
	FROM raw
	),
filtered AS (
	SELECT
		*
	FROM
		raw
	INNER JOIN
		most_recent
	ON raw.participant = most_recent.participant
	AND raw.submitted_dt = most_recent.max_subm_dt
),
top_five AS (
SELECT DISTINCT
	month,
	day,
	time_description,
	SUM(response) OVER (PARTITION BY day,time_description) AS "Headcount"
FROM
	filtered
ORDER BY "Headcount" DESC
LIMIT 5
)
SELECT
top_five.month AS "Month",
top_five.day AS "Day",
top_five.time_description AS "Time",
top_five."Headcount",
filtered.participant AS "Folks Available (Submitted Name)"
FROM top_five
LEFT JOIN filtered
ON top_five.day = filtered.day
AND top_five.time_description = filtered.time_description
INNER JOIN
	most_recent
	ON filtered.participant = most_recent.participant
	AND filtered.submitted_dt = most_recent.max_subm_dt