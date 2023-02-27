from flask_restful import Resource
import controllers.register_controller as register

# register 
class RegisterRoute(Resource):

    # getting all users
    def get(self):
        return register.getAllUsers()

    # creating user
    def post(self):
        return register.createUser()
          
    # delete user      
    def delete(self):
        return register.deleteUser()
    
    # update user
    def put(self):
        #  this is requrest body
        return register.updateUser()