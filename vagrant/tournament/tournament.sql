-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- drop view if exists wins;
-- drop view if exists player_one_matches;
-- drop view if exists player_two_matches;
-- drop view if exists played_matches;

drop table if exists players cascade;
drop table if exists matches cascade;


create table players (player_id serial primary key, name text);
create table matches (match_id serial primary key, player_one_id integer references players(player_id), 
	player_two_id integer references players(player_id), match_winner integer references players(player_id));

-- create table players (player_id serial primary key, name text);
-- create table matches (match_id serial primary key, player_one_id integer, 
-- 	player_two_id integer, match_winner integer);

-- testing purpose
-- create table players (player_id integer primary key, name text);
-- create table matches (match_id serial primary key, player_one_id integer, 
-- 	player_two_id integer, match_winner integer);


-- create view wins as
-- 	select match_winner as winner, count(*) as wins
-- 	from matches
-- 	group by match_winner;

create view wins as 
	select players.player_id as winner, count(matches.match_winner) as wins
	from players left join matches
	on players.player_id = matches.match_winner
	group by players.player_id;

create view player_one_matches as 
	select players.player_id, count(matches.player_one_id) as count
	from players left join matches
	on players.player_id = matches.player_one_id
	group by players.player_id;

create view player_two_matches as
	select players.player_id, count(matches.player_two_id) as count
	from players left join matches
	on players.player_id = matches.player_two_id
	group by players.player_id;

create view played_matches as
	select players.player_id as player, player_one_matches.count + player_two_matches.count as matches
	from players 
	left join player_one_matches
	on players.player_id = player_one_matches.player_id
	left join player_two_matches
	on players.player_id = player_two_matches.player_id;

create view standings as
	select players.player_id, players.name, wins.wins, played_matches.matches
	from players 
	left join wins
	on players.player_id = wins.winner
	left join played_matches
	on players.player_id = played_matches.player
	order by wins.wins desc;


-- test data
-- insert into players values (1, 'Player A');
-- insert into players values (2, 'Player B');
-- insert into matches (player_one_id, player_two_id, match_winner) values (1,2,1);
-- insert into matches (player_one_id, player_two_id, match_winner) values (2,1,1);
-- insert into matches (player_one_id, player_two_id, match_winner) values (1,2,1);
-- insert into matches (player_one_id, player_two_id, match_winner) values (2,1,2);

