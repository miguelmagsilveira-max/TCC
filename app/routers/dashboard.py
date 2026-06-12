from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from app.auth import get_usuario_atual
from app.database import execute_one, execute_query
from app.helpers import contar_alertas
from app.templates_config import templates

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, usuario: dict = Depends(get_usuario_atual)):
    # Contadores principais
    total_ativos      = execute_one("SELECT COUNT(*) as c FROM ativos WHERE ativo = 1")["c"]
    em_uso            = execute_one("SELECT COUNT(*) as c FROM ativos WHERE situacao = 'Em uso' AND ativo = 1")["c"]
    em_estoque        = execute_one("SELECT COUNT(*) as c FROM ativos WHERE situacao = 'Em estoque' AND ativo = 1")["c"]
    em_manutencao     = execute_one("SELECT COUNT(*) as c FROM ativos WHERE situacao = 'Manutenção' AND ativo = 1")["c"]
    total_desativados = execute_one("SELECT COUNT(*) as c FROM ativos WHERE situacao = 'Desativado'")["c"]
    total_colaboradores = execute_one("SELECT COUNT(*) as c FROM colaboradores WHERE status = 'ativo'")["c"]

    valor_row = execute_one("SELECT COALESCE(SUM(preco), 0) as v FROM ativos WHERE ativo = 1")
    valor_total = float(valor_row["v"]) if valor_row else 0.0

    alertas_count = contar_alertas()

    # Últimas 8 movimentações
    ultimas_movimentacoes = execute_query("""
        SELECT
            a.nome        AS ativo_nome,
            a.codigo      AS ativo_codigo,
            h.acao,
            COALESCE(c.nome, '—') AS colaborador_nome,
            COALESCE(u.nome, '—') AS realizado_por_nome,
            h.realizado_em
        FROM historico_ativos h
        JOIN ativos a ON a.id = h.id_ativo
        LEFT JOIN colaboradores c ON c.id = h.id_colaborador_novo
        LEFT JOIN usuarios u ON u.id = h.realizado_por
        ORDER BY h.realizado_em DESC
        LIMIT 8
    """)

    # Ativos por tipo (para gráfico de barras)
    ativos_por_tipo = execute_query("""
        SELECT tipo, COUNT(*) AS total
        FROM ativos
        WHERE ativo = 1 AND tipo IS NOT NULL
        GROUP BY tipo
        ORDER BY total DESC
        LIMIT 8
    """)

    # Ativos por situação (para gráfico de rosca)
    ativos_por_situacao = execute_query("""
        SELECT situacao, COUNT(*) AS total
        FROM ativos
        WHERE ativo = 1
        GROUP BY situacao
    """)

    return templates.TemplateResponse("dashboard.html", {
        "request":               request,
        "usuario":               usuario,
        "total_ativos":          total_ativos,
        "em_uso":                em_uso,
        "em_estoque":            em_estoque,
        "em_manutencao":         em_manutencao,
        "total_desativados":     total_desativados,
        "total_colaboradores":   total_colaboradores,
        "valor_total":           valor_total,
        "alertas_count":         alertas_count,
        "ultimas_movimentacoes": ultimas_movimentacoes,
        "ativos_por_tipo":       ativos_por_tipo,
        "ativos_por_situacao":   ativos_por_situacao,
    })
