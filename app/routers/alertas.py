from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.auth import get_usuario_atual
from app.database import execute_query, execute_write
from app.templates_config import templates

router = APIRouter(prefix="/alertas", tags=["Alertas"])


@router.get("", response_class=HTMLResponse)
def pagina_alertas(request: Request, usuario: dict = Depends(get_usuario_atual)):
    alertas_estoque = execute_query(
        """SELECT t.nome AS tipo, t.estoque_minimo,
                  COUNT(a.id) AS em_estoque
           FROM tipos_ativo t
           LEFT JOIN ativos a ON a.tipo = t.nome AND a.situacao = 'Em estoque' AND a.ativo = 1
           GROUP BY t.id, t.nome, t.estoque_minimo
           HAVING COUNT(a.id) < t.estoque_minimo AND t.estoque_minimo > 0
           ORDER BY em_estoque ASC"""
    )

    garantias_vencendo = execute_query(
        """SELECT a.id, a.codigo, a.nome, a.tipo, a.data_garantia,
                  DATEDIFF(a.data_garantia, CURDATE()) AS dias_restantes,
                  COALESCE(c.nome, '—') AS colaborador_nome
           FROM ativos a
           LEFT JOIN colaboradores c ON c.id = a.id_colaborador
           WHERE a.ativo = 1
             AND a.data_garantia IS NOT NULL
             AND a.data_garantia BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
           ORDER BY a.data_garantia ASC"""
    )

    sem_colaborador = execute_query(
        """SELECT codigo, nome, tipo FROM ativos
           WHERE situacao = 'Em uso' AND id_colaborador IS NULL AND ativo = 1"""
    )

    notificacoes = execute_query(
        "SELECT * FROM notificacoes WHERE lida = 0 ORDER BY criada_em DESC"
    )

    alertas_count = len(notificacoes)

    return templates.TemplateResponse("alertas/index.html", {
        "request": request, "usuario": usuario,
        "alertas_estoque": alertas_estoque,
        "garantias_vencendo": garantias_vencendo,
        "sem_colaborador": sem_colaborador,
        "notificacoes": notificacoes,
        "alertas_count": alertas_count,
    })


@router.post("/marcar-lida/{notif_id}")
def marcar_lida(notif_id: int, usuario: dict = Depends(get_usuario_atual)):
    execute_write("UPDATE notificacoes SET lida=1 WHERE id=%s", (notif_id,))
    return RedirectResponse(url="/alertas", status_code=302)


@router.post("/marcar-todas-lidas")
def marcar_todas_lidas(usuario: dict = Depends(get_usuario_atual)):
    execute_write("UPDATE notificacoes SET lida=1")
    return RedirectResponse(url="/alertas", status_code=302)
