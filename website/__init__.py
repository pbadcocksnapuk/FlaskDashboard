from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL

# url = URL.create(
#     drivername="postgresql",
#     username="pbadcock",
#     host="snap-phoenix-analytics.csp7okigym8g.eu-west-2.rds.amazonaws.com",
#     database="snap_analytics"
# )
#
# engine = create_engine(url)

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfghjko iuytrexcv bnm' # secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
