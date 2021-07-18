# Warm-up Challenges

## Counting Valleys

```python
def countingValleys(steps, path):
    height = valleys = 0
    for step in path:
        height += 1 if step == "U" else -1
        valleys += height == 0 and step == "U"
    return valleys
```

## Jumping on the Clouds

```python
def jumpingOnClouds(c):
    path = ''.join([str(i) for i in c])
    jumps = path.count('1')
    jumps += sum(len(step)//2 for step in path.split('1'))
    return jumps
```

## Repeated String

```python
def repeatedString(s, n):
    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')
```

## Sales by Match

```python
def sockMerchant(n, ar):
    output = 0
    for num in set(ar):
        count = ar.count(num)
        output += count // 2
    return int(output)
```

# Arrays

## 2D Array - DS

```python
def getHourglass(arr, x, y):
    total = arr[y][x]
    for i in range(3):
        total += arr[y-1][x-1+i]
        total += arr[y+1][x-1+i]
    print(total)
    return total


def hourglassSum(arr):
    output = getHourglass(arr, 1, 1)
    for y in range(1, len(arr)-1):
        for x in range(1, len(arr[y])-1):
            output = max(output, getHourglass(arr, x, y))
    return output
```

## Arrays: Left Rotation

```python
def rotLeft(a, d):
    return a[d:] + a[:d]
```

## Minimum Swaps 2

```python
```

## New Year Chaos

```python
def minimumBribes(q):
    bribes = 0
    for i, p in enumerate(q):
        if p - i > 3:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)
```

## Array Manipulation

```python
```

# Dictionaries and Hashmaps

## Hash Tables: Ransom Note
## Two Strings
## Count Triplets
## Frequency Queries
## Sherlock and Anagrams

# Sorting



# String Manipulation

## Alternating Characters
## Strings: Making Anagrams
## Common Child
## Sherlock and the Valid String
## Special String Again

# Greedy Algorithms
# Search
# Dynamic Programming
# Stacks and Queues
# Graphs
# Trees
# Linked Lists
# Recursion and Backtracking
# Miscellaneous

## Flipping bits
## Friend Circle Queries
## Maximum Xor
## Time Complexity: Primality