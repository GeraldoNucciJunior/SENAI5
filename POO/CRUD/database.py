import os

import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self,
                 host="localhost",
                 user="root",
                 password=None,
                 db_name="crud_contatos"):
        self.host = host
        self.user = user
        self.password = password or os.getenv("DB_PASSWORD", "senai@126")
        self.db_name = db_name
        self.conn = None
        self.cursor = None

        self.conectar()
        self.criar_banco()
        self.criar_tabela()

    def __del__(self):
        self.fechar()

    def fechar(self):
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.conn and self.conn.is_connected():
                self.conn.close()
        except Error:
            pass

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                autocommit=True,
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Erro ao conectar: {e}")
            raise

    def criar_banco(self):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{self.db_name}`")
            self.conn.database = self.db_name
        except Error as e:
            print(f"Erro ao criar/selecionar o banco: {e}")
            raise

    def criar_tabela(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS contatos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(150) NOT NULL,
                    telefone VARCHAR(50) NOT NULL,
                    email VARCHAR(150) NOT NULL
                )
            """)
        except Error as e:
            print(f"Erro ao criar a tabela: {e}")
            raise

    def inserir(self, nome, telefone, email):
        sql = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, telefone, email))

    def atualizar(self, contato_id, nome, telefone, email):
        sql = "UPDATE contatos SET nome=%s, telefone=%s, email=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, telefone, email, contato_id))

    def excluir(self, contato_id):
        sql = "DELETE FROM contatos WHERE id=%s"
        self.cursor.execute(sql, (contato_id,))

    def listar(self):
        self.cursor.execute(
            "SELECT id, nome, telefone, email FROM contatos ORDER BY nome"
        )
        return self.cursor.fetchall()