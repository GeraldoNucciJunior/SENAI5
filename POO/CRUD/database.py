import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self,
                 host="localhost",
                 user="root",
                 password="senai@126",
                 db_name="crud_contatos"):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.conn = None
        self.cursor = None

        self.conectar()
        self.criar_banco()
        self.criar_tabela()

    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn and self.conn.is_connected():
                self.conn.close()
        except Error:
            pass

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Erro ao conectar: {e}")
            raise

    def criar_banco(self):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
            self.cursor.execute(f"USE {self.db_name}")
        except Error as e:
            print(f"Erro: {e}")

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
            self.conn.commit()
        except Error as e:
            print(f"Erro: {e}")

    def inserir(self, nome, telefone, email):
        sql = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, telefone, email))
        self.conn.commit()

    def atualizar(self, id, nome, telefone, email):
        sql = "UPDATE contatos SET nome=%s, telefone=%s, email=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, telefone, email, id))
        self.conn.commit()

    def excluir(self, id):
        sql = "DELETE FROM contatos WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM contatos")
        return self.cursor.fetchall()