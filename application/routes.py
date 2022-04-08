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
from application.models import Player, Football_Team, AddPlayerForm, AddFootball_TeamForm
from flask import render_template, redirect, url_for, request


app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 600 
app.config['SQLALCHEMY_POOL_RECYCLE'] = 100


# @app.route('/', methods=['GET', 'POST'])
# def index1():
#     return render_template('index.html')
# @app.route('/index,', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html',)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_football_team', methods=['GET', 'POST'])
def add_football_team():
    form = AddFootball_TeamForm()
    if form.validate_on_submit():
        new_football_team = Football_Team(football_team_name =form.football_team_name.data)
        db.session.add(new_football_team)
        db.session.commit()
        return render_template('index.html', message="Football Team Added")
    else:
        return render_template('add_football_team.html', form=form)

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = AddPlayerForm()
    form.football_team_name.choices = [(football_team.id, football_team.football_team_name) for football_team in Football_Team.query.order_by(Football_Team.football_team_name).all()]    
    if form.validate_on_submit():
        new_player_name = Player(player_name=form.player_name.data, player_number=form.player_number.data, player_age=form.player_age.data, football_team_id = form.football_team_name.data)  
        db.session.add(new_player_name)
        db.session.commit()
        return render_template('index.html', message="Player Added")
    else:
        return render_template('add_player.html', form=form)

@app.route('/player_list')
def player():
    all_player = Player.query.all()

    return render_template('player_list.html', all_player=all_player)

# route created to delete players from database

@app.route('/delete_player/<name>')
def delete_player(name):
    deleted_player = db.session.query(player).filter_by(name=name).first()
    if deleted_player:
        db.session.delete(deleted_player)
        db.session.commit()
        return redirect('/players')
    else:
        return redirect('/players')

@app.route('/delete/<player_name>', methods = ['GET', 'DELETE'])
def delete(player_name):
    delete_player = Player.query.filter_by(player_name=player_name).first()
    db.session.delete(delete_player)
    db.session.commit()
    return redirect(url_for('player names'))

@app.route('/edit_football_teams')
def edit():
    all_football_teams = Football_Team.query.all()

    return render_template('edit_football_teams.html', all_football_teams=all_football_teams)

@app.route('/edit_one_football_team/<football_team_name>', methods = ['GET', 'POST'])
def edit_football_team(football_team_name):
    form = AddFootball_TeamForm()
    edit_one_football_team = Football_Team.query.filter_by(football_team_name=football_team_name).first()
    if request.method == 'POST':
        if edit_one_football_team:
            edit_one_football_team.football_team_name = form.football_team_name.data
            db.session.commit()
            return redirect(url_for('edit', message ="Football Team Name Updated!"))
    else:
        return render_template('edit_one_football_team.html', edit_one_football_team=edit_one_football_team, form=form)

# @app.route('/players')
# def read():
#     all_players = players.query.all()
#     players_string = ""
#     for players in all_players:
#         players_string += "<br>"+ players.name
#     return players_string

# @app.route('/update_player/<name1>', methods=['GET', 'POST'])
# def update_player(name1):
#     form = AddPlayerForm()
#     player = Player(name=name1)

#     return render_template('update_player.html', player=player, form=form)

# @app.route('/update_player2/<name2>', methods=['GET', 'POST'])
# def update_player2(name2):
#     updated_player = db.session.query(Player).filter_by(name=name2).first()
#     updated_player.name = request.form.get('name')
#     updated_player.player_age = request.form.get('player_age')
#     db.session.commit()
#     return redirect('/players')

# @app.route('/update_player3/<name3>', methods=['GET', 'POST'])
# def update_player3(name3):
#     updated_player = db.session.query(Player).filter_by(name=name3).first()
#     updated_player.name = request.form.get('name')
#     updated_player.player_age = request.form.get('player_age')
#     updated_player.player_number = request.form.get('player_number')
#     db.session.commit()
#     return redirect('/players')


# @app.route('/update_football_team/<name>/<manager>', methods=['GET', 'POST'])
# def update_football_team(name,):
#     form = Football_TeamForm()
#     Football_Team = Football_Team(name=name)

#     return render_template('update_football_team.html', football_team=football_team, form=form)




