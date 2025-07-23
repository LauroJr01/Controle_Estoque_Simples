from setup_db import Session, Usuario
from tkinter import *
from tkinter import messagebox
from cadastro import abrir_cadastro
from alterar_senha import abrir_alterar_senha
from janela_principal import abrir_janela_principal

# Janela
janela_login = Tk()
janela_login.title('Controle de Estoque     |     Desenvolvido por Lauro Júnior')
janela_login.geometry('600x400')

# Nome
nome_label = Label(janela_login, text="Nome")
nome_label.pack(padx=10, pady=10)
nome_entrada = Entry(janela_login)
nome_entrada.pack(padx=10, pady=10)

# Senha
senha_label = Label(janela_login, text="Senha")
senha_label.pack(padx=10, pady=10)
senha_entrada = Entry(janela_login, show="*")
senha_entrada.pack(padx=10, pady=10)

# Verificar Login
def verificar_login():
    nome = nome_entrada.get()
    senha = senha_entrada.get()
    
    sessao = Session()
    try:
        usuario = sessao.query(Usuario).filter_by(nome=nome, senha=senha).first()
        if usuario:
            messagebox.showinfo("Login", "Login válido!")
            janela_login.destroy()
            abrir_janela_principal()
            return
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            return
    finally:        
        sessao.close()

# Botão Entrar   
botao_enviar = Button(janela_login, text="Entrar", command=verificar_login)
botao_enviar.pack(padx=10, pady=10)

# Botão Alterar Senha
alterar_senha = Button(janela_login, text="Alterar Senha", command=lambda: abrir_alterar_senha(janela_login))
alterar_senha.pack(padx=10, pady=10)

# Botão Cadastre-se
botao_cadastro = Button(janela_login, text="Cadastre-se", command=lambda: abrir_cadastro(janela_login))
botao_cadastro.pack(padx=10, pady=10)

janela_login.mainloop()