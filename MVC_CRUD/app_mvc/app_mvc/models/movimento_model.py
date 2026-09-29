"""Model de movimento (data, codigo_cliente, codigo_produto)."""
import sqlite3
from database import get_connection


class MovimentoModel:
    def listar(self):
        with get_connection() as conn:
            return conn.execute(
                """
                SELECT m.id, m.data,
                       m.codigo_cliente, c.nome AS nome_cliente,
                       m.codigo_produto, p.nome AS nome_produto
                FROM movimento m
                JOIN cliente c ON c.codigo = m.codigo_cliente
                JOIN produto p ON p.codigo = m.codigo_produto
                ORDER BY m.data DESC, m.id DESC
                """
            ).fetchall()

    def inserir(self, data, codigo_cliente, codigo_produto):
        self._executar(
            "INSERT INTO movimento (data, codigo_cliente, codigo_produto) VALUES (?, ?, ?)",
            (data, codigo_cliente, codigo_produto),
        )

    def atualizar(self, id_, data, codigo_cliente, codigo_produto):
        self._executar(
            "UPDATE movimento SET data = ?, codigo_cliente = ?, codigo_produto = ? WHERE id = ?",
            (data, codigo_cliente, codigo_produto, id_),
        )

    def excluir(self, id_):
        self._executar("DELETE FROM movimento WHERE id = ?", (id_,))

    @staticmethod
    def _executar(sql, params):
        try:
            with get_connection() as conn:
                conn.execute(sql, params)
        except sqlite3.IntegrityError:
            raise ValueError("Cliente ou produto inexistente.")
