# Easy

## A Very Big Sum

```python
def aVeryBigSum(ar):
    return sum(ar)
```

## Birthday Cake Candles

```python
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
```

## Compare the Triplets

```python
def compareTriplets(a, b):
    alice = bob = 0
    for i in range(len(a)):
        if a[i] > b[i]: alice += 1
        if b[i] > a[i]: bob += 1
    return [alice,bob]
```

## Diagonal Difference

```python
def diagonalDifference(arr):
    sum1 = sum2 = 0
    for x in range(0, n):
        sum1 += arr[x][x]
        sum2 += arr[x][n-x-1]
    return abs(sum1-sum2)
```

## Mini-Max Sum

```python
def miniMaxSum(arr):
    total = sum(arr)
    min = total
    max = 0
    for num in arr:
        val = total - num
        if val < min: min = val
        if val > max: max = val
    print(str(min)+" "+str(max))
```

## Plus Minus

```python
def plusMinus(arr):
    neg = pos = zro = 0
    for num in arr:
        if num < 0: neg += 1
        if num > 0: pos += 1
        if num == 0: zro += 1
    print(pos/n)
    print(neg/n)
    print(zro/n)
```

## Simple Array Sum

```python
def simpleArraySum(ar):
    return sum(ar)
```

## Solve Me First

```python
def solveMeFirst(a,b):
    return a + b
```

## Staircase

```python
def staircase(n):
    output = ""
    for row in range(0,n):
        for space in range(0, n-row-1): output += " "
        for hashtag in range(0, row+1): output += "#"
        output += "\n"
    print(output)
```

## Time Conversion

```python
def timeConversion(s):
    half = s[8:10]
    hour = int(s[0:2])
    if (half == "PM"):
        if (hour != 12): hour += 12
    else:
        if (hour == 12): hour = 0
    if hour < 10: hour = "0"+str(hour)
    output = str(hour)+s[2:8]
    return output
```