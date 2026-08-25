from dataclasses import dataclass, field
from typing import Optional

from app.models.event import Event


@dataclass
class Fixture:
    fixture_id: int
    date: str
    league: str
    round: str
    home_team: str
    away_team: str
    home_score: Optional[int]
    away_score: Optional[int]
    status: str
    events: list[Event] = field(default_factory=list)
