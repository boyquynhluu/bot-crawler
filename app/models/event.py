from dataclasses import dataclass
from typing import Optional


@dataclass
class Event:
    minute: int
    type: str
    detail: str
    team: str
    player: str
    assist: Optional[str]
