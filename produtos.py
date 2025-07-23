from setup_db import Session, Produto
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from treeviews import criar_treeview_estoque


# Estoque
def abrir_estoque(janela_principal):
    janela_estoque = Toplevel(janela_principal)
    janela_estoque.title("Estoque de Produtos")
    janela_estoque.geometry("600x400")
    janela_estoque.grab_set()

    colunas = criar_treeview_estoque(janela_estoque)
    colunas.pack(expand=True, fill="both", padx=10, pady=10)
    sessao = Session()
    try:
        produtos = sessao.query(Produto).all()
        for produto in produtos:
            preco_custo_formatado = f'R$ {produto.preco_custo:.2f}'
            preco_venda_formatado = f'R$ {produto.preco_venda:.2f}'
            colunas.insert("", "end", values=(produto.produto_nome, produto.quantidade, preco_custo_formatado, preco_venda_formatado))
    finally:    
        sessao.close()


# Adicionar Produto
def abrir_adicionar_produto(janela_principal):
    janela_cadastrar = Toplevel(janela_principal)
    janela_cadastrar.title("Cadastrar Produto")
    janela_cadastrar.geometry("500x300")
    janela_cadastrar.grab_set()

    # Produto
    produto_cadastrar = Label(janela_cadastrar, text="Nome")
    produto_cadastrar.pack(padx=10, pady=10)
    produto_cadastrar_entrada = Entry(janela_cadastrar)
    produto_cadastrar_entrada.pack(padx=10, pady=10)

    # Preço de Custo
    preco_custo_cadastrar = Label(janela_cadastrar, text="Preço de Custo")
    preco_custo_cadastrar.pack(padx=10, pady=10)
    preco_custo_cadastrar_entrada = Entry(janela_cadastrar)
    preco_custo_cadastrar_entrada.pack(padx=10, pady=10)

    # Preço de Venda
    preco_venda_cadastrar = Label(janela_cadastrar, text="Preço de Venda")
    preco_venda_cadastrar.pack(padx=10, pady=10)
    preco_venda_cadastrar_entrada = Entry(janela_cadastrar)
    preco_venda_cadastrar_entrada.pack(padx=10, pady=10)

    # DEF Adicinar Produto
    def adicionar_produto():
        produto = produto_cadastrar_entrada.get().strip().capitalize()
        preco_custo_str = preco_custo_cadastrar_entrada.get().replace(",", ".")
        preco_venda_str = preco_venda_cadastrar_entrada.get().replace(",", ".")

        if not produto:
            messagebox.showerror("Error", "Nome do produto não pode estar vazio.")
            return
        try:
            preco_custo = float(preco_custo_str)
            preco_venda = float(preco_venda_str)
            if preco_custo < 0 or preco_venda < 0:
                messagebox.showerror("Erro", "Preço não pode ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido. Insira um número.")
            return

        sessao = Session()
        try:
            adicionar = sessao.query(Produto).filter(Produto.produto_nome == produto).first()
            if adicionar:
                messagebox.showerror("Erro", "Produto já existe.")
                return
            else:
                novo_produto = Produto(produto_nome=produto, preco_custo=preco_custo,preco_venda=preco_venda, quantidade=0)
                sessao.add(novo_produto)
                sessao.commit()
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso.")
                return
        finally:
            sessao.close()
    # Botão Salvar
    botao_salvar_cadastrar = Button(janela_cadastrar, text="Salvar", command=adicionar_produto)
    botao_salvar_cadastrar.pack(padx=10, pady=10)


# Editar Produto
def abrir_editar_produto(janela_principal):
    janela_editar = Toplevel(janela_principal)
    janela_editar.title("Editar Produto")
    janela_editar.geometry("500x400")
    janela_editar.grab_set()

    sessao = Session()
    produtos = sessao.query(Produto).all()
    sessao.close()

    nome_produtos = [produto.produto_nome for produto in produtos]

    # Selecionar Produto
    produto_selecionar = Label(janela_editar, text="Selecionar Produto")
    produto_selecionar.pack(padx=10, pady=10)
    produto_selecionar_entrada = Combobox(janela_editar, values=nome_produtos)
    produto_selecionar_entrada.pack(padx=10, pady=10)

    # Produto
    produto_editar = Label(janela_editar, text="Nome")
    produto_editar.pack(padx=10, pady=10)
    produto_editar_entrada = Entry(janela_editar)
    produto_editar_entrada.pack(padx=10, pady=10)

    # Preço de Custo
    preco_custo_editar = Label(janela_editar, text="Preço de Custo")
    preco_custo_editar.pack(padx=10, pady=10)
    preco_custo_editar_entrada = Entry(janela_editar)
    preco_custo_editar_entrada.pack(padx=10, pady=10)

    # Preço de Venda
    preco_venda_editar = Label(janela_editar, text="Preço de Venda")
    preco_venda_editar.pack(padx=10, pady=10)
    preco_venda_editar_entrada = Entry(janela_editar)
    preco_venda_editar_entrada.pack(padx=10, pady=10)

    def preencher_campos(event):
        produto_selecionado = produto_selecionar_entrada.get().strip()

        sessao = Session()
        produto = sessao.query(Produto).filter_by(produto_nome=produto_selecionado).first()
        sessao.close()

        if produto:
            produto_editar_entrada.delete(0, END)
            preco_custo_editar_entrada.delete(0, END)
            preco_venda_editar_entrada.delete(0, END)

            produto_editar_entrada.insert(0, produto.produto_nome)
            preco_custo_editar_entrada.insert(0, produto.preco_custo)
            preco_venda_editar_entrada.insert(0, produto.preco_venda)

    produto_selecionar_entrada.bind("<<ComboboxSelected>>", preencher_campos)
    
    def atualizar_combobox():
        sessao = Session()
        produtos = sessao.query(Produto).all()
        sessao.close()
        atualizado = [produto.produto_nome for produto in produtos]
        produto_selecionar_entrada['values'] = atualizado
    
    def salvar_alteracoes():
        produto_original = produto_selecionar_entrada.get().strip()
        produto_nome = produto_editar_entrada.get().strip().capitalize()
        preco_custo_str = preco_custo_editar_entrada.get().strip().replace(",", ".")
        preco_venda_str = preco_venda_editar_entrada.get().strip().replace(",", ".")
        
        if not produto_nome:
            messagebox.showerror("Erro", 'Preencha o campo "Produto"')
            return
        try:
            preco_custo = float(preco_custo_str)
            preco_venda = float(preco_venda_str)
            if preco_custo < 0 or preco_venda < 0:
                messagebox.showerror("Erro", "Preço não pode ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido. Insira um número.")
            return

        sessao = Session()
        try:
            produto = sessao.query(Produto).filter_by(produto_nome=produto_original).first()
            if produto:
                produto.produto_nome = produto_nome
                produto.preco_custo = preco_custo
                produto.preco_venda = preco_venda
                sessao.commit()
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
                atualizar_combobox()
        finally:
            sessao.close()
    botao_salvar_editar = Button(janela_editar, text="Salvar", command=salvar_alteracoes)
    botao_salvar_editar.pack(padx=10, pady=10)



# Remover Produto
def abrir_remover_produto(janela_principal):
    janela_remover = Toplevel(janela_principal)
    janela_remover.title("Remover Produto")
    janela_remover.geometry("500x300")
    janela_remover.grab_set()
    
    sessao = Session()
    produtos = sessao.query(Produto).all()
    sessao.close()

    nome_produtos = [produto.produto_nome for produto in produtos]

    # Selecionar Produto
    produto_remover = Label(janela_remover, text="Selecionar Produto")
    produto_remover.pack(padx=10, pady=10)    
    produto_remover_entrada = Combobox(janela_remover, values=nome_produtos)
    produto_remover_entrada.pack(padx=10, pady=10)

    def atualizar_combobox():
        sessao = Session()
        produtos = sessao.query(Produto).all()
        sessao.close()
        atualizado = [produto.produto_nome for produto in produtos]
        produto_remover_entrada['values'] = atualizado
    
    def salvar_alteracoes():
        produto = produto_remover_entrada.get().strip().capitalize()

        if not produto:
            messagebox.showerror("Erro","Nome do produto não pode estar vazio.")
            return
        
        resposta = messagebox.askyesno("Confirmação", "Deseja remover este produto?")
        if resposta:
            sessao = Session()
            try:
                remover = sessao.query(Produto).filter(Produto.produto_nome == produto).first()
                if not remover:
                    messagebox.showerror("Erro", "Produto não existe.")
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


















    # DEF Remover Produto
    '''def remover_produto():
        produto = produto_entrada_remover.get().strip().capitalize()

        if not produto:
            messagebox.showerror("Erro","Nome do produto não pode estar vazio.")
            return
        
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente remover este produto?")
        if resposta:
            sessao = Session()
            try:
                remover = sessao.query(Produto).filter(Produto.produto_nome == produto).first()
                if not remover:
                    messagebox.showerror("Erro", "Produto não existe.")
                    return
                else:
                    sessao.delete(remover)
                    sessao.commit()
                    messagebox.showinfo("Sucesso", "Produto removido com sucesso.")
                    return
            finally:
                sessao.close()
        else:
            return   
    # Botão Salvar
    botao_salvar_remover = Button(janela_remover, text="Salvar", command=remover_produto)
    botao_salvar_remover.pack(padx=10, pady=10)'''



















     # DEF Editar Produto
    '''def editar_produto():
        produto = produto_entrada_editar.get().strip().capitalize()
        preco_custo_str = preco_custo_entrada_editar.get().replace(",", ".")
        preco_venda_str = preco_venda_entrada_editar.get().replace(",", ".")

        if not produto:
            messagebox.showerror("Erro","Nome do produto não pode estar vazio.")
            return
        try:
            preco_custo = float(preco_custo_str)
            preco_venda = float(preco_venda_str)
            if preco_custo < 0 or preco_venda < 0:
                messagebox.showerror("Erro", "Preço não pode ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido. Insira um número.")
            return

        sessao=Session()
        try:
            editar = sessao.query(Produto).filter(Produto.produto_nome == produto).first()
            if not editar:
                messagebox.showerror("Erro", "Produto não existe.")
                return
            else:
                editar.preco_custo = preco_custo
                editar.preco_venda = preco_venda
                sessao.commit()
                messagebox.showinfo("Sucesso", "Produto alterado com sucesso.")
                return
        finally:
            sessao.close()
    # Botão Salvar
    botao_salvar_editar = Button(janela_editar, text="Salvar", command=editar_produto)
    botao_salvar_editar.pack(padx=10, pady=10)'''