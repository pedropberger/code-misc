-- Question 7
-- What are the top few topics that are popular and trending but are not being answered?

with tags as (SELECT tag, COUNT(*) total_questions, datas, sum(comment) comment, sum(answer) answer, sum(favorite) favorite, sum(comment + answer + favorite)+count(*) engagement
FROM (
  SELECT SPLIT(tags, '|') tags, date_trunc(creation_date, month) as datas, comment_count comment, answer_count answer, favorite_count favorite
  FROM `bigquery-public-data.stackoverflow.posts_questions` a
  WHERE EXTRACT(YEAR FROM creation_date)>=2019
), UNNEST(tags) tag
GROUP BY 1, 3
ORDER BY 2 DESC), toptags as (select tag, sum(total_questions) total from tags group by tag order by 2 desc limit 10)

SELECT t.*,  FROM tags t
INNER JOIN toptags tt
on t.tag = tt.tag
order by tag asc
