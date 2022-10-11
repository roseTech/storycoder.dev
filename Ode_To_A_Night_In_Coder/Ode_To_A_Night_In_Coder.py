#!/usr/bin/env python3

bell_rings = 0

for hour in list(range(8, 12 + 1)) + list(range(1, 5 + 1)):
    bell_rings += hour
    for minute in range(0, 60, 15):
        # print(hour, minute)
        bell_rings += minute // 15

print(bell_rings)
