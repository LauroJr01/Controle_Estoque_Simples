from setup_db import Session, Usuario
from tkinter import *
from tkinter import messagebox

# Alterar Senha
def abrir_alterar_senha(janela_principal):
    janela_senha = Toplevel(janela_principal)
    janela_senha.title("Alterar Senha")
    janela_senha.geometry("300x250")    
    janela_senha.grab_set()

    # Nome
    nome_senha = Label(janela_senha, text="Nome")
    nome_senha.pack(padx=5, pady=5)
    nome_entrada_senha = Entry(janela_senha)
    nome_entrada_senha.pack(padx=5, pady=5)

    # Senha Atual
    senha_atual_senha = Label(janela_senha, text="Senha Atual")
    senha_atual_senha.pack(padx=5, pady=5)
    senha_atual_entrada_senha = Entry(janela_senha, show="*")
    senha_atual_entrada_senha.pack(padx=5, pady=5)

    # Senha Nova
    senha_nova_senha = Label(janela_senha, text="Nova Senha")
    senha_nova_senha.pack(padx=5, pady=5)
    senha_nova_entrada_senha = Entry(janela_senha, show="*")
    senha_nova_entrada_senha.pack(padx=5, pady=5)

    # DEF Alterar Senha
    def alterar_senha():
        nome = nome_entrada_senha.get()
        senha_atual = senha_atual_entrada_senha.get()
        senha_nova = senha_nova_entrada_senha.get()
        if not nome or not senha_atual or not senha_nova:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
        
        sessao = Session()
        try:
            usuario = sessao.query(Usuario).filter_by(nome=nome, senha=senha_atual).first()
            if usuario:
                usuario.senha = senha_nova
                sessao.commit()
                messagebox.showinfo("Sucesso", "Senha alterada com sucesso.")
                janela_senha.destroy()
                return
            else:
                messagebox.showwarning("Erro", "Senha atual incorreta.")
                return
        finally:
            sessao.close()
    # Botão Salvar
    botao_salvar_senha = Button(janela_senha, text="Alterar Senha", command=alterar_senha)
    botao_salvar_senha.pack(padx=5, pady=5)
