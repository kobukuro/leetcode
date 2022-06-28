# Database
# Write your MySQL query statement below
SELECT stu.id, stu.name
FROM Students stu
         LEFT JOIN Departments dep on (stu.department_id = dep.id)
WHERE dep.name is NULL