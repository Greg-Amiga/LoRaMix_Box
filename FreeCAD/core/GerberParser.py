"""
GerberParser.py

Interface de lecture des fichiers Gerber et Excellon.

V1 :
- lecture des fichiers
- préparation de la structure de données

Les méthodes d'analyse seront complétées
progressivement.
"""

from pathlib import Path


class GerberParser:

    def __init__(self, folder):

        self.folder = Path(folder)

        self.outline = None
        self.drill = None

    # ---------------------------------------------------------

    def locate_files(self):

        for f in self.folder.iterdir():

            suffix = f.suffix.upper()

            if suffix == ".GKO":
                self.outline = f

            elif suffix == ".DRL":
                self.drill = f

    # ---------------------------------------------------------

    def check(self):

        if self.outline is None:
            raise FileNotFoundError("BoardOutline (.GKO) absent")

        if self.drill is None:
            raise FileNotFoundError("Drill (.DRL) absent")

    # ---------------------------------------------------------

    def load(self):

        self.locate_files()

        self.check()

        print("Outline :", self.outline)
        print("Drill   :", self.drill)

        return {
            "outline": self.outline,
            "drill": self.drill
        }
