-- Question 3
-- How does the reputation growth rate of users who answer questions frequently compare with those who do so less frequently?
-- Qual a taxa de crescimendo da reputação "reputation" dos usuários que respondem questões frequentemente comparado com os que respondem menos frequentemente

select a.display_name, a.reputation, b.answers
FROM
  `bigquery-public-data.stackoverflow.users` as a
JOIN (select count(id) as answers, owner_user_id
from
  `bigquery-public-data.stackoverflow.posts_answers`
  group by 2) as b ON a.id = b.owner_user_id
where creation_date > '2019-01-01'

-- Fazer uma regressão e tirar onda
