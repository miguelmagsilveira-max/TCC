from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.auth import get_usuario_atual, requer_admin
from app.database import execute_one, execute_query, execute_write
from app.templates_config import templates

router = APIRouter(prefix="/ativos", tags=["Ativos"])


def _alertas_count() -> int:
    row = execute_one("SELECT COUNT(*) as c FROM notificacoes WHERE lida = 0")
    return row["c"] if row else 0


def _proximo_codigo() -> str:
    row = execute_one(
        "SELECT MAX(CAST(SUBSTRING(codigo, 5) AS UNSIGNED)) AS ultimo FROM ativos WHERE codigo LIKE 'AST-%'"
    )
    proximo = (row["ultimo"] or 0) + 1
    return f"AST-{proximo:03d}"


def _registrar_historico(id_ativo: int, acao: str, id_anterior=None, id_novo=None, detalhes=None, realizado_por=None):
    execute_write(
        """INSERT INTO historico_ativos
           (id_ativo, acao, id_colaborador_anterior, id_colaborador_novo, detalhes, realizado_por)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (id_ativo, acao, id_anterior, id_novo, detalhes, realizado_por),
    )


@router.get("", response_class=HTMLResponse)
def listar(
    request: Request,
    busca: str = "",
    tipo: str = "",
    situacao: str = "",
    usuario: dict = Depends(get_usuario_atual),
):
    sql = """
        SELECT a.*, c.nome AS colaborador_nome
        FROM ativos a
        LEFT JOIN colaboradores c ON c.id = a.id_colaborador
        WHERE a.ativo = 1
    """
    params = []
    if busca:
        sql += " AND (a.nome LIKE %s OR a.codigo LIKE %s OR a.marca LIKE %s OR a.modelo LIKE %s)"
        params += [f"%{busca}%"] * 4
    if tipo:
        sql += " AND a.tipo = %s"
        params.append(tipo)
    if situacao:
        sql += " AND a.situacao = %s"
        params.append(situacao)
    sql += " ORDER BY a.codigo"

    ativos = execute_query(sql, tuple(params))
    tipos  = execute_query("SELECT nome FROM tipos_ativo ORDER BY nome")

    return templates.TemplateResponse("ativos/index.html", {
        "request": request, "usuario": usuario,
        "ativos": ativos, "tipos": tipos,
        "busca": busca, "tipo_sel": tipo, "situacao_sel": situacao,
        "alertas_count": _alertas_count(),
    })


@router.get("/novo", response_class=HTMLResponse)
def form_novo(request: Request, admin: dict = Depends(requer_admin)):
    tipos         = execute_query("SELECT nome FROM tipos_ativo ORDER BY nome")
    colaboradores = execute_query("SELECT id, nome FROM colaboradores WHERE status='ativo' ORDER BY nome")
    return templates.TemplateResponse("ativos/form.html", {
        "request": request, "usuario": admin,
        "ativo": None, "tipos": tipos, "colaboradores": colaboradores,
        "alertas_count": _alertas_count(),
    })


@router.post("/novo")
def criar(
    request: Request,
    nome: str = Form(...),
    tipo: str = Form(""),
    marca: str = Form(""),
    modelo: str = Form(""),
    numero_serie: str = Form(""),
    tipo_aquisicao: str = Form(""),
    preco: str = Form(""),
    data_aquisicao: str = Form(""),
    data_garantia: str = Form(""),
    fornecedor: str = Form(""),
    numero_nota_fiscal: str = Form(""),
    localizacao: str = Form(""),
    admin: dict = Depends(requer_admin),
):
    codigo    = _proximo_codigo()
    preco_val = float(preco) if preco else None
    id_ativo  = execute_write(
        """INSERT INTO ativos
           (codigo, nome, tipo, marca, modelo, numero_serie, tipo_aquisicao,
            preco, data_aquisicao, data_garantia, fornecedor, numero_nota_fiscal,
            localizacao, criado_por)
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (
            codigo, nome, tipo or None, marca or None, modelo or None,
            numero_serie or None, tipo_aquisicao or None,
            preco_val,
            data_aquisicao or None, data_garantia or None,
            fornecedor or None, numero_nota_fiscal or None,
            localizacao or None, admin["id"],
        ),
    )
    _registrar_historico(id_ativo, "Cadastro", detalhes="Ativo cadastrado no sistema", realizado_por=admin["id"])
    return RedirectResponse(url=f"/ativos/{id_ativo}", status_code=302)


@router.get("/{ativo_id}", response_class=HTMLResponse)
def detalhe(request: Request, ativo_id: int, usuario: dict = Depends(get_usuario_atual)):
    ativo = execute_one(
        """SELECT a.*, c.nome AS colaborador_nome
           FROM ativos a
           LEFT JOIN colaboradores c ON c.id = a.id_colaborador
           WHERE a.id = %s""",
        (ativo_id,),
    )
    if not ativo:
        return RedirectResponse(url="/ativos", status_code=302)

    historico = execute_query(
        """SELECT h.*,
                  cant.nome AS colaborador_anterior_nome,
                  cnov.nome AS colaborador_novo_nome,
                  u.nome    AS realizado_por_nome
           FROM historico_ativos h
           LEFT JOIN colaboradores cant ON cant.id = h.id_colaborador_anterior
           LEFT JOIN colaboradores cnov ON cnov.id = h.id_colaborador_novo
           LEFT JOIN usuarios u ON u.id = h.realizado_por
           WHERE h.id_ativo = %s
           ORDER BY h.realizado_em DESC""",
        (ativo_id,),
    )
    colaboradores = execute_query("SELECT id, nome FROM colaboradores WHERE status='ativo' ORDER BY nome")

    return templates.TemplateResponse("ativos/detalhe.html", {
        "request": request, "usuario": usuario,
        "ativo": ativo, "historico": historico, "colaboradores": colaboradores,
        "alertas_count": _alertas_count(),
    })


@router.get("/{ativo_id}/editar", response_class=HTMLResponse)
def form_editar(request: Request, ativo_id: int, admin: dict = Depends(requer_admin)):
    ativo = execute_one("SELECT * FROM ativos WHERE id = %s", (ativo_id,))
    if not ativo:
        return RedirectResponse(url="/ativos", status_code=302)
    tipos         = execute_query("SELECT nome FROM tipos_ativo ORDER BY nome")
    colaboradores = execute_query("SELECT id, nome FROM colaboradores WHERE status='ativo' ORDER BY nome")
    return templates.TemplateResponse("ativos/form.html", {
        "request": request, "usuario": admin,
        "ativo": ativo, "tipos": tipos, "colaboradores": colaboradores,
        "alertas_count": _alertas_count(),
    })


@router.post("/{ativo_id}/editar")
def salvar_edicao(
    ativo_id: int,
    nome: str = Form(...),
    tipo: str = Form(""),
    marca: str = Form(""),
    modelo: str = Form(""),
    numero_serie: str = Form(""),
    tipo_aquisicao: str = Form(""),
    preco: str = Form(""),
    data_aquisicao: str = Form(""),
    data_garantia: str = Form(""),
    fornecedor: str = Form(""),
    numero_nota_fiscal: str = Form(""),
    localizacao: str = Form(""),
    admin: dict = Depends(requer_admin),
):
    preco_val = float(preco) if preco else None
    execute_write(
        """UPDATE ativos SET nome=%s, tipo=%s, marca=%s, modelo=%s, numero_serie=%s,
           tipo_aquisicao=%s, preco=%s, data_aquisicao=%s, data_garantia=%s,
           fornecedor=%s, numero_nota_fiscal=%s, localizacao=%s
           WHERE id=%s""",
        (
            nome, tipo or None, marca or None, modelo or None, numero_serie or None,
            tipo_aquisicao or None, preco_val,
            data_aquisicao or None, data_garantia or None,
            fornecedor or None, numero_nota_fiscal or None, localizacao or None,
            ativo_id,
        ),
    )
    _registrar_historico(ativo_id, "Edição", detalhes="Dados do ativo atualizados", realizado_por=admin["id"])
    return RedirectResponse(url=f"/ativos/{ativo_id}", status_code=302)


@router.post("/{ativo_id}/vincular")
def vincular(
    ativo_id: int,
    colaborador_id: int = Form(...),
    admin: dict = Depends(requer_admin),
):
    ativo = execute_one("SELECT id_colaborador FROM ativos WHERE id = %s", (ativo_id,))
    id_anterior = ativo["id_colaborador"] if ativo else None

    execute_write(
        "UPDATE ativos SET situacao='Em uso', id_colaborador=%s, data_vinculacao=NOW() WHERE id=%s",
        (colaborador_id, ativo_id),
    )
    colob = execute_one("SELECT nome FROM colaboradores WHERE id = %s", (colaborador_id,))
    _registrar_historico(
        ativo_id, "Vinculação",
        id_anterior=id_anterior, id_novo=colaborador_id,
        detalhes=f"Vinculado a {colob['nome'] if colob else colaborador_id}",
        realizado_por=admin["id"],
    )
    return RedirectResponse(url=f"/ativos/{ativo_id}", status_code=302)


@router.post("/{ativo_id}/desvincular")
def desvincular(ativo_id: int, admin: dict = Depends(requer_admin)):
    ativo = execute_one("SELECT id_colaborador FROM ativos WHERE id = %s", (ativo_id,))
    id_anterior = ativo["id_colaborador"] if ativo else None

    execute_write(
        "UPDATE ativos SET situacao='Em estoque', id_colaborador=NULL, data_vinculacao=NULL WHERE id=%s",
        (ativo_id,),
    )
    _registrar_historico(
        ativo_id, "Desvinculação",
        id_anterior=id_anterior,
        detalhes="Ativo devolvido ao estoque",
        realizado_por=admin["id"],
    )
    return RedirectResponse(url=f"/ativos/{ativo_id}", status_code=302)


@router.post("/{ativo_id}/manutencao")
def enviar_manutencao(
    ativo_id: int,
    detalhes: str = Form(""),
    admin: dict = Depends(requer_admin),
):
    execute_write("UPDATE ativos SET situacao='Manutenção' WHERE id=%s", (ativo_id,))
    _registrar_historico(
        ativo_id, "Manutenção",
        detalhes=detalhes or "Enviado para manutenção",
        realizado_por=admin["id"],
    )
    return RedirectResponse(url=f"/ativos/{ativo_id}", status_code=302)


@router.post("/{ativo_id}/retornar")
def retornar_manutencao(ativo_id: int, admin: dict = Depends(requer_admin)):
    execute_write("UPDATE ativos SET situacao='Em estoque' WHERE id=%s", (ativo_id,))
    _registrar_historico(
        ativo_id, "Retorno de Manutenção",
        detalhes="Ativo retornou da manutenção para o estoque",
        realizado_por=admin["id"],
    )
    return RedirectResponse(url=f"/ativos/{ativo_id}", status_code=302)


@router.post("/{ativo_id}/desativar")
def desativar(ativo_id: int, admin: dict = Depends(requer_admin)):
    execute_write(
        "UPDATE ativos SET ativo=0, situacao='Desativado', id_colaborador=NULL WHERE id=%s",
        (ativo_id,),
    )
    _registrar_historico(
        ativo_id, "Desativação",
        detalhes="Ativo desativado e removido do inventário ativo",
        realizado_por=admin["id"],
    )
    return RedirectResponse(url="/ativos", status_code=302)
