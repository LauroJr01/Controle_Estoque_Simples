from setup_db import Session, Produto, Movimentacao, Cliente
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter.ttk import Combobox
from ttkwidgets.autocomplete import AutocompleteCombobox
from clientes import abrir_cadastro_cliente


# Entrada Produto
def abrir_entrada_produto(janela_principal):
    janela_entrada = Toplevel(janela_principal)
    janela_entrada.title("Controle de Entrada")
    janela_entrada.geometry("500x400")
    janela_entrada.grab_set()

    sessao = Session()
    produtos = sessao.query(Produto).all()
    sessao.close()

    sessao = Session()
    clientes = sessao.query(Cliente).all()
    sessao.close()

    nome_produtos = [produto.produto_nome for produto in produtos]
    nome_clientes = [cliente.nome for cliente in clientes]


    # Selecionar Produto
    produto_selecionar = Label(janela_entrada, text="Selecionar Produto")
    produto_selecionar.pack(padx=10, pady=10)
    produto_selecionar_entrada = AutocompleteCombobox(janela_entrada, completevalues=nome_produtos)
    produto_selecionar_entrada.pack(padx=10, pady=10)

    # Quantidade
    quantidade_entrada = Label(janela_entrada, text="Quantidade")
    quantidade_entrada.pack(padx=10, pady=10)
    quantidade_entrada_entrada = Entry(janela_entrada)
    quantidade_entrada_entrada.pack(padx=10, pady=10)

    # Selecionar Cliente
    cliente_selecionar = Label(janela_entrada, text="Selecionar Cliente")
    cliente_selecionar.pack(padx=10, pady=10)
    cliente_selecionar_entrada = AutocompleteCombobox(janela_entrada, completevalues=nome_clientes)
    cliente_selecionar_entrada.pack(padx=10, pady=10)

    # DEF Atualizar Clientes Combobox
    def atualizar_clientes_combobox():
        sessao = Session()
        clientes = sessao.query(Cliente).all()
        sessao.close()
        nome_clientes = [cliente.nome for cliente in clientes]
        cliente_selecionar_entrada['values'] = nome_clientes

    # DEF Entrada Produto
    def entrada_produto():
        produto = produto_selecionar_entrada.get().strip().title()
        quantidade_str = quantidade_entrada_entrada.get()
        cliente_nome = cliente_selecionar_entrada.get().strip()
        try:
            quantidade = int(quantidade_str)
            if quantidade < 0:
                messagebox.showerror("Erro", "Quantidade não pode ser negativa.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida. Insira um número.")
            return
        
        if not produto:
            messagebox.showerror("Erro", "Nome do produto não pode estar vazio.")
            return
        elif not quantidade:
            messagebox.showerror("Erro", "Quantidade do produto não pode estar vazio.")
            return
        elif not cliente_nome:
            messagebox.showerror("Error", "Selecione um cliente.")
            return

        sessao = Session()
        try:
            entrada = sessao.query(Produto).filter(Produto.produto_nome == produto).first()
            cliente = sessao.query(Cliente).filter_by(nome=cliente_nome).first()

            if not entrada:
                messagebox.showerror("Erro", "Produto não encontrado.")
                return
            
            if not cliente:
                deseja_cadastrar = messagebox.askyesno("Cliente não encontrado.", f'O cliente "{cliente_nome}" não está cadastrado. \nDeseja cadastrar agora? ')
                if deseja_cadastrar:
                    abrir_cadastro_cliente(janela_entrada)
                    janela_entrada.grab_set()
                    
                    def atualizar_uma_vez(event):
                        atualizar_clientes_combobox()
                        janela_entrada.unbind("<FocusIn>")
                        
                    janela_entrada.bind("<FocusIn>", atualizar_uma_vez)
                    janela_entrada.deiconify()
                    janela_entrada.lift()
                    janela_entrada.grab_set()
                return

            entrada.quantidade += quantidade
            nova_movimentacao = Movimentacao(produto_id=entrada.id, tipo="Entrada", quantidade=quantidade, data=datetime.now(), cliente_id=cliente.id)
            sessao.add(nova_movimentacao)
            sessao.commit()
            messagebox.showinfo("Sucesso", "Produto alterado com sucesso.")
            return
        finally:
            sessao.close()
    # Botão Salvar        
    botao_salvar_entrada = Button(janela_entrada, text="Salvar", command=entrada_produto)
    botao_salvar_entrada.pack(padx=10, pady=10)


# Saída Produto
def abrir_saida_produto(janela_principal):
    janela_saida = Toplevel(janela_principal)
    janela_saida.title("Controle de Saída")
    janela_saida.geometry("500x400")
    janela_saida.grab_set()

    sessao = Session()
    produtos = sessao.query(Produto).all()
    sessao.close()

    sessao = Session()
    clientes = sessao.query(Cliente).all()
    sessao.close()

    nome_produtos = [produto.produto_nome for produto in produtos]
    nome_clientes = [cliente.nome for cliente in clientes]

    # Selecionar Produto
    produto_selecionar = Label(janela_saida, text="Selecionar Produto")
    produto_selecionar.pack(padx=10, pady=10)
    produto_selecionar_entrada = Combobox(janela_saida, values=nome_produtos)
    produto_selecionar_entrada.pack(padx=10, pady=10)

    # Quantidade
    quantidade_saida = Label(janela_saida, text="Quantidade")
    quantidade_saida.pack(padx=10, pady=10)
    quantidade_saida_entrada = Entry(janela_saida)
    quantidade_saida_entrada.pack(padx=10, pady=10)

    # Selecionar Cliente
    cliente_selecionar = Label(janela_saida, text="Selecionar Cliente")
    cliente_selecionar.pack(padx=10, pady=10)
    cliente_selecionar_entrada = Combobox(janela_saida, values=nome_clientes)
    cliente_selecionar_entrada.pack(padx=10, pady=10)

    # DEF Atualizar Clientes Combobox
    def atualizar_clientes_combobox():
        sessao = Session()
        clientes = sessao.query(Cliente).all()
        sessao.close()
        nome_clientes = [cliente.nome for cliente in clientes]
        cliente_selecionar_entrada['values'] = nome_clientes
    
    # DEF Saída Produto
    def saida_produto():
        produto = produto_selecionar_entrada.get().strip().capitalize()
        quantidade_str = quantidade_saida_entrada.get()
        cliente_nome = cliente_selecionar_entrada.get().strip()
        try:
            quantidade = int(quantidade_str)
            if quantidade < 0:
                messagebox.showerror("Erro", "Quantidade não pode ser negativa.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida. Insira um número.")
            return
       
        if not produto:
            messagebox.showerror("Erro", "Nome do produto não pode estar vazio.")
            return
        elif not quantidade:
            messagebox.showerror("Erro", "Quantidade do produto não pode estar vazio.")
            return
        elif not cliente_nome:
            messagebox.showerror("Error", "Selecione um cliente.")
            return


        sessao = Session()
        try:
            saida = sessao.query(Produto).filter(Produto.produto_nome == produto).first()
            cliente = sessao.query(Cliente).filter_by(nome=cliente_nome).first()

            if not saida:
                messagebox.showerror("Erro", "Produto não encontrado.")
                return

            if not cliente:
                deseja_cadastrar = messagebox.askyesno("Cliente não encontrado.", f'O cliente "{cliente_nome}" não está cadastrado. \nDeseja cadastrar agora? ')
                if deseja_cadastrar:
                    abrir_cadastro_cliente(janela_saida)
                    janela_saida.grab_set()

                    def atualizar_uma_vez(event):
                        atualizar_clientes_combobox()
                        janela_saida.unbind("<FocusIn>")
                        
                    janela_saida.bind("<FocusIn>", atualizar_uma_vez)
                    janela_saida.deiconify()
                    janela_saida.lift()
                    janela_saida.grab_set()
                return

            if saida.quantidade < quantidade:
                messagebox.showerror("Erro", "Produto não possui está quantidade no estoque.")
                return
            else:
                saida.quantidade -= quantidade 
                nova_movimentacao = Movimentacao(produto_id=saida.id, tipo="Saída", quantidade=quantidade, data=datetime.now(), cliente_id=cliente.id)
                sessao.add(nova_movimentacao)
                sessao.commit()
                messagebox.showinfo("Sucesso", "Produto alterado com sucesso.")
                return
        finally:
            sessao.close()
    # Botão Salvar
    botao_salvar_saida = Button(janela_saida, text="Salvar", command=saida_produto)
    botao_salvar_saida.pack(padx=10, pady=10)

