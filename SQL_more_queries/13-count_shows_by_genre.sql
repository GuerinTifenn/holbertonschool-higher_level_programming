-- List all genres from hbtn_0d_tvshows and the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id GROUP BY tv_genres.name HAVING number_of_shows > 0 ORDER BY number_of_shows DESC;
