import tkinter as tk
from tkinter import ttk


class CaixaComAutoCompletar(ttk.Combobox):
    def definir_lista_de_opcoes(self, lista_opcoes):
        """Recebe uma lista e configura o autocomplete."""
        self._lista_opcoes = sorted(lista_opcoes, key=str.lower)  # Ordena ignorando maiúsculas/minúsculas
        self._sugestoes = []  # Itens que coincidem com o que foi digitado
        self._indice_sugestao = 0  # Índice da sugestão atual
        self.posicao_cursor = 0  # Posição do cursor no texto
        self.bind('<KeyRelease>', self.ao_soltar_tecla)  # Chama função ao soltar uma tecla

    def completar_texto(self, ajuste=0):
        """Tenta completar o texto com base nas sugestões disponíveis."""
        if ajuste:
            self.delete(self.posicao_cursor, tk.END)
        else:
            self.posicao_cursor = len(self.get())

        sugestoes_atuais = []
        for item in self._lista_opcoes:
            if item.lower().startswith(self.get().lower()):
                sugestoes_atuais.append(item)

        if sugestoes_atuais != self._sugestoes:
            self._indice_sugestao = 0
            self._sugestoes = sugestoes_atuais

        if sugestoes_atuais:
            self.delete(0, tk.END)
            self.insert(0, sugestoes_atuais[self._indice_sugestao])
            self.select_range(self.posicao_cursor, tk.END)

    def ao_soltar_tecla(self, evento):
        """Lida com o evento de soltar uma tecla."""
        if evento.keysym in ("BackSpace", "Left", "Right", "Up", "Down"):
            return
        self.completar_texto()