-- Script that creates database hbtn_0d_usa and table states
SELECT id, name
FROM cities
WHERE state_id = (
        SELECT Id
		FROM states
        WHERE name = 'California'
)
ORDER BY cities.id;
