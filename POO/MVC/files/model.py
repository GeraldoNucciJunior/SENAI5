"""
Model
-----
Responsável por toda a interação com o banco de dados SQLite:
criação da tabela, inserção, listagem e representação dos dados.
"""

import sqlite3
from dataclasses import dataclass


DB_NAME = "cadastro.db"


@dataclass
class Pessoa:
    """Representa os dados de uma pessoa a serem persistidos."""
    nome: str
    data_nascimento: str  # formato: DD/MM/AAAA
    salario: float
    id: int = None


class PessoaModel:
    """Camada de acesso a dados (Model) usando SQLite."""

    def __init__(self, db_name: str = DB_NAME):
        self.db_name = db_name
        self._criar_tabela()

    def _conectar(self):
        return sqlite3.connect(self.db_name)

    def _criar_tabela(self):
        with self._conectar() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data_nascimento TEXT NOT NULL,
                    salario REAL NOT NULL
                )
            """)
            conn.commit()

    def salvar(self, pessoa: Pessoa) -> int:
        """Insere uma nova pessoa no banco e retorna o id gerado."""
        with self._conectar() as conn:
            cursor = conn.execute(
                "INSERT INTO pessoas (nome, data_nascimento, salario) VALUES (?, ?, ?)",
                (pessoa.nome, pessoa.data_nascimento, pessoa.salario),
            )
            conn.commit()
            return cursor.lastrowid

    def listar_todos(self) -> list[Pessoa]:
        """Retorna todas as pessoas cadastradas."""
        with self._conectar() as conn:
            cursor = conn.execute(
                "SELECT id, nome, data_nascimento, salario FROM pessoas ORDER BY id"
            )
            return [
                Pessoa(id=row[0], nome=row[1], data_nascimento=row[2], salario=row[3])
                for row in cursor.fetchall()
            ]
