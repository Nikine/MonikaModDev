## TODO
## we need a neato menu for everything
#
# VER: python 2.7

import spritepuller as spp
import spritechecker as spc
import menutils

menu_main = [
    ("MAS Dev Tools", "Utility: "),
    ("Sprite Puller", spp.run),
    ("Check Sprites", spc.run)
]

choice = True

while choice is not None:

    choice = menutils.menu(menu_main)

    if choice is not None:
        choice()

