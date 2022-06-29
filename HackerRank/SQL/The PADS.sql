select Name + '('+left(Occupation, 1)+')'
from occupations
order by Name asc

select 'There are a total of', count(occupation), lower (occupation) + 's.'
from occupations
group by occupation
order by count(occupation), occupation asc

/* This is a hard one for a begginer, we learn the use of "+" to concat the data and the use of "lower" and "left" */
