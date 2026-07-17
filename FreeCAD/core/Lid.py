"""
Lid.py

Construction du couvercle LoRaMix.

Auteur :
Greg-Amiga
"""

import FreeCAD as App
import Part

from config.Parameters import *

from core.Geometry import (
    make_box,
    move
)


class LidBuilder:

    def __init__(self):

        self.body = None

    # ---------------------------------------------------------

    def create_cover(self):

        self.body = make_box(
            BOX_LENGTH,
            BOX_WIDTH,
            LID
        )

    # ---------------------------------------------------------

    def create_lip(self):
        """
        Feuillure qui s'insère dans la base.
        """

        lip = Part.makeBox(
            BOX_LENGTH - WALL * 2 - CLEARANCE * 2,
            BOX_WIDTH - WALL * 2 - CLEARANCE * 2,
            6.0
        )

        move(
            lip,
            WALL + CLEARANCE,
            WALL + CLEARANCE,
            -6.0
        )

        self.body = self.body.fuse(lip)

    # ---------------------------------------------------------

    def hollow_lip(self):
        """
        Évite une pièce massive.
        """

        inner = Part.makeBox(
            BOX_LENGTH - WALL * 4 - CLEARANCE * 2,
            BOX_WIDTH - WALL * 4 - CLEARANCE * 2,
            6.2
        )

        move(
            inner,
            WALL * 2 + CLEARANCE,
            WALL * 2 + CLEARANCE,
            -6.1
        )

        self.body = self.body.cut(inner)

    # ---------------------------------------------------------

    def build(self):

        self.create_cover()

        self.create_lip()

        self.hollow_lip()

        return self.body
