from dataclasses import dataclass
from typing import Optional


@dataclass
class Job:
    title: str
    company: str
    salary: Optional[str]
    location: Optional[str]
    experience: Optional[str]
    source: str
    status: str
    url: str
