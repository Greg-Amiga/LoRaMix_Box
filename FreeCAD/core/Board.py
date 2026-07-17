"""
Board.py

Représentation interne d'un PCB.

Toutes les informations mécaniques du projet
passent par cette classe.
"""

from dataclasses import dataclass, field


@dataclass
class Hole:
    x: float
    y: float
    diameter: float


@dataclass
class Opening:
    kind: str
    side: str
    x: float
    y: float
    width: float
    height: float


@dataclass
class PCB:

    name: str = "Unknown"

    length: float = 0.0
    width: float = 0.0
    thickness: float = 1.6

    outline: list = field(default_factory=list)

    holes: list = field(default_factory=list)

    openings: list = field(default_factory=list)
