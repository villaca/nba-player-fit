from nba_api.stats.static import teams
from app import db

def baseTeams():
    team_dict = teams.get_teams()

    nbaCollection = db.get_collection("Teams")

    for team in team_dict:
        team1 = db.get_document(nbaCollection, team['nickname'].replace(" ",""))
        team1["value"] = team
        team1.save()