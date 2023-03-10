"""
a valid user creating post
"""

from flask_restful import abort, marshal_with, fields, reqparse
from flask import request
from api import db
from db.model import Post
from middleware.islogin import islogin


#  request bodies
parse = reqparse.RequestParser()
parse.add_argument("title", type=str, help="title is required")
parse.add_argument("body", type=str, help="body is required")


#  json serialization
resource_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "user_id": fields.Integer
}



# get all post from current user
@islogin
@marshal_with(resource_fields)
def getUserPosts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return posts,200



# creating post by current user
@islogin
@marshal_with(resource_fields)
def createPosts(user_id):
    #  request body
    args = parse.parse_args()

    is_title_exist = Post.query.filter_by(title=args['title']).first()
    if is_title_exist:
        abort(404, message="Title is already taken, please try another one")

    post = Post(title=args['title'], body=args['body'], user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return post,201



# update post by current user
@islogin
@marshal_with(resource_fields)
def updatePost(user_id):
    
    #  getting from parse for getting data of query parameter
    args = parse.parse_args()

    title_name = request.args.get('title_name')

    # checking if post is present or not
    post = Post.query.filter_by(title=title_name).first()


    # if post is not pres
    if not post:
        abort(404, message="no post")

        #  checking if user_id and post.user_id is same
    if user_id != post.user_id:
        abort(404, message="Invalid user")

    #  query parameters
    post.title = args['title']
    post.body = args['body']
    
    # commiting actions
    db.session.commit()

    return post,200



@islogin
def deletePost(user_id):

    title_name = request.args.get('title_name')


    # checking if post is present
    post = Post.query.filter_by(title=title_name).first()
    
    # if not post
    if not post:
        abort(404, message="Post is not present cant delete")

    if user_id != post.user_id:
        abort(404, message="cant delete invalid user")
    
    # deleting from db
    db.session.delete(post)
    db.session.commit()

    return {"message":"deleted successfully"},200