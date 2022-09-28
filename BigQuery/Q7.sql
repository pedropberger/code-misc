# Question 7
# What are the top few topics that are popular and trending but are not being answered?

/*
select tags, answer_count
FROM
  `bigquery-public-data.stackoverflow.posts_questions`
where answer_count = 0
limit 100
*/

-- tentar criar medida de tendência, ver quais estão sendo mais perguntados por agora

-- a query abaixo trás os tópicos mais populares

  #standardSQL
SELECT tag, COUNT(*) Count, SUM(Answer_count) Answers, IEEE_DIVIDE(Count(tag),sum(Answer_count)) as ratio --date_trunc(creation_date, month) as creation_month
FROM (
  SELECT SPLIT(tags, '|') tags, creation_date, answer_count
  FROM `bigquery-public-data.stackoverflow.posts_questions` a
  WHERE EXTRACT(YEAR FROM creation_date)>=2019
), UNNEST(tags) tag
GROUP BY 1
ORDER BY 2 DESC
LIMIT 100
