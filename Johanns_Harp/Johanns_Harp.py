#!/usr/bin/env python3
# Pythonic solution for Johann's Harp @ Storycode.dev
# 2023-02-14

import math

# Factorzation function
# r = starting number for result; f = factor; l = loop count
def factor(r,f,l):
    # For each iteration, multiply the result by the value
    for each in range(1,l):
        r *= f
    return r

# main program
def main():
    # Print the result, and truncate to 6 decimal places
    print(round(factor(1,math.pow(2,1/12),13),6))

# Call the main program
if __name__ == "__main__":
    main()
