import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened database successfully")


df = pd.read_sql_query("""SELECT * FROM sqlite_master WHERE type='table';""", conn)

print(df)

player_match = pd.read_sql_query("SELECT * FROM Player_Match;", conn)
print(player_match.head())

null_player_match = pd.read_sql_query("SELECT * FROM Player_Match WHERE Team_ID IS NULL;", conn)
print(null_player_match)

toss_dec = pd.read_sql("SELECT * FROM Match ;", conn)
print(toss_dec.head())

null_match = pd.read_sql(""" SELECT * FROM Match WHERE MATCH_Winner IS NULL;""", conn)
print(null_match)