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
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum((apple + a) in range(s,t+1) for apple in apples))
    print(sum((orange + b) in range(s,t+1) for orange in oranges))
```

## Beautiful Days at the Movies

```python
def beautifulDays(i, j, k):
    return sum(1 for day in range(i, j+1) if abs(day-int(str(day)[::-1])) % k == 0)
```

## Beautiful Triplets

```python
def beautifulTriplets(d, arr):
    return sum(1 for i in arr if i+d in arr and i+2*d in arr)
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

## Bill Division

```python
def bonAppetit(bill, k, b):
    total = sum(bill)
    anna = total - bill[k]
    half = int(anna / 2)
    due = b - half
    if due == 0:
        print("Bon Appetit")
    else:
        print(due)
```

## Breaking the Records

```python
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

## Cats and a Mouse

```python
def catAndMouse(x, y, z):
    diffb = abs(z-y)
    diffa = abs(z-x)
    if diffa == diffb:
        output = "Mouse C"
    else:
        output = "Cat A" if diffa < diffb else "Cat B"
    return output
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
def countingValleys(steps, path):
    height = valleys = 0
    for step in path:
        height += 1 if step == "U" else -1
        valleys += height == 0 and step == "U"
    return valleys
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
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def dayOfProgrammer(year):
    print(isLeapYear(year))
    normal = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    if (year < 1918):
        if year % 4 == 0:
            normal += 1
    elif (year == 1918):
        normal -= 13
    else:
        if isLeapYear(year):
            normal += 1
    diff = 256 - normal
    return str(diff)+".09."+str(year)
```

## Designer PDF Viewer

```python
def designerPdfViewer(h, word):
    return len(word) * max(h[ord(char) - 97] for char in word)
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

## Drawing Book

```python
def pageCount(n, p):
    return min(p//2, n//2 - p//2)
```

## Electronics Shop

```python
def getMoneySpent(keyboards, drives, b):
    output = -1
    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive
            if total <= b:
                output = max(output, total)
    return output
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
def processGrade(grade):
    output = 0
    rounded = math.ceil(grade/5) * 5
    if (rounded - grade < 3):
        output = rounded
    if (output < 40):
        return grade
    return output
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
def migratoryBirds(arr):
    count = [0,0,0,0,0]
    for num in arr:
        count[num-1] += 1
    return count.index(max(count)) + 1
```

## Minimum Distances

```python

```

## Modified Kaprekar Numbers

```python

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
        return 'NO'
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
def sockMerchant(n, ar):
    output = 0
    for num in set(ar):
        count = ar.count(num)
        output += count // 2
    return int(output)
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
def birthday(s, d, m):
    print("started")
    output = 0
    for x in range(len(s)-m+1):
        if sum(s[x:x+m])==d:
            output+=1
    return output
```

## Taum and B'day

```python
def taumBday(b, w, bc, wc, z):
    if (bc > wc + z):
        return (b + w) * wc + b * z
    elif(wc > bc + z):
        return (b + w) * bc + w * z
    else:
        return b * bc + w * wc
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