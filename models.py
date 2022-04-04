from application import db

class Football_Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_club = db.Column(db.String(30), nullable=False)
manager = bd.Column(db.String(30), nullable=False)
    players = db.relationship('player', backref='football_teambr')


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_number = db.Column(db.String(7), nullable=False)
    player_age = (db.Column(db.Integer, nullable=False)
    football_team_id = db.Column(db.Integer, db.ForeignKey('football_team.id'), nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

