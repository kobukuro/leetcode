#
Database
# Write your MySQL query statement below
select teacher_id, COUNT(subject_id) AS cnt
from (
         select distinct teacher_id, subject_id
         from Teacher) temp
group by temp.teacher_id