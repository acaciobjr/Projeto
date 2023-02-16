import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="db",
        user="postgres",
        password="postgres"
    )

    print("Conexão estabelecida com sucesso!")

except psycopg2.Error as error:
    print("Erro ao conectar:", error)

#finally:
  #  if conn:
   #     conn.close()
    #    print("Conexão fechada.")
