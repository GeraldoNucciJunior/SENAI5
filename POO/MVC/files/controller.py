"""
Controller
----------
Faz a ponte entre a View (entrada/saída) e o Model (dados),
aplicando as validações necessárias.
"""

from datetime import datetime

from model import Pessoa, PessoaModel
from view import PessoaView


class PessoaController:
    """Camada de controle (Controller)."""

    def __init__(self, model: PessoaModel, view: PessoaView):
        self.model = model
        self.view = view

    def executar(self):
        """Loop principal da aplicação."""
        while True:
            opcao = self.view.exibir_menu()

            if opcao == "1":
                self._cadastrar_pessoa()
            elif opcao == "2":
                self._listar_pessoas()
            elif opcao == "0":
                self.view.exibir_mensagem("Encerrando...")
                break
            else:
                self.view.exibir_erro("Opção inválida.")

    def _cadastrar_pessoa(self):
        dados = self.view.capturar_dados_pessoa()

        if not dados["nome"]:
            self.view.exibir_erro("O nome não pode estar vazio.")
            return

        if not self._validar_data(dados["data_nascimento"]):
            self.view.exibir_erro("Data de nascimento inválida. Use o formato DD/MM/AAAA.")
            return

        try:
            salario = float(dados["salario"])
            if salario < 0:
                raise ValueError
        except ValueError:
            self.view.exibir_erro("Salário inválido.")
            return

        pessoa = Pessoa(
            nome=dados["nome"],
            data_nascimento=dados["data_nascimento"],
            salario=salario,
        )
        id_gerado = self.model.salvar(pessoa)
        self.view.exibir_mensagem(f"Pessoa cadastrada com sucesso! (ID {id_gerado})")

    def _listar_pessoas(self):
        pessoas = self.model.listar_todos()
        self.view.exibir_pessoas(pessoas)

    @staticmethod
    def _validar_data(data_str: str) -> bool:
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
