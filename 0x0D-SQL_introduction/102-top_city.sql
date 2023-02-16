-- script that displays the top 3 of cities temp during Jul & Aug ordered by temperature

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
