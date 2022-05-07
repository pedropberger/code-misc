SELECT sum(city.population)
FROM city
INNER JOIN country
ON City.Countrycode = COUNTRY.Code
WHERE CONTINENT = 'Asia'
