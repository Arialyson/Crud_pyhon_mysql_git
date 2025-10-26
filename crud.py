import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='satander'
)

cursor = conexao.cursor()

#CREATE

#nome_var = "Kratos"
#nasc_var = "1988-12-03"
#na_var = "Grécia"
#comando = f'INSERT INTO personas (id, nome, nascimento, nacionalidade) VALUES ("","{nome_var}","{nasc_var}","");'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

# resultado = cursor.fetchall() # ler o banco de dados

#READ

#comando = 'SELECT * FROM  personas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#UPDATE

#nome_vari = "Kratos"
#na_vari = "Suiça"
#comando = f'UPDATE personas SET nacionalidade = "{na_vari}" WHERE nome = "{nome_vari}"'
#cursor.execute(comando)
#conexao.commit()

#DELETE

nome_vari = "Maria"
comando = f'DELETE FROM personas WHERE nome = "{nome_vari}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()