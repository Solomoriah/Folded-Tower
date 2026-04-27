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
<text:p text:style-name="BoxedText">%(boxedtext)s </text:p>
"""

from DungeoneerNG import Dice, Stocker, ODT

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
    (1, "This room is %(lighting)s. " +
        "The floor is covered with %(floor)s, " +
        "the walls with %(walls)s, and " +
        "the ceiling with %(ceiling)s."),
    (1, "This %(lighting)s room has a floor of %(floor)s, " +
        "walls of %(walls)s, and on the ceiling is %(ceiling)s."),
]


output = []

for i in range(1, 8):

    output.append(ODT.genericparagraph("Tower Level %d" % i, style = "SubHeading"))

    for q in ("A", "B", "C", "D"):
        for n in range(1, 26):
            outdata = {
                "roomnumber": "%d%s%d" % (i, q, n),
                "roomtitle":  Dice.tableroller(Stocker.roomtypes)[1].upper(),
            }

            room = {}

            room["lighting"] = Dice.tableroller(lighting)[1]

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
