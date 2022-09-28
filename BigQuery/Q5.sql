# Question 5
# What category (tag) of questions are driving the most engagement (questions, answers, comments, favorites), and how has this changed over time?

-- separar as tags e fazer o comparativo do engajamento ao longo do tempo

-- rever no python

-- fazer uma consulta para cada contagem (questions, answers, comments, favorites)

#standardSQL

with tags as (SELECT tag, COUNT(*) total_questions, datas, sum(comment) comment, sum(answer) answer, sum(favorite) favorite, (sum(comment) + sum(answer) + sum(favorite)+count(*)) engagement
FROM (
  SELECT SPLIT(tags, '|') tags, date_trunc(creation_date, month) as datas, comment_count comment, answer_count answer, favorite_count favorite
  FROM `bigquery-public-data.stackoverflow.posts_questions` a
  WHERE EXTRACT(YEAR FROM creation_date)>=2019
), UNNEST(tags) tag
GROUP BY 1, 3
ORDER BY 2 DESC), toptags as (select tag, sum(total_questions) total from tags group by tag order by 2 desc limit 10)

SELECT t.* FROM tags t
INNER JOIN toptags tt
on t.tag = tt.tag
order by tag asc



