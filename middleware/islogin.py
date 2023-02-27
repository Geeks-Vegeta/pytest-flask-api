"""
In this file we are creating an islogin decoretor 
for finding if the user is valid or not by sending
a jwt token in headerfile of application, each time
when the user is requesting an api where he is dealing
with some sensitive information, each time we are going to
add this decoretor in particular routes function.
"""
from flask_restful import abort  #  functions abort for sending error message
from flask import request  #  for requesting header if jwt is present or not
from functools import wraps  #  wrap for creating decoretor
import jwt  # jwt for creating token
from api import app
from db.model import User  #  importing user model 


#  creating islogin decorator
def islogin(f):
    @wraps(f)
    def wrap(*args, **kwargs): 
        auth_header = request.headers.get('authorization')
        get_bearer = auth_header.split()[0]

        if get_bearer != "Bearer":
            return {"message":"Please add Bearer"}, 400 

        # checking if auth is present in request header/ cookies
        # auth = request.cookies.get('auth')  

        # getting headers auth token
        auth = auth_header.split()[1]

        
        #  if present 
        if auth:
            user = jwt.decode(auth, algorithms=['HS256'], key=app.config['SECRET_KEY'])
            user_id = user['user_id']

        else:
            # if not present
            abort(404, message="you are not login")
        return f(user_id, *args, **kwargs)
    return wrap