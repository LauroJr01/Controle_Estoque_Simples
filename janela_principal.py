from setup_db import Session
from tkinter import *
from produtos import abrir_estoque, abrir_adicionar_produto, abrir_editar_produto, abrir_remover_produto
from entrada_saida import abrir_entrada_produto, abrir_saida_produto
from movimentacao import abrir_movimentacao
from clientes import abrir_lista_cliente, abrir_cadastro_cliente, abrir_editar_cliente, abrir_remover_cliente

def abrir_janela_principal():
    janela_principal = Tk()
    janela_principal.title("Controle de Estoque   |   Desenvolvido por Lauro Júnior")
    janela_principal.geometry("800x600")

    menu_barra = Menu(janela_principal)
    janela_principal.config(menu=menu_barra)

    # Menu Estoque
    menu_estoque = Menu(menu_barra, tearoff=0)
    menu_estoque.add_command(label="Visualizar Estoque", command=lambda: abrir_estoque(janela_principal))
    menu_estoque.add_command(label="Cadastrar Produto", command=lambda: abrir_adicionar_produto(janela_principal))
    menu_estoque.add_separator()
    menu_estoque.add_command(label="Editar Produto", command=lambda: abrir_editar_produto(janela_principal))
    menu_estoque.add_command(label="Remover Produto", command=lambda: abrir_remover_produto(janela_principal))
    menu_barra.add_cascade(label="Estoque", menu=menu_estoque)
    
    # Menu Movimentação
    menu_movimentacao = Menu(menu_barra, tearoff=0)
    menu_movimentacao.add_command(label="Ver Movimentações", command=lambda: abrir_movimentacao(janela_principal))
    menu_movimentacao.add_separator()
    menu_movimentacao.add_command(label="Entrada de Produto", command=lambda: abrir_entrada_produto(janela_principal))
    menu_movimentacao.add_command(label="Saída de Produto", command=lambda: abrir_saida_produto(janela_principal))
    menu_barra.add_cascade(label="Movimentações", menu=menu_movimentacao)
    
    # Menu Clientes
    menu_cliente = Menu(menu_barra, tearoff=0)
    menu_cliente.add_command(label="Lista de Clientes", command=lambda: abrir_lista_cliente(janela_principal))
    menu_cliente.add_command(label="Cadastrar Cliente", command=lambda: abrir_cadastro_cliente(janela_principal))
    menu_cliente.add_separator()
    menu_cliente.add_command(label="Editar Cliente", command=lambda: abrir_editar_cliente(janela_principal))
    menu_cliente.add_command(label="Remover Cliente", command=lambda: abrir_remover_cliente(janela_principal))
    menu_barra.add_cascade(label="Clientes", menu=menu_cliente)

    # Menu Relatórios
    menu_relatorio = Menu(menu_barra, tearoff=0)
    menu_relatorio.add_command(label="Relatório de Produtos")
    menu_relatorio.add_command(label="Relatório de Clientes")
    menu_relatorio.add_command(label="Relatório de Vendas")
    menu_barra.add_cascade(label="Relatórios", menu=menu_relatorio)

    # Menu Gráficos
    menu_grafico = Menu(menu_barra, tearoff=0)
    menu_grafico.add_command(label="Produtos com Maior Saída")
    menu_grafico.add_command(label="Producos com Menor Lucro")
    menu_grafico.add_command(label="Variação por Período")
    menu_barra.add_cascade(label="Gráficos", menu=menu_grafico)

    # Menu Ajuda
    menu_ajuda = Menu(menu_barra, tearoff=0)
    menu_ajuda.add_command(label="Sobre o Sistema")
    menu_barra.add_cascade(label="Ajuda", menu=menu_ajuda)        

    janela_principal.mainloop()
    