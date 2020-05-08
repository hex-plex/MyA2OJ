from flask import Flask
from config import Config
from flaskwebgui import FlaskUI

app=Flask(__name__)
ui = FlaskUI(app)
app.config.from_object(Config)
from app import routes
