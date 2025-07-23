from tkinter import *
from tkinter import ttk

# TreeView Estoque
def criar_treeview_estoque(janela_estoque):
    tree = ttk.Treeview(janela_estoque, columns=("Nome", "Quantidade", "Preço Custo", "Preço Venda"), show="headings")
    tree.heading("Nome", text="Nome do Produto")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Preço Custo", text="Preço de Custo")
    tree.heading("Preço Venda", text="Preço de Venda")
    
    tree.column("Nome", width=150, anchor="center")
    tree.column("Quantidade", width=100, anchor="center")
    tree.column("Preço Custo", width=100, anchor="center")
    tree.column("Preço Venda", width=100, anchor="center")
    return tree

# Treeview Movimentação
def criar_treeview_movimentacao(janela_movimentacao):
    tree = ttk.Treeview(janela_movimentacao, columns=("Nome", "Tipo", "Quantidade", "Data", "Cliente"), show="headings")
    tree.heading("Nome", text="Nome do Produto")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Data", text="Data/Hora")
    tree.heading("Cliente", text="Cliente")

    tree.column("Nome", width=150, anchor="center")
    tree.column("Tipo", width=100, anchor="center")
    tree.column("Quantidade", width=100, anchor="center")
    tree.column("Data", width=150, anchor="center")
    tree.column("Cliente", width=150, anchor="center")
    return tree

# Treeview Clientes
def criar_treeview_cliente(janela_cliente):
    tree = ttk.Treeview(janela_cliente, columns=("Nome", "Endereço", "Telefone", "E-mail"), show="headings")
    tree.heading("Nome", text="Nome do Cliente")
    tree.heading("Endereço", text="Endereço")
    tree.heading("Telefone", text="Telefone")
    tree.heading("E-mail", text="E-mail")
    

    tree.column("Nome", width=150, anchor="center")
    tree.column("Endereço", width=150, anchor="center")
    tree.column("Telefone", width=100, anchor="center")
    tree.column("E-mail", width=150, anchor="center")
    return tree

