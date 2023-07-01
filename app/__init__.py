from flask import Flask
from flask_socketio import SocketIO
import config
# создание экземпляра приложения

app = Flask(__name__)
app.config.from_object(config.DevelopementConfig)
socketio = SocketIO(app)

# инициализирует расширения
# db = SQLAlchemy(app)
# mail = Mail(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

from . import views
