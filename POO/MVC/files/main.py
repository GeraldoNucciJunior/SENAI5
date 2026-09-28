"""
Ponto de entrada da aplicação.
Monta as camadas Model, View e Controller (padrão MVC) e inicia o programa.
"""

from model import PessoaModel
from view import PessoaView
from controller import PessoaController


def main():
    model = PessoaModel()
    view = PessoaView()
    controller = PessoaController(model, view)
    controller.executar()


if __name__ == "__main__":
    main()
