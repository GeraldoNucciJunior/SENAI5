"""
View
----
Responsável por toda a interação com o usuário: exibir menus,
capturar entradas e mostrar resultados no terminal.
"""

from model import Pessoa


class PessoaView:
    """Camada de apresentação (View)."""

    def exibir_menu(self) -> str:
        print("\n=== Cadastro de Pessoas ===")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas cadastradas")
        print("0 - Sair")
        return input("Escolha uma opção: ").strip()

    def capturar_dados_pessoa(self) -> dict:
        nome = input("Nome: ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        salario_str = input("Salário: ").strip().replace(",", ".")
        return {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "salario": salario_str,
        }

    def exibir_mensagem(self, mensagem: str):
        print(mensagem)

    def exibir_erro(self, mensagem: str):
        print(f"[ERRO] {mensagem}")

    def exibir_pessoas(self, pessoas: list[Pessoa]):
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        print("\n--- Pessoas cadastradas ---")
        for p in pessoas:
            print(
                f"ID: {p.id} | Nome: {p.nome} | "
                f"Nascimento: {p.data_nascimento} | Salário: R$ {p.salario:,.2f}"
            )
