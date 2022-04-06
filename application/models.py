

from application import db
from application import app
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class Football_Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_club = db.Column(db.String(30), nullable=False)
    manager = db.Column(db.String(30), nullable=False)
    players = db.relationship('player', backref='football_teambr')

class Football_TeamsForm(FlaskForm):
    name_of_club = StringField('Enter the game title')
    manager = StringField ('Enter the manager name')
    submit = SubmitField ('submit')


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    player_number = db.Column(db.Integer, nullable=False)
    player_age = db.Column(db.Integer, nullable=False)
    football_team_id = db.Column(db.Integer, db.ForeignKey('football_team.id'), nullable=False)

class PlayersForm(FlaskForm):
    name = StringField ('Enter your name')
    player_number = IntegerField ('Enter the players number')
    player_age = IntegerField ('Enter the players age')
    submit = SubmitField ('submit')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

