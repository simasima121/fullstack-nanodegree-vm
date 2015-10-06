-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

/* what needs to be in the database?

1) players - id (serial), name, who they've played (matches), their score (playerStandings), 
who won/lost (reportMatch), who next opponent is (swissPairings)

2) unique id for tournaments

- when players add to tournament, database should create unique id for each player using serial
- SQL aggregation when wanting to count or adding up
- try using loop in database queries
- if database calls get confusing use views

will have player table with name and id
have another table with player id, their wins, the matches they have played

*/

CREATE DATABASE tournament;
\c tournament
CREATE TABLE players( id SERIAL PRIMARY KEY,
											name TEXT);

CREATE TABLE matches( player_id SERIAL REFERENCES players (id) ON DELETE CASCADE,
										  wins INTEGER,
										  games_played INTEGER);

