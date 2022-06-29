SELECT MAX(SALARY*MONTHS), COUNT(*)
FROM EMPLOYEE
WHERE (SALARY*MONTHS) = (SELECT MAX(SALARY*MONTHS)
                         FROM EMPLOYEE)
/* we have moe forms to aswer this, but will need to create another tables */
