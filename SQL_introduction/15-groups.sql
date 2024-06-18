-- This script lists the number of records with the same score in the second_table in the current database
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
