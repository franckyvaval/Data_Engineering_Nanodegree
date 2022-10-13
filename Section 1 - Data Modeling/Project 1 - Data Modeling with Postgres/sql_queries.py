# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE table IF NOT EXISTS songplays\
(songplay_id SERIAL PRIMARY KEY, start_time BIGINT, user_id \
varchar, level text, song_id varchar, artist_id varchar,\
session_id varchar, location text, user_agent text) 
""")

user_table_create = ("""CREATE table IF NOT EXISTS users\
(user_id int, first_name text, last_name text, gender text,\
level text)
""")

song_table_create = ("""CREATE table IF NOT EXISTS songs\
(song_id varchar, title text, artist_id varchar,\
year int, duration float)
""")

artist_table_create = ("""CREATE table IF NOT EXISTS artists\
(artist_id varchar, artist_name text, location text,\
latitude float, longitude float)
""")

time_table_create = ("""CREATE table IF NOT EXISTS time\
(start_time timestamp, hour int, day int,\
 weekofyear int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name,\
 last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, \
artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, \
artist_name, location, latitude, longitude) VALUES \
(%s, %s, %s, %s, %s)
""")


time_table_insert = (""" INSERT INTO time (start_time, \
hour, day, weekofyear, month, year, weekday) VALUES \
(%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = (""" SELECT s.song_id AS song_id, a.artist_id AS artist_id FROM ( songs s INNER JOIN artists a ON s.artist_id = a.artist_id) WHERE s.title = %s AND a.artist_name = %s AND s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]