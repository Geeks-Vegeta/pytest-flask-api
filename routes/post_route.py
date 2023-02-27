"""
a valid user creating post
"""

from flask_restful import Resource
import controllers.post_controller as pc


class PostRoute(Resource):
    
    # get all post from current user
    def get(self):
        return pc.getUserPosts()



    # creating post by current user
    def post(self):
        return pc.createPosts()

    

    # update post by current user
   
    def put(self):
       return pc.updatePost()

    
    def delete(self):
        return pc.deletePost()