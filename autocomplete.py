import tkinter as tk
from tkinter import ttk


class CaixaComAutoCompletar(ttk.Combobox):
    def definir_lista_de_opcoes(self, lista_opcoes):
        self._lista_opcoes = sorted(lista_opcoes, key=str.lower)
        self._sugestoes = []
        self._indice_sugestao = 0
        self.posicao_cursor = 0
        self.bind("<KeyRelease>", self.ao_soltar_tecla)

    def completar_texto(self, ajuste=0):
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
        if evento.keysym in ("BackSpace", "Left", "Right", "Up", "Down"):
            return
        self.completar_texto()






























'''class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def autocomplete(self, delta=0):
        if delta:
            self.delete(self.position, tk.END)
        else:
            self.position = len(self.get())

        _hits = []
        for item in self._completion_list:
            if item.lower().startswith(self.get().lower()):
                _hits.append(item)

        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits

        if _hits:
            self.delete(0, tk.END)
            self.insert(0, _hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        if event.keysym in ("BackSpace", "Left", "Right", "Up", "Down"):
            return
        self.autocomplete()
'''