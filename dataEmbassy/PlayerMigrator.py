from nba_api.stats.static import players
from app import db

def basePlayers():
    player_dict = players.get_players()

    nbaCollection = db.get_collection("Players")

    for player in player_dict:
        player1 = db.get_document(nbaCollection, player['full_name'].replace(" ",""))
        player1["value"] = player
        player1.save()