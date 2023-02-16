-- script that displays the top 3 of cities
-- temp during Jul Aug ordered by temperature

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
