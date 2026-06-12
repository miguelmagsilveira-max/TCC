from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routers import (
    auth_routes,
    dashboard,
    colaboradores,
    ativos,
    relatorios,
    alertas,
    admin,
)
from app.routers.admin import api_router

app = FastAPI(
    title="Stock Flow",
    description="TCC — Gestão de Ativos de TI com rastreabilidade completa.",
    version="1.0.0",
)

# Arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Routers
app.include_router(auth_routes.router)
app.include_router(dashboard.router)
app.include_router(colaboradores.router)
app.include_router(ativos.router)
app.include_router(relatorios.router)
app.include_router(alertas.router)
app.include_router(admin.router)
app.include_router(api_router)


@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/dashboard")


@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}


@app.exception_handler(403)
async def handler_403(request: Request, exc):
    from app.templates_config import templates
    return templates.TemplateResponse(
        "errors/403.html", {"request": request}, status_code=403
    )


@app.exception_handler(404)
async def handler_404(request: Request, exc):
    from app.templates_config import templates
    return templates.TemplateResponse(
        "errors/404.html", {"request": request}, status_code=404
    )
