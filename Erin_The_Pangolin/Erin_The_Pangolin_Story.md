---
Author: Noctiluca
License: CC BY-NC-SA 4.0
Coding Level: beginner
Coding Ideas: loop, array, derivative
Story Content: animal, pangolin, mountain
Story Genre: fiction, family story
---

# Erin the Pangolin

Erin was a different soul within the world of Pangolin souls. She always knew that
there was something special about her. All her friends and family where eating
the whole day and the only thing they talked about was Black ants, Red ants,
Yellow Meadow ants and and and.

Only Lucia, her sister, was also somewhat different, she loved to steal food
from this smelly, sweating, shouting, ape-like animals. One day Lucia told her,
that the ape-likes would like to take her to a Zoo, and that was it.

For Erin, this was not enough and she started to think about an adventure. She
wanted to reach the highest speed a Pangolin ever did.

Some Himalayan peaks around her seemed like a good opportunity. Walking slowly
up, then running as fast as possible, and while running, shaping herself into
her ball stance and .... woooooooooooosh rolling down the cliffs, hills, and
ridges.

She knew exactly how high the peaks, surrounding her, were, Frederic her
grand-pa told her: 1335, 1439, 987, 312, 871, 1461, 1171, 654 and 123 meters
high. But the important question was: Between which peak would she reach the
fastest speed? It quite likely would be the peak where there was the biggest
steepness.

Which peak would this be?

<div data-solution="3"></div>

What is the maximum steepness?

<div data-solution="675"></div>

Assumptions:

- Erin only goes forward, one peak after the other
- The list of peaks is ordered
- Erin only rolles downward (as she cannot fly)

Hints

1. Make an array of all the peaks
2. Set a variable of the maximal peak index to `0`
3. Set a variable of the maximal difference to `0`
4. Make a for loop, calculating only the positive difference between one item in
   the array and the adjacent item
5. Set two new conditions in the loop, by setting the maximal peak index to i
   and the maximal difference to `peaks[i] - peaks[i + 1]`
6. Print maximal peak index (start from `1` not from `0`)
7. Print the maximal difference
