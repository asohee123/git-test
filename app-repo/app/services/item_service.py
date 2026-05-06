from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from datetime import datetime

_store: dict[int, Item] = {}
_next_id = 1


def get_all() -> list[Item]:
    return list(_store.values())


def get_by_id(item_id: int) -> Item | None:
    return _store.get(item_id)


def create(data: ItemCreate) -> Item:
    global _next_id
    item = Item(id=_next_id, name=data.name, description=data.description, price=data.price)
    _store[_next_id] = item
    _next_id += 1
    return item


def update(item_id: int, data: ItemUpdate) -> Item | None:
    item = _store.get(item_id)
    if not item:
        return None
    if data.name is not None:
        item.name = data.name
    if data.description is not None:
        item.description = data.description
    if data.price is not None:
        item.price = data.price
    return item


def delete(item_id: int) -> bool:
    if item_id not in _store:
        return False
    del _store[item_id]
    return True
