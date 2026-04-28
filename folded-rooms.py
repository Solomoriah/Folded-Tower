#!/usr/bin/env python3

# Folded Tower of Coldarius -- Standard Room Generator
# Copyright 2019, 2026 Chris Gonnerman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, self list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, self list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from self software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# Path to DungeoneerNG's parent folder must be set here.
# Don't be fooled by this path, on my system there's a DungeoneerNG folder
# underneath this DungeoneerNG folder.  And don't ask why.
dngpath = "/home/chris/Source/DungeoneerNG"

import sys
sys.path.append(dngpath)

roomdescription = """
<text:p text:style-name="MapKeyHeading">%(roomnumber)s. <text:span text:style-name="T20">%(roomtitle)s</text:span>: </text:p>
%(prenote)s
<text:p text:style-name="BoxedText">%(boxedtext)s </text:p>
%(notes)s
"""

from DungeoneerNG import Dice, ODT

mapinfo = {
     1: {
            "balcony": 0,
            "secret": 0,
        },
     2: {
            "balcony": 0,
            "secret": 0,
        },
     3: {
            "balcony": 0,
            "secret": 0,
        },
     4: {
            "balcony": 2,
            "secret": 0,
        },
     5: {
            "balcony": 0,
            "secret": 0,
        },
     6: {
            "balcony": 0,
            "secret": 0,
        },
     7: {
            "balcony": 0,
            "secret": 0,
        },
     8: {
            "balcony": 0,
            "secret": 1,
        },
     9: {
            "balcony": 0,
            "secret": 0,
        },
    10: {
            "balcony": 0,
            "secret": 1,
        },
    11: {
            "balcony": 0,
            "secret": 0,
        },
    12: {
            "balcony": 0,
            "secret": 0,
        },
    13: {
            "balcony": 1,
            "secret": 0,
        },
    14: {
            "balcony": 1,
            "secret": 0,
        },
    15: {
            "balcony": 0,
            "secret": 0,
        },
    16: {
            "balcony": 0,
            "secret": 1,
        },
    17: {
            "balcony": 0,
            "secret": 0,
        },
    18: {
            "balcony": 0,
            "secret": 0,
        },
    19: {
            "balcony": 0,
            "secret": 0,
        },
    20: {
            "balcony": 0,
            "secret": 0,
        },
    21: {
            "balcony": 0,
            "secret": 0,
        },
    22: {
            "balcony": 0,
            "secret": 0,
        },
    23: {
            "balcony": 0,
            "secret": 0,
        },
    24: {
            "balcony": 0,
            "secret": 0,
        },
    25: {
            "balcony": 0,
            "secret": 2,
        },
}

roomtypes = [
    0,
    ( 5, "Antechamber"),
    ( 3, "Armory"),
    ( 7, "Audience"),
    ( 2, "Aviary"),
    ( 7, "Banquet Room"),
    ( 4, "Barracks"),
    ( 6, "Bath"),
    (10, "Bedroom"),
    ( 2, "Bestiary"),
    ( 1, "Cell"),
    ( 1, "Chantry"),
    ( 2, "Chapel"),
    ( 1, "Cistern"),
    ( 3, "Classroom"),
    ( 8, "Closet"),
    ( 2, "Conjuring"),
    ( 5, "Corridor"),
    ( 1, "Courtroom"),
    ( 1, "Crypt"),
    ( 7, "Dining Room"),
    ( 2, "Divination Room"),
    ( 6, "Dormitory"),
    ( 4, "Dressing Room"),
    ( 3, "Gallery"),
    ( 3, "Game Room"),
    ( 4, "Great Hall"),
    ( 5, "Guardroom"),
    ( 6, "Hall"),
    ( 1, "Harem"),
    ( 1, "Seraglio"),
    ( 2, "Kennel"),
    ( 6, "Kitchen"),
    ( 3, "Laboratory"),
    ( 3, "Library"),
    ( 7, "Lounge"),
    ( 3, "Meditation Room"),
    ( 2, "Museum"),
    ( 1, "Observatory"),
    ( 7, "Office"),
    ( 6, "Pantry"),
    ( 2, "Prison"),
    ( 1, "Privy"),
    ( 4, "Reception Room"),
    ( 3, "Refectory"),
    ( 2, "Robing Room"),
    ( 2, "Shrine"),
    ( 7, "Sitting Room"),
    ( 3, "Smithy"),
    ( 1, "Solar"),
    ( 4, "Stable"),
    ( 6, "Storage"),
    ( 1, "Vault"),
    ( 1, "Strongroom"),
    ( 5, "Study"),
    ( 1, "Temple"),
    ( 1, "Throne Room"),
    ( 1, "Torture Chamber"),
    ( 2, "Training Room"),
    ( 2, "Trophy Room"),
    ( 8, "Vestibule"),
    ( 6, "Waiting Room"),
    ( 3, "Water Closet"),
    ( 3, "Well"),
    ( 4, "Workroom"),
    ( 6, "Workshop"),
]


lighting = [
    0,
    (4, "magically illuminated"),
    (6, "unlit"),
]

flooring = [
    0,
    (1, "white marble"),
    (5, "dark gray tiles"),
    (3, "light gray tiles"),
    (3, "tan tiles"),
    (5, "dark red tiles"),
    (1, "%(color)s mosaic tiles %(arrangement)s", {
        "color":        [
                            0,
                            (1, "warm-colored"),
                            (1, "cool-colored"),
                            (1, "black and white"),
                            (1, "purple, blue, and red"),
                            (1, "green, yellow, and brown"),
                        ],
        "arrangement":  [
                            0,
                            (4, "in a random pattern"),
                            (3, "in a knotwork pattern"),
                            (1, "depicting a face"),
                            (1, "depicting an eye"),
                            (1, "depicting a shield"),
                            (1, "depicting a star"),
                            (1, "depicting patterns of overlaid circles"),
                        ],
    }),
    (1, "pale wood"),
    (2, "medium-tone wood"),
    (3, "dark wood"),
    (1, "bright silver plates"),
    (1, "shining gold"),
]

walls = [
    0,
    (5, "dark wood paneling"),
    (4, "light wood paneling"),
    (3, "medium wood paneling"),
    (5, "%(plaster)s", {
        "plaster":  [
                        0,
                        (10, "red-painted plaster"),
                        (30, "green-painted plaster"),
                        (20, "blue-painted plaster"),
                        ( 5, "unpainted plaster"),
                        ( 2, "religious murals painted on plaster"),
                        ( 2, "heroic murals painted on plaster"),
                    ],
    }),
    (1, "white tiles"),
    (2, "gray tiles"),
    (3, "green tiles"),
    (2, "light brown tiles"),
]

ceiling = [
    0,
    (4, "dark wood crossed at intervals by heavy wooden timbers"),
    (3, "pale wood crossed at intervals by heavy wooden timbers"),
    (1, "plaster, painted black"),
    (2, "plaster, painted light blue"),
    (3, "plaster, painted light green"),
    (2, "plaster, painted yellow"),
]

descriptions = [
    0,
    (1, "This %(roomtype)s is %(lighting)s. " +
        "The floor is covered with %(floor)s, " +
        "the walls with %(walls)s, and " +
        "the ceiling with %(ceiling)s."),
    (1, "This %(lighting)s %(roomtype)s has a floor of %(floor)s, " +
        "walls of %(walls)s, and on the ceiling is %(ceiling)s."),
]


output = []

for i in range(1, 8):

    output.append(ODT.genericparagraph("Tower Level %d" % i, style = "SubHeading"))

    for q in ("A", "B", "C", "D"):
        for n in range(1, 26):
            outdata = {
                "roomnumber": "%d%s%d" % (i, q, n),
                "roomtitle":  Dice.tableroller(roomtypes)[1].upper(),
                "prenote": "",
                "notes": "",
            }

            room = {}
            room["lighting"] = Dice.tableroller(lighting)[1]
            room["roomtype"] = "room"

            if mapinfo[n]["secret"] == 1:
                outdata["roomtitle"] = "SECRET ROOM"
            elif mapinfo[n]["secret"] == 2:
                outdata["roomtitle"] = "SECRET CORRIDOR"
                room["roomtype"] = "corridor"

            room["floor"] = Dice.tableroller(flooring)
            if len(room["floor"]) == 2:
                room["floor"] = room["floor"][1]
            else:
                msg = room["floor"][1]
                data = {}
                for k in room["floor"][2].keys():
                    data[k] = Dice.tableroller(room["floor"][2][k])[1]
                room["floor"] = msg % data

            room["ceiling"] = Dice.tableroller(ceiling)
            if len(room["ceiling"]) == 2:
                room["ceiling"] = room["ceiling"][1]
            else:
                msg = room["ceiling"][1]
                data = {}
                for k in room["ceiling"][2].keys():
                    data[k] = Dice.tableroller(room["ceiling"][2][k])[1]
                room["ceiling"] = msg % data

            room["walls"] = Dice.tableroller(walls)
            if len(room["walls"]) == 2:
                room["walls"] = room["walls"][1]
            else:
                msg = room["walls"][1]
                data = {}
                for k in room["walls"][2].keys():
                    data[k] = Dice.tableroller(room["walls"][2][k])[1]
                room["walls"] = msg % data

            outdata["boxedtext"] = Dice.tableroller(descriptions)[1] % room

            output.append(ODT.genericparagraph("%(roomnumber)s. %(roomtitle)s:" % outdata, style = "MapKeyHeading"))
            output.append(ODT.genericparagraph(outdata["boxedtext"], style = "BoxedText"))


ODT.saveodt("".join(output),
    defcontent = "%s/DungeoneerNG/content.static" % dngpath,
    base = "%s/DungeoneerNG/base.odt" % dngpath)


# end of file.
