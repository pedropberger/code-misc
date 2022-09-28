select count(distinct(owner_user_id)) as users, date_trunc(creation_date, month) as creation_month, --DATE_TRUNC(CAST('2021-01-01' AS DATE), MONTH) AS month,
FROM
  `bigquery-public-data.stackoverflow.posts_questions`
where creation_date >= '2019-01-01' and creation_date < '2022-03-01'
group by 2
order by 2 desc
