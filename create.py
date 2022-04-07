from application import db
from application.models import Football_Team, Player
from application import models

db.drop_all()
db.create_all()

# football_team1 = Football_Teams(name = "Liverpool", manager = "Jurgen Klopp")
# db.session.add(football_team1)
# db.session.commit()
# player1 = Players(name = "Jordan Henderson", player_number = "14", player_age = "31")
# db.session.add(player1)
# db.session.commit()
