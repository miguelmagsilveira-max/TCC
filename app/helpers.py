from app.database import execute_one


def contar_alertas() -> int:
    """Retorna a quantidade de notificações não lidas (badge de alertas)."""
    row = execute_one("SELECT COUNT(*) as c FROM notificacoes WHERE lida = 0")
    return row["c"] if row else 0
