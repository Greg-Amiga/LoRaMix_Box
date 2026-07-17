"""
Configuration mécanique de la carte LoRaMix V2 Premium

Toutes les coordonnées sont exprimées
par rapport au coin inférieur gauche du PCB.
"""

BOARD = {

    "name": "LoRaMix V2 Premium",

    "pcb": {
        "length": 105.0,
        "width": 80.0,
        "thickness": 1.6
    },

    "mounting_holes": [

        (5.0, 5.0),

        (100.0, 5.0),

        (100.0, 75.0),

        (5.0, 75.0)

    ],

    "openings": [

        {
            "type": "RJ45",
            "side": "left",
            "x": 0,
            "z": 12,
            "width": 16,
            "height": 14
        },

        {
            "type": "SMA",
            "side": "top",
            "x": 45,
            "diameter": 7
        },

        {
            "type": "BORNIER",
            "side": "right",
            "x": 20,
            "width": 32,
            "height": 12
        }

    ]
}
