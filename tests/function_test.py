import logging

from app import db
from app.db.models import User, Song
from faker import Faker

def test_register(client):
    """This makes the index page"""
    data = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
        'confirm': 'zzz123'
    }
    response = client.post("/register", data = data)
    user = User.query.filter_by(email='aaa111@test.com').first()
    assert user.email == 'aaa111@test.com'