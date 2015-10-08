#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

#- when players add to tournament, database should create unique id for each player using serial
#- SQL aggregation when wanting to count or adding up
#- try using loop in database queries
#- if database calls get confusing use views


import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches *")

    DB.commit()
    DB.close();


def deletePlayers():
    """Remove all the player records from the database."""

    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players *")

    DB.commit()
    DB.close();


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    
    # fetching results from db and storing in results var
    results = c.fetchone()

    print "Count players is returning: {}".format(results)

    DB.close()
    return results[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    ## Database connection
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))

    DB.commit()
    DB.close();


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB = connect()
    c = DB.cursor()

    c.execute("SELECT * FROM players ORDER BY wins DESC")
    
    results = c.fetchall()
    #print "PlayerStandings is returning: {}".format(results)
    DB.close();
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    ## Database connection
    DB = connect()
    c = DB.cursor()

    c.execute("UPDATE players \
               SET games_played = games_played + 1, \
                   wins = wins + 1 \
               WHERE players.id = (%s)", (winner,))

    c.execute("UPDATE players \
               SET games_played = games_played + 1 \
               WHERE players.id = (%s)", (loser,))

    c.execute("INSERT INTO matches (winning_id, losing_id) \
               VALUES (%s, %s)", (winner, loser,))
    
    DB.commit()
    DB.close();
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()

    standings = playerStandings()
    results = []

    for p1, p2 in zip(standings[0::2], standings[1::2]):
        results.append((p1[0], p1[1], p2[0], p2[1]))

    return results



