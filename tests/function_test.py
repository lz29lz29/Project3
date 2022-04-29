import logging
import os

from app import db
from app.db.models import User, Song
from faker import Faker
from pathlib import Path

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


def test_login(client):
    """This makes the index page"""
    data = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
        'confirm': 'zzz123'
    }
    client.post("/register", data = data)
    user = User.query.filter_by(email='aaa111@test.com').first()
    assert user.email == 'aaa111@test.com'
    data1 = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
    }

    responce = client.post("/login", data = data1)
    assert responce.status_code == 302


def test_upload(client):
    """This makes the index page"""
    data = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
        'confirm': 'zzz123'
    }
    client.post("/register", data = data)

    data1 = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
    }

    client.post("/login", data = data1)

    root = Path(__file__).parent.parent
    test_file = root/ 'tests' / 'music.csv'
    upload_folder = root/ 'app'/ 'uploads' / 'music.csv'

    if os.path.exists(upload_folder):
        os.remove(upload_folder)

    data2 ={
        'file': test_file.open('rb')
    }

    client.post('/songs/upload', data = data2)

    upload_dir = root/ 'app'/ 'uploads'/ 'home/runner/work/Project3/Project3/tests/music.csv'
    assert os.path.exists(upload_dir)
    os.remove(upload_dir)
