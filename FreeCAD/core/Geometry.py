"""
Geometry.py
Bibliothèque géométrique LoRaMix_Box

Toutes les primitives utilisées dans le projet.

Auteur :
Greg-Amiga
"""

import FreeCAD as App
import Part

# ==========================================================
# Boîte pleine
# ==========================================================

def make_box(length, width, height):

    return Part.makeBox(length, width, height)


# ==========================================================
# Boîte creuse
# ==========================================================

def make_shell(length,
               width,
               height,
               wall,
               bottom):

    outer = Part.makeBox(
        length,
        width,
        height
    )

    inner = Part.makeBox(
        length - wall * 2,
        width - wall * 2,
        height - bottom
    )

    inner.translate(
        App.Vector(
            wall,
            wall,
            bottom
        )
    )

    return outer.cut(inner)


# ==========================================================
# Cylindre
# ==========================================================

def make_cylinder(
        diameter,
        height):

    return Part.makeCylinder(
        diameter / 2,
        height
    )


# ==========================================================
# Entretoise PCB
# ==========================================================

def make_standoff(
        diameter,
        hole,
        height):

    body = Part.makeCylinder(
        diameter / 2,
        height
    )

    drill = Part.makeCylinder(
        hole / 2,
        height + 2
    )

    drill.translate(
        App.Vector(
            0,
            0,
            -1
        )
    )

    return body.cut(drill)


# ==========================================================
# Trou cylindrique
# ==========================================================

def make_hole(
        diameter,
        height):

    return Part.makeCylinder(
        diameter / 2,
        height
    )


# ==========================================================
# Fente
# ==========================================================

def make_slot(
        length,
        width,
        height):

    return Part.makeBox(
        length,
        width,
        height
    )


# ==========================================================
# Grille de ventilation
# ==========================================================

def make_vent_grid(
        rows,
        cols,
        slot_length,
        slot_width,
        spacing,
        height):

    slots = []

    for y in range(rows):

        for x in range(cols):

            s = make_slot(
                slot_length,
                slot_width,
                height
            )

            s.translate(
                App.Vector(
                    x * (slot_length + spacing),
                    y * (slot_width + spacing),
                    0
                )
            )

            slots.append(s)

    return slots


# ==========================================================
# Fusion
# ==========================================================

def fuse_all(parts):

    result = parts[0]

    for p in parts[1:]:

        result = result.fuse(p)

    return result


# ==========================================================
# Soustraction
# ==========================================================

def cut_all(body, tools):

    result = body

    for t in tools:

        result = result.cut(t)

    return result


# ==========================================================
# Translation
# ==========================================================

def move(shape,
         x,
         y,
         z):

    shape.translate(
        App.Vector(
            x,
            y,
            z
        )
    )

    return shape
