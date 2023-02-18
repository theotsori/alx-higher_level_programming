-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT tv_genres.name, SUM(rating)
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
INNER JOIN hbtn_0d_tvshows_rate ON hbtn_0d_tvshows_rate.tv_show_id = tv_shows.id
GROUP BY tv_genres.id
ORDER BY SUM(rating) DESC;
