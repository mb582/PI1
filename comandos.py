# importando SQLite
import sqlite3 as lite

#Criando conexão
con = lite.connect('dados.db')


#lista = ['Odete Shum', 123456778]
#Inserir informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cliente (nome, contato) VALUES (?, ?)"
        cur.execute(query, i) 
  
#Acessar informações
def mostrar_infO():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cliente"
        cur.execute(query) 
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista

#Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cliente SET nome=?, contato=? WHERE id=?"
        cur.execute(query, i)    

       
#Excluir informações
def excluir_info(i):
    with con:   
        cur = con.cursor()
        query = "DELETE FROM cliente WHERE id=?"
        cur.execute(query, i)    