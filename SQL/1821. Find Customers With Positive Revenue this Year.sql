# Database
# Write your MySQL query statement below
SELECT customer_id
FROM Customers cu
WHERE cu.year = 2021
  AND cu.revenue > 0
