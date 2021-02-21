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
```