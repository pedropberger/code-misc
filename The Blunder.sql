select CAST(CEILING(avg(cast(salary as float)) - avg(cast(replace(salary,0,'') as FLOAT))) AS INT)
from EMPLOYEES

/* problematic question, use ceil function in mysql
select ceil(avg(salary) - avg(cast(replace(salary,0,'') as DECIMAL)))
from EMPLOYEES
*/
