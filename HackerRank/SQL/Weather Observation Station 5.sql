-- Easy level
-- The plus in this exercise is the use of 2 querys and ORDER BY and LEN funcion

SELECT TOP 1 CITY,
LEN(CITY)

FROM STATION
ORDER BY LEN (CITY), CITY

SELECT TOP 1 CITY,
LEN(CITY)

FROM STATION
ORDER BY LEN (CITY) DESC, CITY ASC

