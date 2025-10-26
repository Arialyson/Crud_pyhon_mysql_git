import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='satander'
)

cursor = conexao.cursor()

#CREATE
#READ
#UPDATE
#DELETE

cursor.close()
conexao.close()