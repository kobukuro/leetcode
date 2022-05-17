#
Database
# Write your MySQL query statement below
SELECT EMAIL
FROM (
         SELECT *, COUNT(*)
         FROM PERSON
         GROUP BY EMAIL
         HAVING COUNT(*) > 1
     ) MODIFIED