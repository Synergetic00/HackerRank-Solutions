#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    for i in range(1,len(pile)):
        pile[0] ^= pile[i]
    return 'Second' if pile[0] == 0 else 'First'

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        print(nimGame(result))

