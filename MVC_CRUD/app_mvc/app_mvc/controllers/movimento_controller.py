"""Controller de Movimento."""
from datetime import datetime


class MovimentoController:
    def __init__(self, model, view, cliente_model, produto_model):
        self.model = model
        self.view = view
        self.cliente_model = cliente_model
        self.produto_model = produto_model
        self.id_editando = None
        view.controller = self
        self.atualizar()

    def atualizar(self):
        """Recarrega combos e lista (chamado ao abrir a aba)."""
        clientes = [f"{c['codigo']} - {c['nome']}" for c in self.cliente_model.listar()]
        produtos = [f"{p['codigo']} - {p['nome']}" for p in self.produto_model.listar()]
        self.view.carregar_combos(clientes, produtos)
        self._carregar_lista()

    def _carregar_lista(self):
        linhas = []
        for m in self.model.listar():
            data_br = datetime.strptime(m["data"], "%Y-%m-%d").strftime("%d/%m/%Y")
            linhas.append((m["id"], (
                m["id"], data_br,
                f"{m['codigo_cliente']} - {m['nome_cliente']}",
                f"{m['codigo_produto']} - {m['nome_produto']}",
            )))
        self.view.carregar_lista(linhas)

    def novo(self):
        self.id_editando = None
        self.view.limpar_selecao()
        self.view.set_dados("", "", "")

    def selecionar(self):
        id_ = self.view.item_selecionado()
        if id_ is None:
            return
        for m in self.model.listar():
            if m["id"] == id_:
                self.id_editando = id_
                self.view.set_dados(
                    datetime.strptime(m["data"], "%Y-%m-%d").strftime("%d/%m/%Y"),
                    f"{m['codigo_cliente']} - {m['nome_cliente']}",
                    f"{m['codigo_produto']} - {m['nome_produto']}",
                )
                break

    def salvar(self):
        data_txt, cliente, produto = self.view.get_dados()
        try:
            data_iso = datetime.strptime(data_txt, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return self.view.mostrar_erro("Data inválida. Use dd/mm/aaaa.")
        if not cliente or not produto:
            return self.view.mostrar_erro("Selecione o cliente e o produto.")
        cod_cli = int(cliente.split(" - ")[0])
        cod_prod = int(produto.split(" - ")[0])
        try:
            if self.id_editando is None:
                self.model.inserir(data_iso, cod_cli, cod_prod)
            else:
                self.model.atualizar(self.id_editando, data_iso, cod_cli, cod_prod)
        except ValueError as e:
            return self.view.mostrar_erro(str(e))
        self._carregar_lista()
        self.novo()

    def excluir(self):
        id_ = self.view.item_selecionado()
        if id_ is None:
            return self.view.mostrar_erro("Selecione um movimento na lista.")
        if not self.view.confirmar("Excluir o movimento selecionado?"):
            return
        self.model.excluir(id_)
        self._carregar_lista()
        self.novo()
