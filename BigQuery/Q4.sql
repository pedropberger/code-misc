-- Question 4

-- In terms of quality of answers (as measured by the number of favorites and comments received), which monthly cohorts of registered users produced the best answers?

-- Coorte é o mês de nascimento do usuário, calcular a média das "notas médias" dos usuários por creation_date

/* Nós temos duas tres formas de analisar essa questão. A primeira é considerando a quantidade média de favoritos recebidos por resposta por usuário, a segunda apenas o número de comentários recebidos por resposta e por usuário e a terceira é utilizando uma média ponderada dos favoritos e comentários por resposta por usuário.

É importante utilizar a média como medida de qualidade porque se usarmos apenas valores absolutos, um usuário que fez poucoas respostas porém sempre com boas avaliações poderia ser considerado de menos qualidade que um usuário que recebe poucas comentários e favoritos em suas respostas porém publica muitas respostas. Exemplo: User1: 230 favoritos em 23 respostas, User2: 300 favoritos em 400 respostas.

O conceito de coorte utilizado é o mês de registro: https://en.wikipedia.org/wiki/Cohort_(statistics)
*/


--TABELA QUE CALCULA A MÉDIA POR USUÁRIO E DEPOIS A MÉDIA DOS USUÁRIOS DA COORTE

SELECT AVG(Comments) as Quality_rate, date_trunc(creation_date, month) as user_creation_month
from
(
select AVG(cast(a.favorite_count as NUMERIC)) as Favorites, AVG(a.comment_count) as Comments, a.owner_user_id as owner_user_id, b.creation_date as creation_date
from
 `bigquery-public-data.stackoverflow.posts_answers` as a
join
 `bigquery-public-data.stackoverflow.users` as b
on a.owner_user_id = b.id
where b.creation_date > '2019-01-01'
GROUP BY 3, 4
)
GROUP BY 2
ORDER BY 2 ASC


/*
select AVG(cast(a.favorite_count as NUMERIC)) as Favorites, AVG(a.comment_count) as Comments, date_trunc(b.creation_date, month) as creation_month
from
 `bigquery-public-data.stackoverflow.posts_answers` as a
join
 `bigquery-public-data.stackoverflow.users` as b
on a.owner_user_id = b.id
where b.creation_date > '2019-01-01'
GROUP BY 3
ORDER BY 2 ASC -- Because users produced the best answers
*/
