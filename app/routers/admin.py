from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel

from app.auth import get_usuario_atual, hash_senha, requer_admin
from app.database import execute_one, execute_query, execute_write
from app.helpers import contar_alertas
from app.templates_config import templates

router = APIRouter(prefix="/admin", tags=["Administração"])
api_router = APIRouter(prefix="/api", tags=["API"])


class OpcaoCreate(BaseModel):
    valor: str


# ── Usuários ──────────────────────────────────────────────────────────────────

@router.get("/usuarios", response_class=HTMLResponse)
def listar_usuarios(request: Request, admin: dict = Depends(requer_admin)):
    usuarios = execute_query(
        "SELECT id, nome, email, nivel, ativo, criado_em, ultimo_acesso FROM usuarios ORDER BY nome"
    )
    return templates.TemplateResponse("admin/usuarios.html", {
        "request": request, "usuario": admin, "usuarios": usuarios,
        "alertas_count": contar_alertas(),
    })


@router.get("/usuarios/novo", response_class=HTMLResponse)
def form_novo_usuario(request: Request, admin: dict = Depends(requer_admin)):
    return templates.TemplateResponse("admin/usuario_form.html", {
        "request": request, "usuario": admin, "editando": None,
        "alertas_count": contar_alertas(),
    })


@router.post("/usuarios/novo")
def criar_usuario(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    nivel: str = Form("operador"),
    admin: dict = Depends(requer_admin),
):
    existente = execute_one("SELECT id FROM usuarios WHERE email=%s", (email,))
    if existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    execute_write(
        "INSERT INTO usuarios (nome, email, senha_hash, nivel) VALUES (%s,%s,%s,%s)",
        (nome, email, hash_senha(senha), nivel),
    )
    return RedirectResponse(url="/admin/usuarios", status_code=302)


@router.get("/usuarios/{user_id}/editar", response_class=HTMLResponse)
def form_editar_usuario(request: Request, user_id: int, admin: dict = Depends(requer_admin)):
    editando = execute_one(
        "SELECT id, nome, email, nivel, ativo FROM usuarios WHERE id=%s", (user_id,)
    )
    if not editando:
        return RedirectResponse(url="/admin/usuarios", status_code=302)
    return templates.TemplateResponse("admin/usuario_form.html", {
        "request": request, "usuario": admin, "editando": editando,
        "alertas_count": contar_alertas(),
    })


@router.post("/usuarios/{user_id}/editar")
def salvar_usuario(
    user_id: int,
    nome: str = Form(...),
    email: str = Form(...),
    nivel: str = Form("operador"),
    admin: dict = Depends(requer_admin),
):
    execute_write(
        "UPDATE usuarios SET nome=%s, email=%s, nivel=%s WHERE id=%s",
        (nome, email, nivel, user_id),
    )
    return RedirectResponse(url="/admin/usuarios", status_code=302)


@router.post("/usuarios/{user_id}/toggle")
def toggle_usuario(user_id: int, admin: dict = Depends(requer_admin)):
    execute_write(
        "UPDATE usuarios SET ativo = NOT ativo WHERE id=%s AND id != %s",
        (user_id, admin["id"]),
    )
    return RedirectResponse(url="/admin/usuarios", status_code=302)


@router.post("/usuarios/{user_id}/senha")
def redefinir_senha(
    user_id: int,
    nova_senha: str = Form(...),
    admin: dict = Depends(requer_admin),
):
    execute_write(
        "UPDATE usuarios SET senha_hash=%s WHERE id=%s",
        (hash_senha(nova_senha), user_id),
    )
    return RedirectResponse(url="/admin/usuarios", status_code=302)


# ── Opções SmartSelect ────────────────────────────────────────────────────────

@api_router.get("/opcoes/{contexto}")
def get_opcoes(contexto: str, usuario: dict = Depends(get_usuario_atual)):
    rows = execute_query(
        "SELECT id, valor FROM opcoes_select WHERE contexto=%s ORDER BY valor",
        (contexto,),
    )
    return JSONResponse([{"id": r["id"], "valor": r["valor"]} for r in rows])


@api_router.post("/opcoes/{contexto}")
def add_opcao(contexto: str, body: OpcaoCreate, usuario: dict = Depends(get_usuario_atual)):
    valor = body.valor.strip()
    if not valor:
        raise HTTPException(status_code=400, detail="Valor não pode ser vazio.")
    existing = execute_one(
        "SELECT id FROM opcoes_select WHERE contexto=%s AND valor=%s", (contexto, valor)
    )
    if existing:
        return JSONResponse({"id": existing["id"], "valor": valor})
    new_id = execute_write(
        "INSERT INTO opcoes_select (contexto, valor) VALUES (%s, %s)", (contexto, valor)
    )
    return JSONResponse({"id": new_id, "valor": valor}, status_code=201)


@api_router.delete("/opcoes/{contexto}/{opcao_id}")
def del_opcao(contexto: str, opcao_id: int, admin: dict = Depends(requer_admin)):
    execute_write(
        "DELETE FROM opcoes_select WHERE id=%s AND contexto=%s", (opcao_id, contexto)
    )
    return JSONResponse({"ok": True})
