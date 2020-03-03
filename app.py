from nba_py import player
from flask import Flask, jsonify, Response
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonteamroster
from utils.mapper import transform_responses
from db import ArangoDB

db = ArangoDB()
app = Flask(__name__)
db.init_app(app)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    #player_dict = players.get_players()
    #print(player_dict)
    #zach = players.find_players_by_full_name("zach lavine")
    #print(zach)
    #print(zach[0])
    #print(zach[0].get("id"))
    #dump = playercareerstats.PlayerCareerStats(per_mode36 = "Per36", player_id = zach[0].get("id"))
    #dump = playercareerstats.PlayerCareerStats(zach[0].get("id"))
    #team_dict = teams.get_teams()
    #bulls = commonteamroster.CommonTeamRoster(1610612762)
    #dict = transform_responses(bulls.common_team_roster.data)

    #for player in dict:
        #payload = playercareerstats.PlayerCareerStats(player.get("PLAYER_ID"))
        #player["career_stats_season_totals_regular_season"] = transform_responses(payload.season_totals_regular_season.data)

    #schema = db.get_db()
    #nbaCollection =  db.get_collection("Test") #schema.createCollection(name="Test")
    #team1 = nbaCollection.createDocument()
    #team1._key = "UtahJazz"
    #team1["roster"] = dict
    #team1.save()

    return jsonify()

@app.route('/embassy/baseteams')
def importBaseTeams():
    from dataEmbassy.TeamMigrator import baseTeams
    baseTeams()
    return Response(status=200)

@app.route('/embassy/baseplayers')
def importBasePlayers():
    from dataEmbassy.PlayerMigrator import basePlayers
    basePlayers()
    return Response(status=200)


if __name__ == '__main__':
    app.run()
