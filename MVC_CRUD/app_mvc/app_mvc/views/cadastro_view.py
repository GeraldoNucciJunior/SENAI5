"""View genérica de cadastro (codigo, nome) — usada por Cliente e Produto."""
import tkinter as tk
from tkinter import ttk, messagebox


class CadastroView(ttk.Frame):
    def __init__(self, parent, titulo):
        super().__init__(parent, padding=10)
        self.controller = None
        self.var_codigo = tk.StringVar()
        self.var_nome = tk.StringVar()

        form = ttk.LabelFrame(self, text=titulo, padding=10)
        form.pack(fill="x")
        ttk.Label(form, text="Código").grid(row=0, column=0, sticky="w")
        self.ent_codigo = ttk.Entry(form, textvariable=self.var_codigo, width=12)
        self.ent_codigo.grid(row=0, column=1, padx=6, pady=3, sticky="w")
        ttk.Label(form, text="Nome").grid(row=1, column=0, sticky="w")
        ttk.Entry(form, textvariable=self.var_nome, width=40).grid(
            row=1, column=1, padx=6, pady=3, sticky="w"
        )

        botoes = ttk.Frame(form)
        botoes.grid(row=2, column=0, columnspan=2, pady=(8, 0), sticky="w")
        ttk.Button(botoes, text="Novo", command=lambda: self.controller.novo()).pack(side="left")
        ttk.Button(botoes, text="Salvar", command=lambda: self.controller.salvar()).pack(side="left", padx=6)
        ttk.Button(botoes, text="Excluir", command=lambda: self.controller.excluir()).pack(side="left")

        self.tree = ttk.Treeview(self, columns=("codigo", "nome"), show="headings", height=12)
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.column("codigo", width=80, anchor="center")
        self.tree.column("nome", width=300)
        self.tree.pack(fill="both", expand=True, pady=(10, 0))
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.controller.selecionar())

    # --- interface usada pelo controller ---
    def get_dados(self):
        return self.var_codigo.get().strip(), self.var_nome.get().strip()

    def set_dados(self, codigo, nome):
        self.var_codigo.set(codigo)
        self.var_nome.set(nome)

    def bloquear_codigo(self, bloquear):
        self.ent_codigo.config(state="disabled" if bloquear else "normal")

    def carregar_lista(self, registros):
        self.tree.delete(*self.tree.get_children())
        for r in registros:
            self.tree.insert("", "end", iid=str(r["codigo"]), values=(r["codigo"], r["nome"]))

    def item_selecionado(self):
        sel = self.tree.selection()
        return self.tree.item(sel[0], "values") if sel else None

    def limpar_selecao(self):
        self.tree.selection_remove(self.tree.selection())

    def mostrar_erro(self, msg):
        messagebox.showerror("Erro", msg)

    def mostrar_info(self, msg):
        messagebox.showinfo("Informação", msg)

    def confirmar(self, msg):
        return messagebox.askyesno("Confirmar", msg)
