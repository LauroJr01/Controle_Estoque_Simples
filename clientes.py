from setup_db import Session, Cliente
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from treeviews import criar_treeview_cliente

# Lista de Clientes
def abrir_lista_cliente(janela_principal):
    janela_cliente = Toplevel(janela_principal)
    janela_cliente.title("Lista de Clientes")
    janela_cliente.geometry("600x400")
    janela_cliente.grab_set()

    colunas = criar_treeview_cliente(janela_cliente)
    colunas.pack(expand=True, fill="both", padx=10, pady=10)
    sessao = Session()
    try:
        clientes = sessao.query(Cliente).all()
        for cliente in clientes:
            colunas.insert("", "end", values=(cliente.nome, cliente.endereco, cliente.telefone, cliente.email))
    finally:
        sessao.close()


# Cadastrar Cliente
def abrir_cadastro_cliente(janela_principal):
    janela_cadastrar = Toplevel(janela_principal)
    janela_cadastrar.title("Cadastrar Cliente")
    janela_cadastrar.geometry("500x400")
    janela_cadastrar.grab_set()

    # Nome
    cliente_cadastrar = Label(janela_cadastrar, text="Nome do Cliente")
    cliente_cadastrar.pack(padx=10, pady=10)
    cliente_cadastrar_entrada = Entry(janela_cadastrar)
    cliente_cadastrar_entrada.pack(padx=10, pady=10)

    # Endereço
    cliente_endereco = Label(janela_cadastrar, text="Endereço")
    cliente_endereco.pack(padx=10, pady=10)
    cliente_endereco_entrada = Entry(janela_cadastrar)
    cliente_endereco_entrada.pack(padx=10, pady=10)

    # Telefone
    cliente_telefone = Label(janela_cadastrar, text="Telefone")
    cliente_telefone.pack(padx=10, pady=10)
    cliente_telefone_entrada = Entry(janela_cadastrar)
    cliente_telefone_entrada.pack(padx=10, pady=10)

    # E-mail
    cliente_email = Label(janela_cadastrar, text="E-mail")
    cliente_email.pack(padx=10, pady=10)
    cliente_email_entrada = Entry(janela_cadastrar)
    cliente_email_entrada.pack(padx=10, pady=10)

    # DEF Cadastrar Cliente
    def cadastrar_cliente():
        nome = cliente_cadastrar_entrada.get().strip().title()
        endereco = cliente_endereco_entrada.get().strip()
        telefone = cliente_telefone_entrada.get().strip()
        email = cliente_email_entrada.get().strip().lower()

        if not nome:
            messagebox.showerror("Erro", 'Preencha o campo "nome"')
            return
        if not endereco:
            endereco = "Não informado"
        if not telefone:
            telefone = "Não informado"
        if not email:
            email = "Não informado"

        sessao = Session()
        try:
            cliente_existente = sessao.query(Cliente).filter_by(nome=nome).first()
            if cliente_existente:
                messagebox.showerror("Erro", "Usuário já existe.")
                return
            novo_cliente = Cliente(nome=nome, endereco=endereco, telefone=telefone, email=email)
            sessao.add(novo_cliente)
            sessao.commit()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            janela_cadastrar.destroy() 
        finally:
            sessao.close()

    # Botão Salvar
    botao_salvar_cadastrar = Button(janela_cadastrar, text="Salvar", command=cadastrar_cliente)
    botao_salvar_cadastrar.pack(padx=10, pady=10)


# Editar Cliente
def abrir_editar_cliente(janela_principal):
    janela_editar = Toplevel(janela_principal)
    janela_editar.title("Editar Cliente")
    janela_editar.geometry("500x500")
    janela_editar.grab_set()

    sessao = Session()
    clientes = sessao.query(Cliente).all()
    sessao.close()

    nome_clientes = [cliente.nome for cliente in clientes]

    # Selecionar Cliente
    cliente_selecionar = Label(janela_editar, text="Selecionar Cliente")
    cliente_selecionar.pack(padx=10, pady=10)
    cliente_selecionar_entrada = Combobox(janela_editar, values=nome_clientes)
    cliente_selecionar_entrada.pack(padx=10, pady=10)

    # Nome
    cliente_nome = Label(janela_editar, text="Nome")
    cliente_nome.pack(padx=10, pady=10)
    cliente_nome_entrada = Entry(janela_editar)
    cliente_nome_entrada.pack(padx=10, pady=10)

    # Endereço
    cliente_endereco = Label(janela_editar, text="Endereço")
    cliente_endereco.pack(padx=10, pady=10)
    cliente_endereco_entrada = Entry(janela_editar)
    cliente_endereco_entrada.pack(padx=10, pady=10)

    # Telefone
    cliente_telefone = Label(janela_editar, text="Telefone")
    cliente_telefone.pack(padx=10, pady=10)
    cliente_telefone_entrada = Entry(janela_editar)
    cliente_telefone_entrada.pack(padx=10, pady=10)

    # E-mail
    cliente_email = Label(janela_editar, text="E-mail")
    cliente_email.pack(padx=10, pady=10)
    cliente_email_entrada = Entry(janela_editar)
    cliente_email_entrada.pack(padx=10, pady=10)

    def preencher_campos(event):
        nome_selecionado = cliente_selecionar_entrada.get().strip()

        sessao = Session()
        cliente = sessao.query(Cliente).filter_by(nome=nome_selecionado).first()
        sessao.close()

        if cliente:
            cliente_nome_entrada.delete(0, END)
            cliente_endereco_entrada.delete(0, END)
            cliente_telefone_entrada.delete(0, END)
            cliente_email_entrada.delete(0, END)

            cliente_nome_entrada.insert(0, cliente.nome)
            cliente_endereco_entrada.insert(0, cliente.endereco)
            cliente_telefone_entrada.insert(0, cliente.telefone)
            cliente_email_entrada.insert(0, cliente.email)

    cliente_selecionar_entrada.bind("<<ComboboxSelected>>", preencher_campos)

    def atualizar_combobox():
        sessao = Session()
        clientes = sessao.query(Cliente).all()
        sessao.close()
        atualizado = [cliente.nome for cliente in clientes]
        cliente_selecionar_entrada['values'] = atualizado

    def salvar_alteracoes():
        nome_original = cliente_selecionar_entrada.get().strip()
        nome = cliente_nome_entrada.get().strip().title()
        endereco = cliente_endereco_entrada.get().strip()
        telefone = cliente_telefone_entrada.get().strip()
        email = cliente_email_entrada.get().strip().lower()
        if email == "não informado":
            email = "Não informado"

        if not nome:
            messagebox.showerror("Erro", 'Preencha o campo "nome"')
            return
        
        sessao = Session()
        try:
            cliente = sessao.query(Cliente).filter_by(nome = nome_original).first()
            if cliente:
                cliente.nome = nome
                cliente.endereco = endereco or "Não informado"
                cliente.telefone = telefone or "Não informado"
                cliente.email = email or "Não informado"
                sessao.commit()
                messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
                atualizar_combobox()
        finally:
            sessao.close()
    botao_salvar_editar = Button(janela_editar, text="Salvar", command=salvar_alteracoes)
    botao_salvar_editar.pack(padx=10, pady=10)


# Remover Cliente
def abrir_remover_cliente(janela_principal):
    janela_remover = Toplevel(janela_principal)
    janela_remover.title("Remover Cliente")
    janela_remover.geometry("500x300")
    janela_remover.grab_set()

    sessao = Session()
    clientes = sessao.query(Cliente).all()
    sessao.close()

    nome_clientes = [cliente.nome for cliente in clientes]

    # Selecionar Produto
    cliente_remover = Label(janela_remover, text="Selecionar Produto")
    cliente_remover.pack(padx=10, pady=10)
    cliente_remover_entrada = Combobox(janela_remover, values=nome_clientes)
    cliente_remover_entrada.pack(padx=10, pady=10)

    def atualizar_combobox():
        sessao = Session()
        clientes = sessao.query(Cliente).all()
        sessao.close()
        atualizado = [cliente.nome for cliente in clientes]
        cliente_remover_entrada['values'] = atualizado

    def salvar_alteracoes():
        cliente = cliente_remover_entrada.get().strip().capitalize()

        if not cliente:
            messagebox.showerror("Erro", "Nome do cliente não pode estar vazio.")
            return
        
        resposta = messagebox.askyesno("Confirmação", "Deseja remover este cliente?")
        if resposta:
            sessao = Session()
            try:
                remover = sessao.query(Cliente).filter(Cliente.nome == cliente).first()
                if not remover:
                    messagebox.showerror("Erro", "Cliente não existe.")
                    return
                else:
                    sessao.delete(remover)
                    sessao.commit()
                    messagebox.showinfo("Sucesso", "Produto removido com sucesso.")
                    atualizar_combobox()
                    return
            finally:
                sessao.close()
        else:
            return
    # Botão Salvar
    botao_salvar_remover = Button(janela_remover, text="Salvar", command=salvar_alteracoes)
    botao_salvar_remover.pack(padx=10, pady=10)