from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Item:
    id: int
    name: str
    description: str
    price: float
    created_at: datetime = field(default_factory=datetime.utcnow)
