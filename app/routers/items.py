from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.services import item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse])
def list_items():
    return item_service.get_all()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    item = item_service.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(data: ItemCreate):
    return item_service.create(data)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, data: ItemUpdate):
    item = item_service.update(item_id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    if not item_service.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
