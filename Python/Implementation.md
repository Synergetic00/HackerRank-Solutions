# Easy

## ACM ICPC Team

```python
def acmTeam(topic):
    known = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            comb = int(topic[i]) + int(topic[j])
            known.append(len(str(comb)) - str(comb).count("0"))
    return [max(known),known.count(max(known))]
```

## Angry Professor

```python

```

## Append and Delete

```python

```

## Apple and Orange

```python

```

## Beautiful Days at the Movies

```python

```

## Beautiful Triplets

```python

```

## Between Two Sets

```python

```

## Bill Division

```python

```

## Breaking the Records

```python

```

## Cats and a Mouse

```python

```

## Cavity Map

```python

```

## Chocolate Feast

```python

```

## Circular Array Rotation

```python

```

## Counting Valleys

```python

```

## Cut the sticks

```python

```

## Day of the Programmer

```python

```

## Designer PDF Viewer

```python

```

## Divisible Sum Pairs

```python

```

## Drawing Book

```python

```

## Electronics Shop

```python

```

## Equalize the Array

```python

```

## Fair Rations

```python

```

## Find Digits

```python

```

## Flatland Space Stations

```python

```

## Grading Students

```python

```

## Halloween Sale

```python

```

## Happy Ladybugs

```python

```

## Jumping on the Clouds

```python

```

## Jumping on the Clouds: Revisited

```python

```

## Library Fine

```python

```

## Lisa's Workbook

```python

```

## Manasa and Stones

```python

```

## Migratory Birds

```python

```

## Minimum Distances

```python

```

## Modified Kaprekar Numbers

```python

```

## Number Line Jumps

```python

```

## Picking Numbers

```python
def pickingNumbers(a):
    output = 0
    for i in a:
        cur = a.count(i)
        prv = a.count(i-1)

        if cur + prv > output:
            output = cur + prv
    return output
```

## Repeated String

```python

```

## Sales by Match

```python

```

## Save the Prisoner!

```python

```

## Sequence Equation

```python

```

## Service Lane

```python

```

## Sherlock and Squares

```python

```

## Strange Counter

```python

```

## Subarray Division

```python

```

## Taum and B'day

```python

```

## The Hurdle Race

```python

```

## Utopian Tree

```python

```

## Viral Advertising

```python

```

# Medium

## 3D Surface Area

```python

```

## Absolute Permutation

```python

```

## Almost Sorted

```python

```

## Bigger is Greater

```python

```

## Climbing the Leaderboard

```python

```

## Ema's Supercomputer

```python

```

## Encryption

```python

```

## Extra Long Factorials

```python

```

## Forming a Magic Square

```python

```

## Larry's Array

```python

```

## Non-Divisible Subset

```python

```

## Organizing Containers of Balls

```python

```

## Queen's Attack II

```python

```

## The Bomberman Game

```python

```

## The Grid Search

```python

```

## The Time in Words

```python

```

# Hard

## Matrix Layer Rotation

```python

```