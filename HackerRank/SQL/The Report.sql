SELECT IIF(Grades.Grade < 8, NULL, Students.Name), Grades.Grade, Marks
FROM Students
JOIN Grades
ON Marks BETWEEN Min_Mark AND MAX_MARK
WHERE Marks > 8
ORDER BY Grade DESC, Name ASC
