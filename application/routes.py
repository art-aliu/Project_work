from application import app, db
from application.models import Players

@app.route('/add')
def add():
    new_player = Players(name="New Player")
    db.session.add(new_game)
    db.session.commit()
    return "Added new player to database"

@app.route('/read')
def read():
    all_players = players.query.all()
    players_string = ""
    for player in all_players:
        players_string += "<br>"+ player.name
    return players_string

@app.route('/update/<name>')
def update(name):
    first_player = player.query.first()
    first_player.name = name
    db.session.commit()
    return first_player.name