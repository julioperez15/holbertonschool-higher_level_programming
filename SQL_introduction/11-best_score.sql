-- This script lists all records with a score >= 10 in the second_table in the current database, ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
