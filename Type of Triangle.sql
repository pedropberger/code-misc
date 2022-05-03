
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
