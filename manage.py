from flask import Flask
from flask_migrate import Migrate
from app import app, db  # assuming you have 'app' and 'db' in your 'app' package
from app import create_app

app = create_app()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
