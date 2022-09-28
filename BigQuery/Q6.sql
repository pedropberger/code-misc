# Question 6
# Is the problem of unhelpful users (define this yourself) getting better or worse?

-- Definir unhelpfull: Usuários que não postam respostas!
-- Unhelpfull: ou usuários que postam respostas de baixo impacto!

-- usar id, owner_user_ide, media(score) do post_answers

-- Unhelpful defintion: usuários que postam respostas frequentemente porém tem score negativo


/*
with unhelpful as
(
select owner_user_id, AVG(score) as Score, count(id) as Answers_posted
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
where creation_date > '2019-01-01'
group by 1
order by Score asc
)

select count(owner_user_id) from unhelpful

*/
/*
select owner_user_id, score, id, date_trunc(creation_date, month) as creation_month
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
where creation_date > '2019-01-01'
*/

with unhelpful as (
select owner_user_id, AVG(score) as Score, count(id) as Answers_posted, creation_month
FROM
  (select owner_user_id, score, id, date_trunc(creation_date, month) as creation_month
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
where creation_date > '2019-01-01')
group by 1, 4
having Score < 0
order by Score asc
)

select count(owner_user_id) as unhelpful_users, creation_month
from unhelpful
group by 2
