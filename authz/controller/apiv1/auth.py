from flask import  request
from jwt import encode, decode
from authz.util import jsonify

class AuthController:

  def create_jwt_token():
    return jsonify(status=501, code=107)

  def verify_jwt_token():
    return jsonify(status=501, code=107)
    