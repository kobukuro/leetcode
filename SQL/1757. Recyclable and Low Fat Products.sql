# Database
# Write your MySQL query statement below
SELECT pro.product_id
FROM Products pro
WHERE pro.low_fats = 'Y'
  and pro.recyclable = 'Y'