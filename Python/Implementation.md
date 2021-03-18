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
def angryProfessor(k, a):
    return "YES" if (sum(1 for i in a if i <= 0) < k) else "NO"
```

## Append and Delete

```python
def appendAndDelete(s, t, k):
    output = 0
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]: break
        output += 1
    diff = len(s)-output + len(t)-output
    return 'Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No'
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
def circularArrayRotation(a, k, queries):
    if k > len(a): k %= len(a)
    for i in range(len(a)-k):
        a.append(a.pop(0))
    return [a[query] for query in queries]
```

## Counting Valleys

```python

```

## Cut the sticks

```python
def cutTheSticks(arr):
    iters = []
    while len(arr) != 0:
        iters.append(len(arr))
        shortest = min(arr)
        arr = [i for i in arr if i-shortest !=0]
    return iters
```

## Day of the Programmer

```python

```

## Designer PDF Viewer

```python
def designerPdfViewer(h, word):
    return len(word) * max(h[ord(char) - 97] for char in word)
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
def findDigits(n):
    return sum(1 for digit in str(n) if int(digit) != 0 and n % int(digit) == 0)
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
def saveThePrisoner(n, m, s):
    return (s+m-2) % n+1
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
def hurdleRace(k, height):
    return max(0, max(height) - k)
```

## Utopian Tree

```python
def utopianTree(n):
    if n == 0: return 1
    return utopianTree(n-1)+1 if n % 2 == 0 else 2*utopianTree(n-1)
```

## Viral Advertising

```python
def viralAdvertising(n):
    given = 5
    likes = 0
    for i in range(n):
        likes += given//2
        given = given//2 * 3
    return likes
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