# Easy

## Arithmetic Operators

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a + b)
    print(a - b)
    print(a * b)
```

## Loops

```python
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i * i)
```

## Print Function

```python
if __name__ == '__main__':
    n = int(input())
    
    print(''.join([str(i) for i in range(1, n+1)]))
```

## Python If-Else

```python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 1:
        w = True
    else:
        if n in range(2,6):
            w = False
        if n in range(6,21):
            w = True
        else:
            w = False
            
    print("Weird" if w else "Not Weird")
```

## Python: Division

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a // b)
    print(a / b)
```

## Say "Hello, World!" With Python

```python
print("Hello, World!")
```

# Medium

## Write a function

```python
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
```