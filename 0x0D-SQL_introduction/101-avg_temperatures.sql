-- A script that displays the average temp by city ordered by temp

SELECT city, AVG((temperature * 1.8) + 32) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
