"""View de movimento (data, cliente, produto)."""
import tkinter as tk
from tkinter import ttk, messagebox


class MovimentoView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.controller = None
        self.var_data = tk.StringVar()
        self.var_cliente = tk.StringVar()
        self.var_produto = tk.StringVar()

        form = ttk.LabelFrame(self, text="Movimento", padding=10)
        form.pack(fill="x")
        ttk.Label(form, text="Data (dd/mm/aaaa)").grid(row=0, column=0, sticky="w")
        ttk.Entry(form, textvariable=self.var_data, width=14).grid(row=0, column=1, padx=6, pady=3, sticky="w")
        ttk.Label(form, text="Cliente").grid(row=1, column=0, sticky="w")
        self.cb_cliente = ttk.Combobox(form, textvariable=self.var_cliente, state="readonly", width=38)
        self.cb_cliente.grid(row=1, column=1, padx=6, pady=3, sticky="w")
        ttk.Label(form, text="Produto").grid(row=2, column=0, sticky="w")
        self.cb_produto = ttk.Combobox(form, textvariable=self.var_produto, state="readonly", width=38)
        self.cb_produto.grid(row=2, column=1, padx=6, pady=3, sticky="w")

        botoes = ttk.Frame(form)
        botoes.grid(row=3, column=0, columnspan=2, pady=(8, 0), sticky="w")
        ttk.Button(botoes, text="Novo", command=lambda: self.controller.novo()).pack(side="left")
        ttk.Button(botoes, text="Salvar", command=lambda: self.controller.salvar()).pack(side="left", padx=6)
        ttk.Button(botoes, text="Excluir", command=lambda: self.controller.excluir()).pack(side="left")

        cols = ("id", "data", "cliente", "produto")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)
        for col, txt, w in (("id", "ID", 50), ("data", "Data", 90),
                            ("cliente", "Cliente", 220), ("produto", "Produto", 220)):
            self.tree.heading(col, text=txt)
            self.tree.column(col, width=w)
        self.tree.pack(fill="both", expand=True, pady=(10, 0))
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.controller.selecionar())

    # --- interface usada pelo controller ---
    def get_dados(self):
        return self.var_data.get().strip(), self.var_cliente.get(), self.var_produto.get()

    def set_dados(self, data, cliente, produto):
        self.var_data.set(data)
        self.var_cliente.set(cliente)
        self.var_produto.set(produto)

    def carregar_combos(self, clientes, produtos):
        self.cb_cliente["values"] = clientes
        self.cb_produto["values"] = produtos

    def carregar_lista(self, linhas):
        self.tree.delete(*self.tree.get_children())
        for iid, valores in linhas:
            self.tree.insert("", "end", iid=str(iid), values=valores)

    def item_selecionado(self):
        sel = self.tree.selection()
        return int(sel[0]) if sel else None

    def limpar_selecao(self):
        self.tree.selection_remove(self.tree.selection())

    def mostrar_erro(self, msg):
        messagebox.showerror("Erro", msg)

    def mostrar_info(self, msg):
        messagebox.showinfo("Informação", msg)

    def confirmar(self, msg):
        return messagebox.askyesno("Confirmar", msg)
