-- Question 2
-- How has the participation rate (questions, answers, comments) of users changed in the last 3 months, compared with the period before?


-- contagem de usuários que fazem questões

--WITH questions as
(select count(distinct(owner_user_id)) as users_questions, --date_trunc(creation_date, month) as creation_month, --DATE_TRUNC(CAST('2021-01-01' AS DATE), MONTH) AS month,
FROM
  `bigquery-public-data.stackoverflow.posts_questions`
where creation_date > '2021-12-01' and creation_date < '2022-03-01')

-- contagem de usuários que fazem respostas
UNION ALL
--WITH answers as
(select count(distinct(owner_user_id)) as users_answers, --date_trunc(creation_date, month) as creation_month, --DATE_TRUNC(CAST('2021-01-01' AS DATE), MONTH) AS month,
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
where creation_date > '2021-12-01' and creation_date < '2022-03-01')

-- contagem de usuários que comentam 
UNION ALL
--WITH comments as 
(select count(distinct(user_id)) as users_coments, --date_trunc(creation_date, month) as creation_month, --DATE_TRUNC(CAST('2021-01-01' AS DATE), MONTH) AS month,
FROM
  `bigquery-public-data.stackoverflow.comments`
where creation_date > '2021-12-01' and creation_date < '2022-03-01')

--select a.users_coments
--from comments as a
--join answers as b

-- usar função WITH para criar 3 tabelas e depois juntar
-- Pesquisar o comparado com o mesmo período anterior -> deve ser algo especial
