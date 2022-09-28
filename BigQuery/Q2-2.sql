-- Question 2
-- How has the participation rate (questions, answers, comments) of users changed in the last 3 months, compared with the period before?

WITH Trimestre as
(select count(distinct(owner_user_id)) as Contagem, 'questions' as Item, 'T0' as Trimester
FROM
  `bigquery-public-data.stackoverflow.posts_questions`
where creation_date between '2021-12-01' and '2022-03-01'
--where creation_date between DATE_ADD(creation_date, INTERVAL -180 DAY) and DATE_ADD(creation_date, INTERVAL -90 DAY)

UNION ALL

select count(distinct(owner_user_id)) as Contagem, 'answers' as Item, 'T0' as Trimester
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
where creation_date > '2021-12-01' and creation_date < '2022-03-01'
--where creation_date > DATE_ADD(creation_date, INTERVAL -90 DAY)

UNION ALL

Select count(distinct(user_id)) as Contagem, 'comments' as Item, 'T0' as Trimester
FROM
  `bigquery-public-data.stackoverflow.comments`
where creation_date between '2021-12-01' and '2022-03-01'
--where creation_date > DATE_ADD(creation_date, INTERVAL -90 DAY)

UNION ALL

select count(distinct(owner_user_id)) as Contagem, 'questions' as Item, 'T-1' as Trimester
FROM
  `bigquery-public-data.stackoverflow.posts_questions`
where creation_date between '2021-09-01' and '2022-12-01'
--where creation_date > DATE_ADD(creation_date, INTERVAL -180 DAY) and creation_date < DATE_ADD(creation_date, INTERVAL -90 DAY)

UNION ALL

select count(distinct(owner_user_id)) as Contagem, 'answers' as Item, 'T-1' as Trimester
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
where creation_date between '2021-09-01' and '2022-12-01'
--where creation_date > DATE_ADD(creation_date, INTERVAL -180 DAY) and creation_date < DATE_ADD(creation_date, INTERVAL -90 DAY)

UNION ALL

Select count(distinct(user_id)) as Contagem, 'comments' as Item, 'T-1' as Trimester
FROM
  `bigquery-public-data.stackoverflow.comments`
where creation_date between '2021-09-01' and '2022-12-01'
--where creation_date > DATE_ADD(creation_date, INTERVAL -180 DAY) and creation_date < DATE_ADD(creation_date, INTERVAL -90 DAY)

)

SELECT * FROM Trimestre
