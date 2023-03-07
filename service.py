class UserService:
    def get_all_users(self):
        cur = conn.cursor()
        cur.execute("SELECT id, name, age, email FROM TbProjetoFaint")
        result = cur.fetchall()
        return [{"id": row[0], "name": row[1], "age": row[2], "email": row[3]} for row in result]

    def create_user(self, name, age, email, password):
        cur = conn.cursor()
        cur.execute("INSERT INTO TbProjetoFaint (name, age, email, password) VALUES (%s, %s, %s, %s) RETURNING id;", (name, age, email, password))
        conn.commit()
        id = cur.fetchone()[0]
        return id

    def read_user(self, name):
        cur = conn.cursor()
        cur.execute("SELECT name, age, email FROM TbProjetoFaint WHERE name = %s", (name))
        result = cur.fetchone()
        if result:
            return {"name": result[0], "age": result[1], "email": result[2]}
        else:
            return None

    def update_user(self, name, age, email, password):
        cur = conn.cursor()
        cur.execute("UPDATE TbProjetoFaint SET age = %s, email = %s, password = %s WHERE name = %s", (age, email, password, name))
        conn.commit()

    def delete_user(self, name):
        cur = conn.cursor()
        cur.execute("DELETE FROM TbProjetoFaint WHERE name = %s", (name,))
        conn.commit()
