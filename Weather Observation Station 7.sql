-- Use %A to select string ending with a choosed letter

SELECT DISTINCT CITY
FROM STATION
WHERE CITY LIKE '%A' OR CITY LIKE '%E' OR CITY LIKE '%I' OR CITY LIKE '%O' OR CITY LIKE '%U'
