#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    diffb = abs(z-y)
    diffa = abs(z-x)
    if diffa == diffb:
        output = "Mouse C"
    else:
        output = "Cat A" if diffa < diffb else "Cat B"
    return output

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
