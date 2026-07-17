"""
Base.py

Construction de la partie inférieure du boîtier LoRaMix.

Auteur :
Greg-Amiga
"""

import FreeCAD as App
import Part

from config.Parameters import *

from core.Geometry import (
    make_shell,
    make_standoff,
    move,
    fuse_all
)


class BaseBuilder:

    def __init__(self):

        self.body = None

    # ---------------------------------------------------------

    def create_shell(self):

        self.body = make_shell(
            pcb.length
            pcb.width
            BOX_HEIGHT - LID,
            WALL,
            BOTTOM
        )

    # ---------------------------------------------------------

    def add_standoffs(self):

        supports = []

        for x, y in STANDOFFS:

            s = make_standoff(
                STANDOFF_DIAMETER,
                STANDOFF_HOLE,
                STANDOFF_HEIGHT
            )

            move(
                s,
                WALL + CLEARANCE + x,
                WALL + CLEARANCE + y,
                BOTTOM
            )

            supports.append(s)

        self.body = self.body.fuse(
            fuse_all(supports)
        )

    # ---------------------------------------------------------

    def build(self):

        self.create_shell()

        self.add_standoffs()

        return self.body
