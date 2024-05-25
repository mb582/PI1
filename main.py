# Importando o Tkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

# Importando comandos
from comandos import *
from vendas import *

################# Cores ###############

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# Criando a Janela ###############

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

################# Dividindo a Janela ###############

frame_titulo = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_titulo.grid(row=0, column=0)

frame_formulario = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_formulario.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_preview = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_preview.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################# Label titulo ###############

label_titulo = Label(frame_titulo, text='Cadastro de Clientes',anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
label_titulo.place(x=10, y=20)

# Definição da variável global tree
global tree 

# Função inserir
def inserir():    
    nome = e_nome.get()
    contato = e_contato.get()

    lista = [nome, contato]
    
    if nome=='':
        messagebox.showerror('O campo nome é obrigatório.')
    else:
        inserir_info(lista)
        messagebox.showinfo('Registro inserido com suceso.')
        
        e_nome.delete(0,'end')
        e_contato.delete(0, 'end')
        
    for widget in frame_preview.winfo_children():
        widget.destroy()
        
    mostrar()
    
# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = tree_lista[0]
        
        e_nome.delete(0,'end')
        e_contato.delete(0, 'end')
        
        e_nome.insert(0,tree_lista[1])
        e_contato.insert(0, tree_lista[2])
        
        # Função inserir utilizada para atualizar
        def atualiz():
    
            nome = e_nome.get()
            contato = e_contato.get()

            lista = [nome, contato, valor_id]
            
            if nome=='':
                messagebox.showerror('O campo nome é obrigatório.')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Registro atualizado com suceso.')
                
                e_nome.delete(0,'end')
                e_contato.delete(0, 'end')
                
            for widget in frame_preview.winfo_children():
                widget.destroy()
            
            mostrar()
                
        #Botão Confirmar
        b_confirmar = Button(frame_formulario, command=atualiz, text='Confirmar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)
            
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um registro na tabela')
        
# Função Excluir
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = [tree_lista[0]]
        
        excluir_info(valor_id)
        messagebox.showinfo('Registro excluído com suceso.')
        
        for widget in frame_preview.winfo_children():
                widget.destroy()
            
        mostrar()
        
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um registro na tabela')

# Função Abrir janela parcela
def cadastrar_parcela():    
    mostrar()
    
    janela_vendas.mainloop()
    
  
        
               
################# Configurando frame formulario ###############

#Nome
l_nome = Label(frame_formulario, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_formulario, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

#Contato
l_contato = Label(frame_formulario, text='Contato *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_contato.place(x=10, y=70)
e_contato = Entry(frame_formulario, width=45, justify='left', relief='solid')
e_contato.place(x=15, y=100)

#Botão Inserir
b_inserir = Button(frame_formulario, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

#Botão Atualizar
b_atualizar = Button(frame_formulario, command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)

#Botão Excluir
b_excluir = Button(frame_formulario, command=deletar, text='Excluir', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_excluir.place(x=205, y=340)

#Botão Cadastrar parcela
b_parcela = Button(frame_formulario, command=cadastrar_parcela, text='Cadastrar parcela', width=20, font=('Ivy 9 bold'), bg=co1, fg=co6, relief='raised', overrelief='ridge')
b_parcela.place(x=15, y=300)

################# Configurando frame preview ###############

def mostrar():
    
    global tree
    
    lista = mostrar_infO()

    #Cabeçário da lista
    t_head = ['ID', 'Nome', 'Contato']

    #Criando a tabela
    tree = ttk.Treeview(frame_preview, selectmode="extended", columns=t_head, show="headings")

    #Criando a barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_preview, orient="vertical", command=tree.yview)

    #Criando a barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_preview, orient="horizontal", command=tree.xview)

    #Configerando a tabela
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_preview.grid_rowconfigure(0, weight=12)

    hd=['nw', 'nw', 'nw']
    h=[50, 380, 280]
    n=0

    for col in t_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)    
    

# Chamando a função mostrar
mostrar() 

janela.mainloop()