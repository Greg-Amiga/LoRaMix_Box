"""
Export.py

Fonctions d'export du projet LoRaMix_Box.
"""

import os
import Mesh
import ImportGui


class ExportManager:

    def __init__(self, document):

        self.document = document

    # ---------------------------------------------------------

    def _ensure_dir(self, path):

        if not os.path.isdir(path):
            os.makedirs(path)

    # ---------------------------------------------------------

    def export_stl(self,
                   obj,
                   filename):

        folder = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "STL"
            )
        )

        self._ensure_dir(folder)

        path = os.path.join(folder, filename)

        Mesh.export(
            [obj],
            path
        )

        print("STL :", path)

    # ---------------------------------------------------------

    def export_step(self,
                    obj,
                    filename):

        folder = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "STEP"
            )
        )

        self._ensure_dir(folder)

        path = os.path.join(folder, filename)

        ImportGui.export(
            [obj],
            path
        )

        print("STEP :", path)

    # ---------------------------------------------------------

    def export_all(self):

        for obj in self.document.Objects:

            if obj.Name == "Base":

                self.export_stl(
                    obj,
                    "LoRaMix_Base.stl"
                )

                self.export_step(
                    obj,
                    "LoRaMix_Base.step"
                )

            elif obj.Name == "Lid":

                self.export_stl(
                    obj,
                    "LoRaMix_Lid.stl"
                )

                self.export_step(
                    obj,
                    "LoRaMix_Lid.step"
                )
