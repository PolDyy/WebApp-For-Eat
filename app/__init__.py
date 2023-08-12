from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session

import config


app = Flask(__name__)
app.config.from_object(config.DevelopementConfig)
socketio = SocketIO(app, manage_session=False)
Session(app)

from . import views
