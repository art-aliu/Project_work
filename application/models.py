
from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


class Football_Team(db.Model):
    __tablename__ = 'football_team'
    id = db.Column(db.Integer, primary_key=True)
    football_team_name = db.Column(db.String(45), nullable=False)
    football_team_player = db.relationship('Player', backref='playerbr')

# def __repr__(self):
#         return 'Choose {}'.format(self.football_team_name)

class Player(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(45), nullable=False)
    football_team_id = db.Column(db.Integer, db.ForeignKey('football_team.id'), nullable=False)


class AddFootball_TeamForm(FlaskForm):
    football_team_name = StringField('Football team name', validators=[DataRequired()])
    submit = SubmitField ('Add name')


class AddPlayerForm(FlaskForm):
    player_name = StringField('Player Name', validators=[DataRequired()])
    football_team_name = SelectField (u'Football Team Name', choices = [])
    submit = SubmitField ('Add Player')

