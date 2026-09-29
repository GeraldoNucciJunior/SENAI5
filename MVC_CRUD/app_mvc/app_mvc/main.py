"""Ponto de entrada: monta Models, Views e Controllers."""
import tkinter as tk
from tkinter import ttk

from database import init_db
from models.cadastro_model import ClienteModel, ProdutoModel
from models.movimento_model import MovimentoModel
from views.cadastro_view import CadastroView
from views.movimento_view import MovimentoView
from controllers.cadastro_controller import CadastroController
from controllers.movimento_controller import MovimentoController


def main():
    init_db()
    root = tk.Tk()
    root.title("Cadastro MVC - Python + SQLite")
    root.geometry("620x520")

    abas = ttk.Notebook(root)
    abas.pack(fill="both", expand=True)

    cliente_model, produto_model = ClienteModel(), ProdutoModel()

    v_cliente = CadastroView(abas, "Cliente")
    v_produto = CadastroView(abas, "Produto")
    v_mov = MovimentoView(abas)
    abas.add(v_cliente, text="Clientes")
    abas.add(v_produto, text="Produtos")
    abas.add(v_mov, text="Movimentos")

    CadastroController(cliente_model, v_cliente, "cliente")
    CadastroController(produto_model, v_produto, "produto")
    c_mov = MovimentoController(MovimentoModel(), v_mov, cliente_model, produto_model)

    # ao abrir a aba de movimentos, recarrega clientes/produtos nos combos
    abas.bind("<<NotebookTabChanged>>",
              lambda e: c_mov.atualizar() if abas.select() == str(v_mov) else None)

    root.mainloop()


if __name__ == "__main__":
    main()
