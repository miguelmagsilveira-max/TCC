from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.auth import COOKIE_NAME, criar_token, get_usuario_atual, verificar_senha
from app.database import execute_one, execute_write
from app.templates_config import templates

router = APIRouter(tags=["Autenticação"])


@router.get("/login", response_class=HTMLResponse)
def pagina_login(request: Request):
    # Se já estiver logado, vai para o dashboard
    token = request.cookies.get(COOKIE_NAME)
    if token:
        from app.auth import verificar_token
        if verificar_token(token):
            return RedirectResponse(url="/dashboard", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def fazer_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
):
    usuario = execute_one(
        "SELECT id, nome, email, senha_hash, nivel, ativo FROM usuarios WHERE email = %s",
        (email,),
    )
    if not usuario or not usuario["ativo"] or not verificar_senha(senha, usuario["senha_hash"]):
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "erro": "E-mail ou senha incorretos."},
            status_code=401,
        )

    # Atualiza último acesso
    execute_write(
        "UPDATE usuarios SET ultimo_acesso = NOW() WHERE id = %s",
        (usuario["id"],),
    )

    token = criar_token(usuario["id"], usuario["nivel"])
    response = RedirectResponse(url="/dashboard", status_code=302)
    response.set_cookie(
        key=COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=86400,
        samesite="lax",
    )
    return response


@router.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie(COOKIE_NAME)
    return response
