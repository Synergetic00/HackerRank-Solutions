#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    output = set()
    comb = arr + brr
    unique = list(set(comb))
    diff = [0 for _ in range(len(unique))]
    for i in arr:
        diff[unique.index(i)] += 1
    for i in brr:
        diff[unique.index(i)] -= 1
    for i in range(len(diff)):
        if diff[i] != 0: output.add(unique[i])
    return sorted(list(output))

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(str(result))
