from application import app, db
from application.models import Player, Football_Team, AddFootball_TeamForm, AddPlayerForm
from flask import render_template, redirect, url_for, request
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", WTF_CSRF_ENABLED=False, SQLALCHEMY_POOL_SIZE = None, SQLALCHEMY_POOL_TIMEOUT = None)
        return app

# app.config.update({'SQLALCHEMY_POOL_SIZE': None,'SQLALCHEMY_POOL_TIMEOUT': None})

    def setUp(self):
        db.create_all()
        # test_football_team1 = Football_Team(football_team_name = "Manchester City" )
        # test_player1 = Player(player_name = "Foden" )
        # db.session.add(test_football_team1)
        # db.session.add(test_player1)
        # db.session.commit()


    

        db.session.add(Football_Team(football_team_name="Liverpool"))
        db.session.add(Football_Team(football_team_name="Chelsea"))
        
        db.session.add(Player(player_name="Mane", football_team_id = 1))
        db.session.add(Player(player_name="Henderson", football_team_id = 2)) 



        # test_football_team = Football_Team(football_team_name = "Barcelona")

        # db.session.add(test_football_team)
        # db.session.commit()

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    # def test_player(self):
    #     response = self.client.get(url_for('player'))

    #     assert "Mane" in response.data.decode()
    #     assert "Henderson" in response.data.decode()
    
            



    def test_add_football_team(self):
        response = self.client.get(url_for('add_football_team'))
        self.assertEqual(response.status_code, 200)

    def test_add_player(self):
        response = self.client.get(url_for('add_player'))
        self.assertEqual(response.status_code, 200)

    def test_player(self):
        response = self.client.get(url_for('player'))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.get(url_for('player'))
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        response = self.client.get(url_for('edit'))
        self.assertEqual(response.status_code, 200)

    def test_edit_football_team(self):
        response = self.client.get(url_for('edit'))
        self.assertEqual(response.status_code, 200)  

    
    # def test_add_football_team_non(self):
    #     response = self.client.get(url_for('add_football_team'))

    #     assert "- Add Football_Team" in response.data.decode()

    # def test_add_football_team(self):
    #     response = self.client.post(
    #     url_for('add_football_team'),
    #     data={"football_team_name": "Liverpool",},
    #     follow_redirects=True
    #     )

    #     assert "Football Team Added!" in response.data.decode()

    class TestAdd(TestBase):
        def test_add_football_team(self):
            response = self.client.post(url_for('add_football_team'))
            assert 'Football_Team_added' in response.data.decode()
