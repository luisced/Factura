from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask import Flask
from facturacion.config import Config
from flask_cors import CORS
from flask_session import Session

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
mail = Mail()


@login_manager.user_loader
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config.from_object(Config)
    Session(app)
    CORS(app)

    #CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    app.app_context().push()

    from facturacion.user.routes import user
    from facturacion.tools.routes import tools

    app.register_blueprint(user)
    app.register_blueprint(tools)
    app.config.from_object(Config)

    return app
