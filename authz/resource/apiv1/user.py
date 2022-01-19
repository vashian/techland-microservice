from flask_restful import Resource
from authz.controller.apiv1 import UserController

class UserResource(Resource):

  def get(self, user_id=None):
    """
    GET /users --> Get list of users.
    GET /users/<user_id> --> Get user.
    """
    if user_id is None:
      return UserController.get_users() # Get list of users
    else:
      return UserController.get_user(user_id) # Get a user

  def post(self):
    """
    POST /users --> Create new user.
    POST /users/<user_id> --> Not allowed.
    """
    return UserController.create_user() # create new user

  def patch(self, user_id):
    """
    PATCH /users --> Not allowed.
    PATCH /users/<user_id> --> Update user.
    """
    return UserController.update_user(user_id) # Update user

  def delete(self, user_id):
    """
    DELETE /users --> Not allowed.
    DELETE /users/<user_id> --> Delete user.
    """
    return UserController.update_user(user_id)