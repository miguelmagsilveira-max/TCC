import io
from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from app.auth import get_usuario_atual
from app.database import execute_query
from app.helpers import contar_alertas
from app.templates_config import templates

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])


def _calcular_curva_abc() -> list[dict]:
    tipos = execute_query(
        """SELECT tipo,
                  COUNT(*) AS qtd,
                  COALESCE(SUM(preco), 0) AS valor_total
           FROM ativos
           WHERE ativo = 1 AND tipo IS NOT NULL AND preco IS NOT NULL
           GROUP BY tipo
           ORDER BY valor_total DESC"""
    )
    if not tipos:
        return []

    total_geral = float(sum(float(t["valor_total"]) for t in tipos))
    if total_geral == 0:
        return []

    acumulado = 0.0
    resultado = []
    for t in tipos:
        acumulado += float(t["valor_total"])
        perc      = float(t["valor_total"]) / total_geral * 100
        perc_acum = acumulado / total_geral * 100

        if perc_acum <= 80:
            classe = "A"
        elif perc_acum <= 95:
            classe = "B"
        else:
            classe = "C"

        resultado.append({
            "tipo":           t["tipo"],
            "qtd":            t["qtd"],
            "valor_total":    float(t["valor_total"]),
            "percentual":     round(perc, 2),
            "perc_acumulado": round(perc_acum, 2),
            "classe":         classe,
        })
    return resultado


@router.get("", response_class=HTMLResponse)
def pagina_relatorios(
    request: Request,
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
    if tipo:
        sql += " AND a.tipo = %s"
        params.append(tipo)
    if situacao:
        sql += " AND a.situacao = %s"
        params.append(situacao)
    sql += " ORDER BY a.tipo, a.codigo"

    lista_ativos = execute_query(sql, tuple(params))
    curva_abc    = _calcular_curva_abc()
    tipos        = execute_query("SELECT nome FROM tipos_ativo ORDER BY nome")

    resumo_por_tipo = execute_query(
        """SELECT tipo, COUNT(*) AS qtd, COALESCE(SUM(preco),0) AS valor_total
           FROM ativos WHERE ativo=1 AND tipo IS NOT NULL
           GROUP BY tipo ORDER BY qtd DESC"""
    )
    resumo_por_situacao = execute_query(
        "SELECT situacao, COUNT(*) AS qtd FROM ativos WHERE ativo=1 GROUP BY situacao"
    )

    return templates.TemplateResponse("relatorios/index.html", {
        "request": request, "usuario": usuario,
        "lista_ativos": lista_ativos,
        "curva_abc": curva_abc,
        "tipos": tipos,
        "tipo_sel": tipo, "situacao_sel": situacao,
        "resumo_por_tipo": resumo_por_tipo,
        "resumo_por_situacao": resumo_por_situacao,
        "alertas_count": contar_alertas(),
    })


@router.get("/exportar-pdf")
def exportar_pdf(usuario: dict = Depends(get_usuario_atual)):
    ativos = execute_query(
        """SELECT a.codigo, a.nome, a.tipo, a.marca, a.modelo,
                  a.situacao, COALESCE(c.nome, '—') AS colaborador, a.preco
           FROM ativos a
           LEFT JOIN colaboradores c ON c.id = a.id_colaborador
           WHERE a.ativo = 1
           ORDER BY a.tipo, a.codigo"""
    )

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4),
                            leftMargin=1.5*cm, rightMargin=1.5*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Stock Flow — Relatório de Ativos", styles["Title"]))
    elements.append(Paragraph(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", styles["Normal"]))
    elements.append(Spacer(1, 0.5*cm))

    header = ["Código", "Nome", "Tipo", "Marca/Modelo", "Situação", "Colaborador", "Preço (R$)"]
    data = [header]
    for a in ativos:
        data.append([
            a["codigo"],
            a["nome"][:30],
            a["tipo"] or "—",
            f"{a['marca'] or ''} {a['modelo'] or ''}".strip() or "—",
            a["situacao"],
            a["colaborador"],
            f"R$ {a['preco']:,.2f}" if a["preco"] else "—",
        ])

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0),  colors.HexColor("#1e3a5f")),
        ("TEXTCOLOR",      (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",       (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",       (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f8")]),
        ("GRID",           (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING",        (0, 0), (-1, -1), 4),
    ]))
    elements.append(table)

    doc.build(elements)
    buffer.seek(0)
    filename = f"stockflow_ativos_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
