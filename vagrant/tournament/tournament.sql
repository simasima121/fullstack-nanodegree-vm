-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament
CREATE TABLE players( id SERIAL PRIMARY KEY,
											name TEXT,
											wins INTEGER DEFAULT 0,
											games_played INTEGER DEFAULT 0);

CREATE TABLE matches( winning_id INTEGER,
											losing_id INTEGER);

