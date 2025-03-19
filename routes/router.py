from fastapi import APIRouter, Request
from typing import Union
from controllers.responde_html import primeira_pagina
router = APIRouter()

@router.get("/view", response_model=None)
async def chama_template(request: Request):
    return primeira_pagina(request)

@router.get("/")
async def read_root():
    return {"teste": "olá mundo"}

@router.get("/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": f"{item_id}", "q": f"{q}"}

@router.post("/items")
async def create_item(item: dict):
    return {"message": "Criado", "item": item}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"message": f"Atualizado item {item_id}", "item": item}

@router.delete("/items/{item_id}")
async def delete_item(item_id: int, item: dict):
    return {"message": f"Deletado item {item_id}", "item": item}