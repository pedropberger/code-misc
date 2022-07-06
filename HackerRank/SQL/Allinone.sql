select round(avg(population),0)
from city

SELECT NAME
FROM EMPLOYEE
ORDER BY NAME

select name from employee where salary > 2000 and months < 10
order by employee_id asc

--MYSQL CODE
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTR(NAME,-3,3), ID ASC

--SQL SERVER
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME,3), ID ASC

select sum(population)
from city
where countrycode='JPN'

select w.id, p.age, w.coins_needed, w.power
from wands as w
join wands_property as p
on w.code = p.code
where w.coins_needed = (select min(coins_needed)
                       from wands
                       join wands_property
                       on wands.code = wands_property.code
                       where wands_property.is_evil = 0 and wands_property.age = p.age and w.power = wands.power)
order by w.power desc, p.age desc

SELECT sum(city.population)
FROM city
INNER JOIN country
ON City.Countrycode = COUNTRY.Code
WHERE CONTINENT = 'Asia'

select max(population) - min(population)
from city

select avg(population)
from city
where district = 'California'

select count(name)
from city
where population > 100000

select sum(population)
from city
where district = "California"


select CAST(CEILING(avg(cast(salary as float)) - avg(cast(replace(salary,0,'') as FLOAT))) AS INT)
from EMPLOYEES

/* problematic question, use ceil function in mysql
select ceil(avg(salary) - avg(cast(replace(salary,0,'') as DECIMAL)))
from EMPLOYEES
*/
select Name + '('+left(Occupation, 1)+')'
from occupations
order by Name asc

select 'There are a total of', count(occupation), lower (occupation) + 's.'
from occupations
group by occupation
order by count(occupation), occupation asc


SELECT IIF(Grades.Grade < 8, NULL, Students.Name), Grades.Grade, Marks
FROM Students
JOIN Grades
ON Marks BETWEEN Min_Mark AND MAX_MARK
WHERE Marks > 8
ORDER BY Grade DESC, Name ASC

select hackers.hacker_id, hackers.name
from hackers
join submissions
on hackers.hacker_id = submissions.hacker_id
join challenges
on submissions.challenge_id = challenges.challenge_id
join difficulty
on challenges.difficulty_level = difficulty.difficulty_level
where difficulty.score = submissions.score
group by hackers.hacker_id, hackers.name
having count(*) > 1
order by count(*) desc, hackers.hacker_id asc


SELECT MAX(SALARY*MONTHS), COUNT(*)
FROM EMPLOYEE
WHERE (SALARY*MONTHS) = (SELECT MAX(SALARY*MONTHS)
                         FROM EMPLOYEE



SELECT
    CASE
--        WHEN A = B AND B = C THEN 'Equilateral'
--        WHEN A = B or A = C or B = C THEN 'Isosceles'
--        WHEN A<>B AND B<>C THEN 'Scalene'
--        WHEN A + B <= C or A + C <= B or B + C <= A THEN 'Not A Triangle'
        WHEN A + B <= C or A + C <= B or B + C <= A THEN 'Not A Triangle'
        WHEN A = B and B = C THEN 'Equilateral'
        WHEN A = B or A = C or B = C THEN 'Isosceles'
        WHEN A <> B and B <> C THEN 'Scalene'
    END TUPLE
    
FROM TRIANGLES;
