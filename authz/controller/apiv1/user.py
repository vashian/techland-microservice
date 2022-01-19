from authz.util import jsonify

class UserController:

  def get_users():
    return jsonify(status=501, code=107, state={"name": "ali"}, headers={"x":"y"}) # Not impleamented

  def get_user(user_id):
    return jsonify(status=501, code=107) # Not impleamented


  def create_user():
    return jsonify(status=501, code=107) # Not impleamented


  def update_user(user_id):
    return jsonify(status=501, code=107) # Not impleamented


  def delete_user(user_id):
    return jsonify(status=501, code=107) # Not impleamented
