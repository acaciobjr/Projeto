class UserService:
    def get_all_users():
        return [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Doe"},
        ]

#import sys
users = []

def create_user(name, age, email, password):  
  dados = request.get_json()
    name = dados["name"]
    age = dados["age"]
    email = dados["email"]
    password = dados["password"]
    cur = conn.cursor()
    cur.execute("INSERT INTO TbProjetoFaint (name, age, email, password) VALUES (%s, %s, %s, %s);", (name,age,email,password))
    conn.commit()
    id = cur.lastrowid
  #user = {"name": name, "age": age, "email": email, "password": password}
  #users.append(user)
  #return f"The {name} was created with this age {age} and this email {email}.\n"

def read_user(users):
    cur = conn.cursor()
    cur.execute("SELECT name, age, email FROM TbProjetoFaint WHERE name = %s", (name))
    recurso = cur.fetchone()  
  readUser = input('whats the username?')
  for user in users:
    if user['name'] == readUser:
      #print("user found:", name)
      return f"user found: name: {user['name']}, age: {user['age']}, email: {user['email']}"
    else:
        return "name not found."

def update_user(name, age, email):
  dados = request.get_json()
    name = dados["name"]
    age = dados["age"]
    email = dados["email"]
    cur = conn.cursor()
    cur.execute("UPDATE TbProjetoFaint SET name = '', age = nova idade, email = 'novo email', password = 'nova senha' WHERE name = 'nome antigo'%s" % (name))
    conn.commit()  
  #wUser = input("what is the email of the user you want to change the data?")
  #for user in users:
    #print(user[email])
    #if user['email'] == wUser:
      #newName = input("digite um novo nome:")
      #newAge = input("digite uma nova idade:")
      #newEmail = input("digite um novo email:")
      #if newName:
        #user["name"] = newName
      #if newAge:
        #user["age"] = newAge
      #if newEmail:
        #user["email"] = newEmail
      #return True
  #return False

def delete_user(users):
  cur = conn.cursor()
    cur.execute("DELETE name, age, email, password FROM TbProjetoFaint WHERE name = %s", (name))
    conn.commit()
  #delUser = input("what is the name of the user you want to delete?")
  #for user in users:
    #print(user[email])
    #if user['name'] == delUser:
      #user = users.remove(user)
      #users.remove(user)
      #return f"User {delUser} has been deleted successfully."
    #else:
  #return "User not found."
 
#def exit(users):
    #Option = input("Are you sure you'd like to leave? Y/N:")
    #for user in users:
        #if Option == "Y":
            #print('good bye')
            #sys.exit()
        #elif Option == "N":
            #print('returning to the menu..')
            #return main()
        #else:
            #return exit(users)
                   
                   
#def main():
  #while True:
    #print("Options:")
    #print("1. create user")
    #print("2. read user")
    #print("3. update user")
    #print("4. remove user")
    #print("5. exit")
    #option = int(input("Enter the desired option!\n"))

    #if option == 1:
      #name = input('enter the username:')
      #age = input('enter user age:')
      #email = input('enter user email:')
      #print(create_user(name, age, email))
    #elif option == 2:
      #print(read_user(users))
    #elif option == 3:
      #print(update_user(name, age, email))
    #elif option == 4:
      #print(delete_user(users))
    #elif option == 5:
      #print(exit(users))
      #break
    #else:
      #print('Opção inválida.')

#if __name__ == "__main__":
  #main()
