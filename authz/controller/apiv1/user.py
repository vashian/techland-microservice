from authz.util import jsonify
from authz.schema.apiv1 import UserSchema
from authz.model import User

class UserController:

  def get_users():
    print('hi')
    users = User.query.all()
    users_schema = UserSchema(many=True)
    return {
      "users": users_schema.dump(users)
    }
    # return jsonify(status=501, code=107, state={"name": "ali"}, headers={"x":"y"}) # Not impleamented

  def get_user(user_id):
    return jsonify(status=501, code=107) # Not impleamented


  def create_user():
    return jsonify(status=501, code=107) # Not impleamented


  def update_user(user_id):
    return jsonify(status=501, code=107) # Not impleamented


  def delete_user(user_id):
    return jsonify(status=501, code=107) # Not impleamented
