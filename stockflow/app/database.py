import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "port":     int(os.getenv("DB_PORT", 3306)),
    "database": os.getenv("DB_NAME", "stockflow"),
    "user":     os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "charset":  "utf8mb4",
}


def get_connection():
    """Retorna uma nova conexão com o banco MySQL."""
    return mysql.connector.connect(**DB_CONFIG)


def execute_query(sql: str, params: tuple = None) -> list[dict]:
    """
    Executa um SELECT e retorna lista de dicionários.
    Cada linha é um dict com os nomes das colunas como chaves.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        return cursor.fetchall()
    except Error as e:
        print(f"[DB ERROR] execute_query: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()


def execute_one(sql: str, params: tuple = None) -> dict | None:
    """
    Executa um SELECT e retorna apenas a primeira linha (dict) ou None.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        return cursor.fetchone()
    except Error as e:
        print(f"[DB ERROR] execute_one: {e}")
        return None
    finally:
        if conn and conn.is_connected():
            conn.close()


def execute_write(sql: str, params: tuple = None) -> int:
    """
    Executa INSERT, UPDATE ou DELETE.
    Retorna lastrowid para INSERT, ou rows affected para UPDATE/DELETE.
    Retorna -1 em caso de erro.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        conn.commit()
        return cursor.lastrowid if cursor.lastrowid else cursor.rowcount
    except Error as e:
        print(f"[DB ERROR] execute_write: {e}")
        if conn:
            conn.rollback()
        return -1
    finally:
        if conn and conn.is_connected():
            conn.close()
