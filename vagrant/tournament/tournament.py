#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

#- when players add to tournament, database should create unique id for each player using serial
#- SQL aggregation when wanting to count or adding up
#- try using loop in database queries
#- if database calls get confusing use views


import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("DELETE FROM matches *")

    DB.commit()
    DB.close();


def deletePlayers():
    """Remove all the player records from the database."""

    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("DELETE FROM players *")
    #c.execute("DELETE FROM matches id")

    DB.commit()
    DB.close();


def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    # fetching results from db and storing in results var
    results = c.fetchall()
    #error processing to see what count players is storing
    print "Count players is returning: {}".format(results)
    for row in results:
        return row[0]

    DB.close();

    return results

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    ## Database connection
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (bleach.clean(name),))
    #c.execute("INSERT INTO matches (player_id) SELECT id FROM players")

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

    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()

    #c.execute("UPDATE matches SET wins = 0, games_played = 0 WHERE wins = null")
    #c.execute("UPDATE matches SET wins = 0, games_played = 0")

    c.execute("SELECT players.id, players.name, \
               COALESCE( matches.wins, '0') as wins, \
               COALESCE( matches.games_played, '0') as games_played \
               FROM players LEFT JOIN matches \
               ON players.id = matches.player_id \
               ORDER BY players.id")

    #c.execute("SELECT players.id, players.name, COALESCE( matches.wins, '0') as wins,COALESCE( matches.games_played, '0') as games_played FROM players LEFT JOIN matches ON players.id = matches.player_id ORDER BY players.id")
    
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


