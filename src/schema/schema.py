from pydantic import BaseModel

from src.state import Agent


class AnimalKnowledge(BaseModel):
    animal: str
    animal_type: str
    topic: str
    response: str


class HistoryKnowledge(BaseModel):
    topic: str
    response: str


class ScienceKnowledge(BaseModel):
    topic: str
    field: str
    response: str


class Knowledge(BaseModel):
    agent: Agent
