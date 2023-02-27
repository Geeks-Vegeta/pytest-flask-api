from flask_restful import Resource
import controllers.login_controller as login


# login class
class LoginRoute(Resource):

    def post(self):
        return login.userLogin()

    
    # islogin is an decorator for checking if user is valid
    
    def get(self):
        return login.getCurrentUser()