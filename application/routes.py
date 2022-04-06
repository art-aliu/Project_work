# @app.route('/add')
# def add():
#     new_player = Players(name="New Player")
#     db.session.add(new_player)
#     db.session.commit()
#     return "Added new player to database"

# @app.route('/read')
# def read():
#     all_players = players.query.all()
#     players_string = ""
#     for player in all_players:
#         players_string += "<br>"+ player.name
#     return players_string

# @app.route('/update/<name>')
# def update(name):
#     first_player = player.query.first()
#     first_player.name = name
#     db.session.commit()
#     return first_player.name


from application import app, db
from application.models import Players, Football_Teams, PlayersForm, Football_TeamsForm
from flask import render_template, redirect, url_for, request


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayersForm()
    if form.validate_on_submit():
        new_player = Players(name=form.name.data)
        db.session.add(new_player)
        db.session.commit()
        return render_template('index.html', message="Player Added")
    else:
        return render_template('add_player.html', form=form)

@app.route('/players')
def players():
    players = Players.query.all()
    return render_template('player.html', players=players)

@app.route('/add_football_team', methods=['GET', 'POST'])
def add_football_team():
    form = Football_TeamsForm()
    if form.validate_on_submit():
        new_football_team = Football_Teams(name=form.name.data, model=form.model.data)
        db.session.add(new_football_team)
        db.session.commit()
        return render_template('index.html', message="Football Team Added!")
    else:
        return render_template('add_football_team.html', form=form)

@app.route('/football_teams')
def football_team():
    football_teams = football_team.query.all()
    return render_template('football_teams.html', football_teams=football_teams)

@app.route('/players')
def read():
    all_players = players.query.all()
    players_string = ""
    for player in all_players:
        players_string += "<br>"+ player.name
    return players_string

@app.route('/update_player/<name1>', methods=['GET', 'POST'])
def update_player(name1):
    form = PlayersForm()
    player = Players(name=name1)

    return render_template('update_player.html', player=player, form=form)

@app.route('/update_player2/<p2>', methods=['GET', 'POST'])
def update_player2(p2):
    updated_player = db.session.query(Players).filter_by(name=p2).first()
    updated_player.name = request.form.get('name')
    updated_player.player_age = request.form.get('player_age')
    db.session.commit()
    return redirect('/players')

@app.route('/update_player3/<p3>', methods=['GET', 'POST'])
def update_player3(p3):
    updated_player = db.session.query(Players).filter_by(name=p3).first()
    updated_player.name = request.form.get('name')
    updated_player.player_age = request.form.get('player_age')
    updated_player.player_number = request.form.get('player_number')
    db.session.commit()
    return redirect('/players')


@app.route('/update_football_team/<name>/<manager>', methods=['GET', 'POST'])
def update_football_team(name, manager):
    form = Football_TeamsForm()
    Football_Team = Football_Team(name=name, manager=manager)

    return render_template('update_football_team.html', football_team=football_team, form=form)


@app.route('/delete_player/<name>')
def delete_player(name):
    deleted_player = db.session.query(players).filter_by(name=name).first()
    if deleted_player:
        db.session.delete(deleted_player)
        db.session.commit()
        return redirect('/players')
    else:
        return redirect('/players')

@app.route('/delete_football_team/<name>/<manager>')
def delete_football_team(name, manager):
    deleted_football_team = db.session.query(football_team).filter_by(name=name, manager=manager).first()
    if deleted_football_team:
        db.session.delete(deleted_football_team)
        db.session.commit()
        return redirect('/football_teams')
    else:
        return redirect('/football_teams')

