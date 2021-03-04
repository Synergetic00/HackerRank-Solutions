# Easy

## Ice Cream Parlor

```python

```

## Missing Numbers

```python
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
```

## Sherlock and Array

```python

```

# Medium

## Beautiful Quadruples

```python

```

## Connected Cells in a Grid

```python

```

## Count Luck

```python

```

## Cut the Tree

```python

```

## Gena Playing Hanoi

```python

```

## Gridland Metro

```python

```

## Hackerland Radio Transmitters

```python

```

## KnightL on a Chessboard

```python

```

## Minimum Loss

```python

```

## Pairs

```python

```

## Red Knight's Shortest Path

```python

```

## Short Palindrome

```python

```

# Hard

## Absolute Element Sums

```python

```

## Bike Racers

```python

```

## King Richard's Knights

```python

```

## Making Candies

```python

```

## Maximizing Mission Points

```python

```

## Maximum Subarray Sum

```python

```

## Sorted Subsegments

```python

```

# Advanced

## Similar Pair

```python

```

## Task Scheduling

```python

```

# Expert

## Almost Integer Rock Garden

```python

```

## Distant Pairs

```python

```