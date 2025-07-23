from setup_db import Session, Movimentacao
from tkinter import *
from treeviews import criar_treeview_movimentacao

# Movimentação
def abrir_movimentacao(janela_principal):
    janela_movimentacao = Toplevel(janela_principal)
    janela_movimentacao.title("Movimentações de Produtos")
    janela_movimentacao.geometry("700x400")
    janela_movimentacao.grab_set()

    colunas = criar_treeview_movimentacao(janela_movimentacao)
    colunas.pack(expand=True, fill="both", padx=10, pady=10)
    sessao = Session()
    try:
        movimentacoes = sessao.query(Movimentacao).all()
        for mov in movimentacoes:
            nome_produto = mov.produto.produto_nome if mov.produto else "Desconhecido"
            data_formatada = mov.data.strftime("%d/%m/%Y %H:%M:%S")
            nome_cliente = mov.cliente.nome if mov.cliente else "-"
            colunas.insert("", "end", values=(nome_produto, mov.tipo, mov.quantidade, data_formatada, nome_cliente))
    finally:
        sessao.close()




