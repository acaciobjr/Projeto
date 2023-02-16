from flask import Flask
from controller import UserController

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/users")
def get_all_users():
    return UserController.get_all_users()

@App.route("/users", methods=["POST"])
def create_user():
    return UserController.create_user()

if __name__ == "__main__":
    app.run(debug=True)
