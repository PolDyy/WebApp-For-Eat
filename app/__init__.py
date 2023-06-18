from flask import Flask
import config
# создание экземпляра приложения

app = Flask(__name__)
app.config.from_object(config.DevelopementConfig)

# инициализирует расширения
# db = SQLAlchemy(app)
# mail = Mail(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

from . import views
