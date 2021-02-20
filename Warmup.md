## Solve Me First

```python
def solveMeFirst(a,b):
	return a+b
```

## Compare the Triplets

```python
def simpleArraySum(ar):
    total = 0
    for item in ar:
        total += item
    return total
```

## A Very Big Sum

```python
def aVeryBigSum(ar):
    total = 0
    for item in ar:
        total += item
    return total
```

## Diagonal Difference

```python
def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for x in range(0, n):
        sum1 += arr[x][x]
        sum2 += arr[x][n-x-1]
    return abs(sum1-sum2)
```

## Plus Minus

```python
def plusMinus(arr):
    neg = 0
    pos = 0
    zro = 0
    for num in arr:
        if num < 0:
            neg += 1
        if num > 0:
            pos += 1
        if num == 0:
            zro += 1
    print(pos/n)
    print(neg/n)
    print(zro/n)
```

## Staircase

```python
def staircase(n):
    output = ""
    for row in range(0,n):
        for space in range(0, n-row-1):
            output += " "
        for hashtag in range(0, row+1):
            output += "#"
        output += "\n"
    print(output)
```

## Mini-Max Sum

```python
def miniMaxSum(arr):
    total = 0
    for num in arr:
        total += num
    min = total
    max = 0
    for num in arr:
        val = total - num
        if val < min:
            min = val
        if val > max:
            max = val
    print(str(min)+" "+str(max))
```

## Birthday Cake Candles

```python
def birthdayCakeCandles(candles):
    max = 0
    count = 0
    for i in candles:
        if i > max:
            max = i
    for i in candles:
        if i == max:
            count += 1
    print(count)
```

## Time Conversion

```python
def timeConversion(s):
    half = s[8:10]
    hour = int(s[0:2])
    if (half == "PM"):
        if (hour != 12):
            hour += 12
    else:
        if (hour == 12):
            hour = 0
    if hour < 10:
        hour = "0"+str(hour)
    output = str(hour)+s[2:8]
    return output
```