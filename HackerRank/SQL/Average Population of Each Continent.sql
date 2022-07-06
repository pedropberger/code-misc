select country.continent, round(avg(city.population),0)
from city
inner join country
on city.countrycode = country.code
group by country.continent