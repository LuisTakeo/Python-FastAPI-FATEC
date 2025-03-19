from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")
def primeira_pagina(request:Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Inicio",
        "message": "Bem vindo"
    })