import os
from datetime import datetime, timedelta, timezone
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.database import execute_one

load_dotenv()

SECRET_KEY     = os.getenv("JWT_SECRET", "chave_insegura_troque_isso")
EXPIRE_HOURS   = int(os.getenv("JWT_EXPIRE_HOURS", 24))
ALGORITHM      = "HS256"
COOKIE_NAME    = "stockflow_token"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha: str, hash_salvo: str) -> bool:
    return pwd_context.verify(senha, hash_salvo)


def criar_token(usuario_id: int, nivel: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(hours=EXPIRE_HOURS)
    payload = {
        "sub":   str(usuario_id),
        "nivel": nivel,
        "exp":   expire,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def get_usuario_atual(request: Request) -> dict:
    """
    Dependency: lê o cookie JWT, valida e retorna o usuário do banco.
    Redireciona para /login se o token for inválido ou ausente.
    """
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": "/login"},
        )
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": "/login"},
        )

    usuario_id = int(payload.get("sub", 0))
    usuario = execute_one(
        "SELECT id, nome, email, nivel, ativo FROM usuarios WHERE id = %s",
        (usuario_id,),
    )
    if not usuario or not usuario["ativo"]:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": "/login"},
        )
    return usuario


def requer_admin(usuario: dict = Depends(get_usuario_atual)) -> dict:
    """
    Dependency: verifica se o usuário é admin.
    Lança 403 caso contrário.
    """
    if usuario["nivel"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso restrito a administradores.",
        )
    return usuario
