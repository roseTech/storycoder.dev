# Johann's Harp solution in Nim
# Rubberduck.tech + human-edited
# 2023-02-14

import std/strformat
import std/math

# Factorize 12 times, the 2^(1/12) increase each time
var product = 1.0
var factor = math.pow(2,1/12)
for i in 1..12:
    product *= factor

# Round the result to 6 decimal places
echo fmt"{product:.6f}"
