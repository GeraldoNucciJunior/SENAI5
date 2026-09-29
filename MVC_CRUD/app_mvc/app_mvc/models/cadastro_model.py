"""Model genérico para tabelas (codigo, nome): cliente e produto."""
import sqlite3
from database import get_connection


class CadastroModel:
    tabela = ""

    def listar(self):
        with get_connection() as conn:
            return conn.execute(
                f"SELECT codigo, nome FROM {self.tabela} ORDER BY codigo"
            ).fetchall()

    def inserir(self, codigo, nome):
        try:
            with get_connection() as conn:
                conn.execute(
                    f"INSERT INTO {self.tabela} (codigo, nome) VALUES (?, ?)",
                    (codigo, nome),
                )
        except sqlite3.IntegrityError:
            raise ValueError(f"Já existe um registro com o código {codigo}.")

    def atualizar(self, codigo, nome):
        with get_connection() as conn:
            conn.execute(
                f"UPDATE {self.tabela} SET nome = ? WHERE codigo = ?", (nome, codigo)
            )

    def excluir(self, codigo):
        try:
            with get_connection() as conn:
                conn.execute(f"DELETE FROM {self.tabela} WHERE codigo = ?", (codigo,))
        except sqlite3.IntegrityError:
            raise ValueError(
                "Não é possível excluir: o registro está em uso em algum movimento."
            )


class ClienteModel(CadastroModel):
    tabela = "cliente"


class ProdutoModel(CadastroModel):
    tabela = "produto"
