"""Conexão e criação do banco SQLite."""
import sqlite3

DB_PATH = "app.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with get_connection() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS cliente (
                codigo INTEGER PRIMARY KEY,
                nome   TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS produto (
                codigo INTEGER PRIMARY KEY,
                nome   TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS movimento (
                id             INTEGER PRIMARY KEY AUTOINCREMENT,
                data           TEXT NOT NULL,
                codigo_cliente INTEGER NOT NULL REFERENCES cliente(codigo),
                codigo_produto INTEGER NOT NULL REFERENCES produto(codigo)
            );
            """
        )
