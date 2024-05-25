# Importando o Tkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

# Importando comandos
from comandos import *

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

janela_vendas = Tk()
janela_vendas.title("")
janela_vendas.geometry('1043x453')
janela_vendas.configure(background=co9)
janela_vendas.resizable(width=FALSE, height=FALSE)

################# Dividindo a Janela ###############

frame_titulo_v = Frame(janela_vendas, width=310, height=50, bg=co2, relief='flat')
frame_titulo_v.grid(row=0, column=0)

frame_formulario_v = Frame(janela_vendas, width=310, height=403, bg=co1, relief='flat')
frame_formulario_v.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_preview_v = Frame(janela_vendas, width=588, height=403, bg=co1, relief='flat')
frame_preview_v.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################# Label titulo ###############

label_titulo_v = Label(frame_titulo_v, text='Conta a receber',anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
label_titulo_v.place(x=10, y=20)

# Definição da variável global tree_v
global tree_v 

# Função inserir
def inserir_v():    
    cod_cliente = e_cod_cliente.get()
    data = e_data.get()
    valor = e_valor.get()

    lista_v = [cod_cliente, data, valor]
    
    if (cod_cliente=='') or (data=='') or (valor==''):
        messagebox.showerror('Todos os campos são obrigatórios.')
    else:
        inserir_info(lista_v)
        messagebox.showinfo('Registro inserido com suceso.')
        
        e_cod_cliente.delete(0,'end')
        e_data.delete(0, 'end')
        e_valor.delete(0, 'end')
        
    for widget in frame_preview_v.winfo_children():
        widget.destroy()
        
    mostrar_v()
    
# Função Excluir
def deletar_v():
    try:
        treev_dados_v = tree_v.focus()
        treev_dicionario_v = tree_v.item(treev_dados_v)
        tree_lista_v = treev_dicionario_v['values']
        
        valor_id_v = [tree_lista_v[0]]
        
        excluir_info(valor_id_v)
        messagebox.showinfo('Registro excluído com suceso.')
        
        for widget in frame_preview_v.winfo_children():
                widget.destroy()
            
        mostrar_v()
        
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um registro na tabela')
        

################# Configurando frame formulario ###############

#cod_cliente
l_cod_cliente = Label(frame_formulario_v, text='Código do Cliente *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cod_cliente.place(x=10, y=10)
e_cod_cliente = Entry(frame_formulario_v, width=45, justify='left', relief='solid')
e_cod_cliente.place(x=15, y=40)

#Data
l_data = Label(frame_formulario_v, text='Data *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_data.place(x=10, y=70)
e_data = Entry(frame_formulario_v, width=45, justify='left', relief='solid')
e_data.place(x=15, y=100)

#Valor
l_valor = Label(frame_formulario_v, text='Valor *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_valor.place(x=10, y=130)
e_valor = Entry(frame_formulario_v, width=45, justify='left', relief='solid')
e_valor.place(x=15, y=160)

#Botão Inserir
b_inserir_v = Button(frame_formulario_v, command=inserir_v, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir_v.place(x=15, y=340)

#Botão Consultar
#b_atualizar = Button(frame_formulario, command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
#b_atualizar.place(x=110, y=340)

#Botão Excluir
b_excluir_v = Button(frame_formulario_v, command=deletar_v, text='Excluir', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_excluir_v.place(x=205, y=340)


################# Configurando frame preview ###############

def mostrar_v():
        
    global tree_v
    
    lista_v = mostrar_infO()

    #Cabeçário da lista
    t_head = ['ID', 'Código', 'Data', 'Valor']

    #Criando a tabela
    tree_v = ttk.Treeview(frame_preview_v, selectmode="extended", columns=t_head, show="headings")

    #Criando a barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_preview_v, orient="vertical", command=tree_v.yview)

    #Criando a barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_preview_v, orient="horizontal", command=tree_v.xview)

    #Configerando a tabela
    tree_v.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_v.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_preview_v.grid_rowconfigure(0, weight=12)

    hd=['nw', 'nw', 'nw', 'nw']
    h=[175, 175, 180, 180]
    n=0

    for col in t_head:
        tree_v.heading(col, text=col.title(), anchor=CENTER)
        tree_v.column(col, width=h[n], anchor=hd[n])
        
        n+=1

    for item in lista_v:
        tree_v.insert('', 'end', values=item)    
        
# Chamando a função mostrar
mostrar_v() 


