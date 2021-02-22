# Easy

## Grading Students

```python
def processGrade(grade):
    output = 0
    rounded = math.ceil(grade/5) * 5
    if (rounded - grade < 3):
        output = rounded
    if (output < 40):
        return grade
    return output

def gradingStudents(grades):
    output = []
    for grade in grades:
        output.append(processGrade(grade))
    return output
```

## Apples and Oranges

```python
def countApplesAndOranges(s, t, a, b, apples, oranges):
    outApples = 0
    outOranges = 0
    for apple in apples:
        if apple > 0:
            if (apple + a) in range(s,t+1):
                outApples += 1
    for orange in oranges:
        if orange < 0:
            if (orange + b) in range(s,t+1):
                outOranges += 1
    print(outApples)
    print(outOranges)
```

## Number Line Jumps

```python
def kangaroo(x1, v1, x2, v2):

    if v1 == v2 and x1 == x2:
        return "YES"
    elif v1 == v2:
        return "NO"

    x = (x2-x1) / (v1-v2)
    if x > 0 and x % 1 == 0:
        return "YES"
    else:
        return "NO"
```

## Between Two Sets

```python
def isFactor(big, small):
    if (small > big):
        return False
    elif (small == big):
        return True
    else:
        return big % small == 0

def getTotalX(a, b):
    output = 0
    start = a[len(a)-1]
    end = b[0]
    for num in range(start,end+1):
        totala = 0
        for numa in a:
            if isFactor(num, numa):
                totala += 1
        totalb = 0
        for numb in b:
            if isFactor(numb, num):
                totalb += 1
        if len(a) == totala and len(b) == totalb:
            output += 1
    return output
```

## Breaking the Records

```python
def breakingRecords(scores):
    min = scores[0]
    mins = 0
    max = scores[0]
    maxs = 0
    for num in scores:
        if num > max:
            max = num
            maxs += 1
        if num < min:
            min = num
            mins += 1
    return [maxs,mins]
```

## Subarray Division

```python
def birthday(s, d, m):
    output = 0
    for x in range(len(s)-m+1):
        if sum(s[x:x+m])==d:
            output+=1
    return output
```

## Divisible Sum Pairs

```python
def divisibleSumPairs(n, k, ar):
    output = 0
    for a in range(len(ar)):
        for b in range(a+1, n):
            if (ar[a] + ar[b]) % k == 0:
                output += 1
    return output
```

## Migratory Birds

```python
def migratoryBirds(arr):
    count = [0,0,0,0,0]
    for num in arr:
        count[num-1] += 1
    return count.index(max(count)) + 1
```

## Day of the Programmer

```python
```

## Bill Division

```python
```

## Sales by Match

```python
```

## Drawing Book

```python
```

## Counting Valleys

```python
```

## Electronics Shop

```python
```

## Cats and a Mouse

```python
```

## Picking Numbers

```python
```

## The Hurdle Race

```python
```

## Designer PDF Viewer

```python
```

## Utopian Tree

```python
```

## Angry Professor

```python
```

## Beautiful Days at the Movies

```python
```

## Viral Advertising

```python
```

## Save the Prisoner!

```python
```

## Circular Array Rotation

```python
```

## Sequence Equation

```python
```

## Jumping on the Clouds: Revisited

```python
```

## Find Digits

```python
```

## Append and Delete

```python
```

## Sherlock and Squares

```python
```

## Library Fine

```python
```

## Cut the sticks

```python
```

## Repeated String

```python
```

## Jumping on the Clouds

```python
```

## Equalize the Array

```python
```

## ACM ICPC Team

```python
```

## Taum and B'day

```python
```

## Modified Kaprekar Numbers

```python
```

## Beautiful Triplets

```python
```

## Minimum Distances

```python
```

## Halloween Sale

```python
```

## Chocolate Feast

```python
```

## Service Lane

```python
```

## Lisa's Workbook

```python
```

## Flatland Space Stations

```python
```

## Fair Rations

```python
```

## Cavity Map

```python
```

## Manasa and Stones

```python
```

## Happy Ladybugs

```python
```

## Strange Counter

```python
```