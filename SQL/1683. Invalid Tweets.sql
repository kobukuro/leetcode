# Database
# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets tw
WHERE LENGTH(tw.content) > 15
