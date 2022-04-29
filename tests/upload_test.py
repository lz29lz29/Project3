import logging
import os

from app import db
from app.db.models import User, Song
from faker import Faker

def test_query_user(application, client):

    with application.app_context():
        data = {
            'email': 'aaa111@test.com',
            'password': 'zzz123',
            'confirm': 'zzz123'
        }
        client.post("/register", data=data)

        data1 ={
            'email': 'aaa111@test.com',
            'password': 'zzz123'

        }

        client.post("/login",data = data1)
        root = os.path.dirname(os.path.abspath(__file__))
        testdir = os.path.join(root, '../tests')
        assert os.path.exists(testdir) == True

        test_file = os.path.join(testdir, 'music.csv')
        assert os.path.exists(test_file) == True
        upload_dir = os.path.join(root, '../app/uploads')
        assert os.path.exists(upload_dir)

        data2 ={
            'file' : open(test_file,'rb')
        }
        client.post('/songs/upload', data = data2)
        upload_file = os.path.join(upload_dir,'home_myuser_tests_.._tests_music.csv')
        assert os.path.exists(upload_file)
        os.remove(upload_file)


