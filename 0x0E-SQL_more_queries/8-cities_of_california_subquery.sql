-- A script that lists all the cities of carlifornia

USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
) AND states.name = 'California'
ORDER BY cities.id ASC;
