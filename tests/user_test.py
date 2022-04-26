import logging

from app import db
from app.db.models import User, Song
from faker import Faker


def test_user_song_table(application):

    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0

def test_adding_user(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1

def test_query_user(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        user1 = User.query.filter_by(email='aaa111@google.com').first()
        assert user1.email == 'aaa111@google.com'

def test_add_song(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        user1 = User.query.filter_by(email='aaa111@google.com').first()
        user1.songs = [Song("test1","smap","1999","elc"),Song("test2","qwer","2000","dele")]
        db.session.commit()
        assert db.session.query(Song).count() == 2
