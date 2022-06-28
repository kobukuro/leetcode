# Database
# Write your MySQL query statement below
SELECT emp.employee_id, temp.team_size
FROM Employee emp
         JOIN
     (
         SELECT emp.team_id, COUNT(*) team_size
         FROM Employee emp
         GROUP BY emp.team_id
     ) temp on (emp.team_id = temp.team_id)