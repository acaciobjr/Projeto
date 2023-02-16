from flask import jsonify
from service import UserService

class UserController:
    def get_all_users():
        users = UserService.get_all_users()
        return jsonify(users)
