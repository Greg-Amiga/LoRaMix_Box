"""
Création des ouvertures du boîtier
"""

import Part
import FreeCAD as App

from core.Geometry import move


class OpeningBuilder:

    def __init__(self, body):

        self.body = body

    # --------------------------------------------------

    def rectangular(self,
                    x,
                    y,
                    z,
                    lx,
                    ly,
                    lz):

        hole = Part.makeBox(
            lx,
            ly,
            lz
        )

        move(
            hole,
            x,
            y,
            z
        )

        self.body = self.body.cut(hole)

    # --------------------------------------------------

    def circular(self,
                 x,
                 y,
                 z,
                 diameter,
                 depth):

        hole = Part.makeCylinder(
            diameter/2,
            depth
        )

        move(
            hole,
            x,
            y,
            z
        )

        self.body = self.body.cut(hole)

    # --------------------------------------------------

    def build(self, pcb.openings):

        for opening in pcb.openings["openings"]:

            if opening["type"] == "RJ45":

                self.rectangular(
                    0,
                    opening["x"],
                    opening["z"],
                    5,
                    opening["width"],
                    opening["height"]
                )

            elif opening["type"] == "BORNIER":

                self.rectangular(
                    100,
                    opening["x"],
                    10,
                    5,
                    opening["width"],
                    opening["height"]
                )

            elif opening["type"] == "SMA":

                self.circular(
                    opening["x"],
                    40,
                    20,
                    opening["diameter"],
                    10
                )

        return self.body
