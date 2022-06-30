# Database
# Write your MySQL query statement below
SELECT uni.unique_id, emp.name
FROM Employees emp
         LEFT JOIN EmployeeUNI uni on (emp.id = uni.id)

