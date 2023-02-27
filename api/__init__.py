from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "sdfhs8dhfuijekfodjiujjj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from routes.home_route import HomeRoute
from routes.register_route import RegisterRoute
from routes.login_route import LoginRoute
from routes.post_route import PostRoute

api.add_resource(HomeRoute,"/")
api.add_resource(RegisterRoute,"/register", "/register/<user_id>")
api.add_resource(LoginRoute,"/login")
api.add_resource(PostRoute,"/post", "/post/<title_name>")