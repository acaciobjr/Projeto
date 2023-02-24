from flask import Flask, request, jsonify
import psycopg2
from service import UserService

#class UserController:
 #   def get_all_users():
  #      users = UserService.get_all_users()
   #     return jsonify(users)
app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="db",
    user="postgres",
    password="postgres"
)

#@app.route("/recursos", methods=["GET"])
#def get_recursos():
 #   cur = conn.cursor()
  #  cur.execute("SELECT * FROM recursos")
   # recursos = cur.fetchall()
    #return jsonify([{ "id": r[0], "nome": r[1] } for r in recursos])

@app.route("/recursos", methods=["POST"])
def create_user(name, age, email, password):   
    return jsonify({"name": name, "age": age, "email": email, "password": password})


@app.route("/recursos/<int:id>", methods=["GET"])
def read_user(users):    
    if row in recurso:
        return jsonify("Name: %s, Age: %s, Email: %s" % (row[0], row[1], row[2]))
    elif recurso is None:
        return "Recurso não encontrado", 404


@app.route("/recursos/<int:id>", methods=["PUT"])
def update_user(name, age, email, password):    
    return jsonify({ "new name": name, "new age": age, "new email": email, "new password": password })

@app.route("/recursos/<int:id>", methods=["DELETE"])
def delete_user(users):
    return "deleted feature", 200

if __name__ == '__main__':
    app.run(debug=True)
