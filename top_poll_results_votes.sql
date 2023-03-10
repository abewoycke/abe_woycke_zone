--group of interest
WITH goi AS
	(SELECT group_pk
	FROM dim_group
	WHERE group_name = ? --PARAMETER
	),
--poll of interest
poi AS
	(SELECT poll_pk
	FROM dim_poll poll
	JOIN goi ON
	poll.group_fk = goi.group_pk
	WHERE month = ? --PARAMETER
	AND year = ?), --PARAMETER
--fact_response without dupes
response AS
	(SELECT DISTINCT
	response.*
	FROM fact_response response
	INNER JOIN
		(SELECT
		MAX(response_pk) OVER (PARTITION BY participant_fk,poll_fk,poll_option) AS max_response_pk
		FROM fact_response
		) most_recent
		ON response.response_pk = most_recent.max_response_pk
	ORDER BY 1),
--votes
votes AS
	(SELECT DISTINCT
		response.poll_option,
		SUM(response.response) OVER(PARTITION BY response.poll_option) AS "Votes"
	FROM response
		JOIN poi
			ON response.poll_fk = poi.poll_pk
	ORDER BY "Votes" DESC),
--ranks
ranks AS
(SELECT
	votes.poll_option,
	votes.Votes,
	DENSE_RANK() OVER(ORDER BY Votes DESC) AS ranking
FROM votes),
top_result AS
--top_poll_results
(
SELECT
	poll_option AS "Top Poll Result",
	Votes
FROM ranks
WHERE ranks.ranking = 1
)
SELECT
replace("Top Poll Result",'-',' '),
Votes,
dp.submitted_name
FROM top_result
LEFT JOIN response
	ON top_result."Top Poll Result" = response.poll_option
LEFT JOIN dim_participant dp 
	ON response.participant_fk = dp.participant_pk
;