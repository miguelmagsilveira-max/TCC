from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.auth import get_usuario_atual, requer_admin
from app.database import execute_one, execute_query, execute_write
from app.helpers import contar_alertas
from app.templates_config import templates

router = APIRouter(prefix="/colaboradores", tags=["Colaboradores"])


@router.get("", response_class=HTMLResponse)
def listar(request: Request, busca: str = "", usuario: dict = Depends(get_usuario_atual)):
    if busca:
        colaboradores = execute_query(
            "SELECT * FROM colaboradores WHERE nome LIKE %s OR email LIKE %s OR departamento LIKE %s ORDER BY nome",
            (f"%{busca}%", f"%{busca}%", f"%{busca}%"),
        )
    else:
        colaboradores = execute_query("SELECT * FROM colaboradores ORDER BY nome")

    return templates.TemplateResponse("colaboradores/index.html", {
        "request": request, "usuario": usuario,
        "colaboradores": colaboradores, "busca": busca,
        "alertas_count": contar_alertas(),
    })


@router.get("/novo", response_class=HTMLResponse)
def form_novo(request: Request, admin: dict = Depends(requer_admin)):
    return templates.TemplateResponse("colaboradores/form.html", {
        "request": request, "usuario": admin, "colaborador": None,
        "alertas_count": contar_alertas(),
    })


@router.post("/novo")
def criar(
    request: Request,
    nome: str = Form(...),
    email: str = Form(""),
    cargo: str = Form(""),
    departamento: str = Form(""),
    admin: dict = Depends(requer_admin),
):
    execute_write(
        "INSERT INTO colaboradores (nome, email, cargo, departamento) VALUES (%s, %s, %s, %s)",
        (nome, email or None, cargo or None, departamento or None),
    )
    return RedirectResponse(url="/colaboradores", status_code=302)


@router.get("/{colaborador_id}", response_class=HTMLResponse)
def detalhe(request: Request, colaborador_id: int, usuario: dict = Depends(get_usuario_atual)):
    colaborador = execute_one("SELECT * FROM colaboradores WHERE id = %s", (colaborador_id,))
    if not colaborador:
        return RedirectResponse(url="/colaboradores", status_code=302)

    ativos_vinculados = execute_query(
        "SELECT * FROM ativos WHERE id_colaborador = %s AND ativo = 1 ORDER BY tipo, nome",
        (colaborador_id,),
    )
    return templates.TemplateResponse("colaboradores/detalhe.html", {
        "request": request, "usuario": usuario,
        "colaborador": colaborador, "ativos": ativos_vinculados,
        "alertas_count": contar_alertas(),
    })


@router.get("/{colaborador_id}/editar", response_class=HTMLResponse)
def form_editar(request: Request, colaborador_id: int, admin: dict = Depends(requer_admin)):
    colaborador = execute_one("SELECT * FROM colaboradores WHERE id = %s", (colaborador_id,))
    if not colaborador:
        return RedirectResponse(url="/colaboradores", status_code=302)
    return templates.TemplateResponse("colaboradores/form.html", {
        "request": request, "usuario": admin, "colaborador": colaborador,
        "alertas_count": contar_alertas(),
    })


@router.post("/{colaborador_id}/editar")
def salvar_edicao(
    colaborador_id: int,
    nome: str = Form(...),
    email: str = Form(""),
    cargo: str = Form(""),
    departamento: str = Form(""),
    admin: dict = Depends(requer_admin),
):
    execute_write(
        "UPDATE colaboradores SET nome=%s, email=%s, cargo=%s, departamento=%s WHERE id=%s",
        (nome, email or None, cargo or None, departamento or None, colaborador_id),
    )
    return RedirectResponse(url=f"/colaboradores/{colaborador_id}", status_code=302)


@router.post("/{colaborador_id}/desligar")
def desligar(colaborador_id: int, admin: dict = Depends(requer_admin)):
    execute_write(
        "UPDATE colaboradores SET status = 'desligado' WHERE id = %s",
        (colaborador_id,),
    )
    return RedirectResponse(url=f"/colaboradores/{colaborador_id}", status_code=302)


@router.post("/{colaborador_id}/reativar")
def reativar(colaborador_id: int, admin: dict = Depends(requer_admin)):
    execute_write(
        "UPDATE colaboradores SET status = 'ativo' WHERE id = %s",
        (colaborador_id,),
    )
    return RedirectResponse(url=f"/colaboradores/{colaborador_id}", status_code=302)
