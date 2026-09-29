"""Controller genérico para Cliente e Produto."""


class CadastroController:
    def __init__(self, model, view, nome_entidade):
        self.model = model
        self.view = view
        self.nome_entidade = nome_entidade
        self.editando = False
        view.controller = self
        self.atualizar_lista()

    def atualizar_lista(self):
        self.view.carregar_lista(self.model.listar())

    def novo(self):
        self.editando = False
        self.view.limpar_selecao()
        self.view.bloquear_codigo(False)
        self.view.set_dados("", "")

    def selecionar(self):
        item = self.view.item_selecionado()
        if item:
            self.editando = True
            self.view.bloquear_codigo(False)
            self.view.set_dados(item[0], item[1])
            self.view.bloquear_codigo(True)

    def salvar(self):
        codigo, nome = self.view.get_dados()
        if not codigo.isdigit():
            return self.view.mostrar_erro("O código deve ser um número inteiro.")
        if not nome:
            return self.view.mostrar_erro("Informe o nome.")
        try:
            if self.editando:
                self.model.atualizar(int(codigo), nome)
            else:
                self.model.inserir(int(codigo), nome)
        except ValueError as e:
            return self.view.mostrar_erro(str(e))
        self.atualizar_lista()
        self.novo()

    def excluir(self):
        item = self.view.item_selecionado()
        if not item:
            return self.view.mostrar_erro(f"Selecione um {self.nome_entidade} na lista.")
        if not self.view.confirmar(f"Excluir {self.nome_entidade} {item[0]} - {item[1]}?"):
            return
        try:
            self.model.excluir(int(item[0]))
        except ValueError as e:
            return self.view.mostrar_erro(str(e))
        self.atualizar_lista()
        self.novo()
