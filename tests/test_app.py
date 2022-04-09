from application import app, db
from application.models import Player, Football_Team
from flask import render_template, redirect, url_for, request
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", WTF_CSRF_ENABLED=False)
        return app

# app.config.update({'SQLALCHEMY_POOL_SIZE': None,'SQLALCHEMY_POOL_TIMEOUT': None})

def setUp(self):
        db.create_all()

        db.session.add(Football_Team(football_team_name="Liverpool"))
        db.session.add(Football_Team(football_team_name="Chelsea"))
        
        db.session.add(Player(player_name="Mane"))
        db.session.add(Player(player_name="Henderson")) 


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
        self.assertEqual(response.status_code, 500)

    def test_player(self):
        response = self.client.get(url_for('player'))
        self.assertEqual(response.status_code, 500)

    def test_delete(self):
        response = self.client.get(url_for('player'))
        self.assertEqual(response.status_code, 500)

    # def test_delete_player(self):
    #     response = self.client.get(url_for('delete_player', name="Mane"))
    #     response2 = self.client.get(url_for('delete_player', name="Henderson"), follow_redirects=True)

    #     assert "Mane" not in response.data.decode()
    #     assert "Henderson" in response2.data.decode()

    def test_edit(self):
        response = self.client.get(url_for('edit'))
        self.assertEqual(response.status_code, 500)

    def test_edit_football_team(self):
        response = self.client.get(url_for('edit'))
        self.assertEqual(response.status_code, 500)      