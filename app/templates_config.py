from datetime import date, datetime
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")


def _format_date(value):
    if value is None:
        return "—"
    if isinstance(value, (datetime, date)):
        return value.strftime("%d/%m/%Y")
    return str(value)


def _format_datahora(value):
    if value is None:
        return "—"
    if isinstance(value, datetime):
        return value.strftime("%d/%m/%Y %H:%M")
    if isinstance(value, date):
        return value.strftime("%d/%m/%Y")
    return str(value)


templates.env.filters["data"] = _format_date
templates.env.filters["datahora"] = _format_datahora
