-- Table definitions for the tournament project. 
-- 
-- Put your SQL 'create table' statements in this file; also 'create view' 
-- statements if you choose to use it. 
-- 
-- You can write comments in this file by starting them with two dashes, like 
-- these lines here. 
-- First making sure that we are getting a new database and new tables every time by deleting  
-- existing ones 

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

DROP TABLE IF EXISTS players CASCADE; 

DROP TABLE IF EXISTS matches CASCADE; 

-- Then we create the two tables that will be used  
CREATE TABLE players 
  ( 
     player_id SERIAL PRIMARY KEY, 
     name      TEXT 
  ); 

CREATE TABLE matches 
  ( 
     match_id      SERIAL PRIMARY KEY, 
     player_one_id INTEGER REFERENCES players(player_id), 
     player_two_id INTEGER REFERENCES players(player_id), 
     match_winner  INTEGER REFERENCES players(player_id) 
  ); 

-- Finally, we create all the views that will be used in the queries 
-- stored in tournament.py 
CREATE view wins 
AS 
  SELECT players.player_id           AS winner, 
         Count(matches.match_winner) AS wins 
  FROM   players 
         LEFT JOIN matches 
                ON players.player_id = matches.match_winner 
  GROUP  BY players.player_id; 

CREATE view player_one_matches 
AS 
  SELECT players.player_id, 
         Count(matches.player_one_id) AS count 
  FROM   players 
         LEFT JOIN matches 
                ON players.player_id = matches.player_one_id 
  GROUP  BY players.player_id; 

CREATE view player_two_matches 
AS 
  SELECT players.player_id, 
         Count(matches.player_two_id) AS count 
  FROM   players 
         LEFT JOIN matches 
                ON players.player_id = matches.player_two_id 
  GROUP  BY players.player_id; 

CREATE view played_matches 
AS 
  SELECT players.player_id          AS player, 
         player_one_matches.count 
         + player_two_matches.count AS matches 
  FROM   players 
         LEFT JOIN player_one_matches 
                ON players.player_id = player_one_matches.player_id 
         LEFT JOIN player_two_matches 
                ON players.player_id = player_two_matches.player_id; 

CREATE view standings 
AS 
  SELECT players.player_id, 
         players.name, 
         wins.wins, 
         played_matches.matches 
  FROM   players 
         LEFT JOIN wins 
                ON players.player_id = wins.winner 
         LEFT JOIN played_matches 
                ON players.player_id = played_matches.player 
  ORDER  BY wins.wins DESC; 