from nba_py import player
from flask import Flask, jsonify
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    player_dict = players.get_players()
    print(player_dict)
    zach = players.find_players_by_full_name("zach lavine")
    print(zach)
    print(zach[0])
    print(zach[0].get("id"))
    #dump = playercareerstats.PlayerCareerStats(per_mode36 = "Per36", player_id = zach[0].get("id"))
    dump = playercareerstats.PlayerCareerStats(zach[0].get("id"))
    #print(player.get_player("Zach", last_name="lavine"))
    #dump = player.PlayerPerformanceSplits(player.get_player("Zach", last_name="lavine"))
    return jsonify(hello='world')


if __name__ == '__main__':
    app.run()
