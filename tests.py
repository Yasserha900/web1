import unittest
from flask_testing import TestCase
from app import app, db

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.client.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Welcome' in response.data)

if __name__ == '__main__':
    unittest.main()
