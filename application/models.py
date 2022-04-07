
from application import db
from application import app
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class Football_Team(db.Model):
    __tablename__ = 'football_team'
    id = db.Column(db.Integer, primary_key=True)
    football_team_name = db.Column(db.String(45), nullable=False)
    player = db.relationship('Player', backref='football_teamsbr')

class Football_TeamForm(FlaskForm):
    football_team_name = StringField('Enter the football team name')
    submit = SubmitField ('Submit')

class Player(db.Model):    
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(45), nullable=False)
    player_number = db.Column(db.Integer, nullable=False)
    player_age = db.Column(db.Integer, nullable=False)
    football_team_id = db.Column(db.Integer, db.ForeignKey('football_team.id'), nullable=False)

class PlayerForm(FlaskForm):
    player_name = StringField ('Enter player name')
    player_number = IntegerField ('Enter the player number')
    player_age = IntegerField ('Enter the player age')
    football_team_name = SelectField ('Football Club', choices = [])
    submit = SubmitField ('Submit')



