#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("select count(*) from players;")
    query_result = cur.fetchall()
    answer = query_result[0][0]
    conn.close()
    return answer


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a 
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from standings;")
    query_result = cur.fetchall()
    conn.close()
    return query_result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO matches (player_one_id, player_two_id, match_winner) " +
        "VALUES (%s, %s, %s);",
        (winner,
         loser,
         winner,
         ))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player 
    adjacent to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    cur = conn.cursor()
    query_result = cur.execute("select count(*) from players;")
    num_players = cur.fetchall()
    num_players = num_players[0][0]
    num_matches = num_players / 2
    current_match = 1
    offset_value = 0
    matches_list = []
    while current_match <= num_matches:
        query_result = cur.execute(
            "select player_id, name from standings limit 2 offset (%s);", 
            (offset_value,))
        temp_result_two_tuples = cur.fetchall()
        temp_result_one_tuple = temp_result_two_tuples[
            0] + temp_result_two_tuples[1]
        matches_list.append(temp_result_one_tuple)
        current_match += 1
        offset_value += 2
    conn.close()

    return matches_list
