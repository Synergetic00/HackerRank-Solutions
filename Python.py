#!/bin/python3

import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    iters = []
    while len(arr) != 0:
        iters.append(len(arr))
        shortest = min(arr)
        arr = [i for i in arr if i-shortest !=0]
    return iters

def findDigits(n):
    return sum(1 for digit in str(n) if int(digit) != 0 and n % int(digit) == 0)

def circularArrayRotation(a, k, queries):
    for i in range(len(a)-k):
        a.append(a.pop(0))
    for query in queries:
        print(a[query])

def viralAdvertising(n):
    given = 5
    likes = 0
    for i in range(n):
        likes += given//2
        given = given//2 * 3
    return likes

def beautifulDays(i, j, k):
    return sum(1 for day in range(i, j+1) if abs(day-int(str(day)[::-1])) % k == 0)

#print(beautifulDays(20,23,6))
#print(viralAdvertising(3))
print(circularArrayRotation([1,2,3],2,[0,1,2]))
print(findDigits(10))