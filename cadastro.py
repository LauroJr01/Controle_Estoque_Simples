from setup_db import Session, Usuario
from tkinter import *
from tkinter import messagebox

# Fazer Cadastro
def abrir_cadastro(janela_principal):
    janela_cadastro = Toplevel(janela_principal)
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("300x200")    
    janela_cadastro.grab_set()

    # Nome
    nome_cadastro = Label(janela_cadastro, text="Nome")
    nome_cadastro.pack(padx=5, pady=5)
    nome_cadastro_entrada = Entry(janela_cadastro)
    nome_cadastro_entrada.pack(padx=5, pady=5)

    # Senha
    senha_cadastro = Label(janela_cadastro, text="Senha")
    senha_cadastro.pack(padx=5, pady=5)
    senha_cadastro_entrada = Entry(janela_cadastro, show="*")
    senha_cadastro_entrada.pack(padx=5, pady=5)

    # DEF Cadastrar Usuário
    def cadastrar_usuario():
        nome = nome_cadastro_entrada.get()
        senha = senha_cadastro_entrada.get()
        if not nome or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
        
        sessao = Session()
        try:
            usuario_existente = sessao.query(Usuario).filter_by(nome=nome).first()
            if usuario_existente:
                messagebox.showerror("Erro", "Usuário já existe.")
                return            
            novo_usuario = Usuario(nome=nome, senha=senha)
            sessao.add(novo_usuario)
            sessao.commit()        
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            janela_cadastro.destroy()
        finally:
            sessao.close()
    # Botão Salvar
    botao_salvar_cadastro = Button(janela_cadastro, text="Salvar", command=cadastrar_usuario)
    botao_salvar_cadastro.pack(padx=10, pady=10)