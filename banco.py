# importando SQLite
import sqlite3 as lite

# criando conexão
con =  lite.connect('dados.db')

# criando tabela
with con:
    cur = con.cursor()
    #cur.execute("CREATE TABLE cliente(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")   
    #cur.execute("ALTER TABLE cliente ADD COLUMN contato INTEGER")
    