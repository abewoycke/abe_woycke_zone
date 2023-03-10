-- group_pk (1=sandwich, 2=taustin_dnd, 3=comm_601)
-- poll_pk (1=sandwich 3/2023, 2=taustin_dnd 3/2023, 3=comm_601 3/2023)
select distinct response.poll_option, SUM(response.response) OVER(PARTITION BY response.poll_option) AS "Votes" from fact_response response
where poll_fk = 1
order by "Votes" desc, 1

SELECT DISTINCT
    response.poll_option,
    