# Database
# Write your MySQL query statement below
SELECT vi.customer_id, COUNT(*) count_no_trans
FROM Visits vi
         LEFT JOIN Transactions tr on (vi.visit_id = tr.visit_id)
WHERE tr.transaction_id is null
GROUP BY vi.customer_id
