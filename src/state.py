from enum import Enum
from typing import TypedDict


class Agent(Enum):
    ANIMAL = "animal"
    HISTORY = "history"
    SCIENCE = "science"


class DetailedLevel(Enum):
    BRIEF = "brief"
    DETAILED = "detailed"


class TargetAudience(Enum):
    CHILD = "child"
    TEEN = "teen"
    ADULT = "adult"


class KnowledgeState(TypedDict):
    message: str
    agent: Agent
    target_audience: TargetAudience
    topic: str
    detailed_level: DetailedLevel
    response: str
    payload: dict
