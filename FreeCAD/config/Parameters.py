"""
LoRaMix_Box
Configuration globale

Toutes les dimensions sont exprimées en millimètres.
Modifier ce fichier suffit pour adapter le boîtier.
"""

# ==========================================================
# PCB
# ==========================================================

PCB_LENGTH = 105.00
PCB_WIDTH = 80.00
PCB_THICKNESS = 1.60

# Hauteur maximale des composants
PCB_COMPONENT_HEIGHT = 28.0

# ==========================================================
# Jeu mécanique
# ==========================================================

CLEARANCE = 0.30

# ==========================================================
# Boîtier
# ==========================================================

WALL = 2.20
BOTTOM = 3.00
LID = 2.50

INSIDE_HEIGHT = 34.00

# Rayon extérieur
CORNER_RADIUS = 7.00

# ==========================================================
# Colonnettes
# ==========================================================

STANDOFF_DIAMETER = 7.0
STANDOFF_HOLE = 2.80
STANDOFF_HEIGHT = 5.00

# Positions (à ajuster après lecture des Gerber)
STANDOFFS = [
    (5, 5),
    (100, 5),
    (100, 75),
    (5, 75),
]

# ==========================================================
# Connecteurs
# ==========================================================

ENABLE_RJ45 = True
ENABLE_SMA = True
ENABLE_USB = False

# ==========================================================
# Ventilation
# ==========================================================

ENABLE_VENTILATION = True

VENT_SLOT_WIDTH = 2.0
VENT_SLOT_SPACING = 3.0
VENT_SLOT_LENGTH = 20.0

# ==========================================================
# Impression
# ==========================================================

NOZZLE = 0.40
LAYER_HEIGHT = 0.20

# ==========================================================
# Logo
# ==========================================================

SHOW_LOGO = True

LOGO_TEXT = "LoRa Mix"

AUTHOR = "Greg-Amiga"

# ==========================================================
# Calculs automatiques
# ==========================================================

BOX_LENGTH = PCB_LENGTH + WALL * 2 + CLEARANCE * 2
BOX_WIDTH = PCB_WIDTH + WALL * 2 + CLEARANCE * 2
BOX_HEIGHT = INSIDE_HEIGHT + BOTTOM + LID
