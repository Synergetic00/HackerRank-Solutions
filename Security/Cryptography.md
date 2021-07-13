# Easy

## Keyword Transposition Cipher

```python
import string

alpha = list(string.ascii_uppercase)
n = int(input())

for i in range(n):
    key = input()
    cipher = input()

    included = list(dict.fromkeys(key))
    excluded = [i for i in alpha if i not in key]
    order = included + excluded

    cols = len(included)
    rows = (-(-26 // cols))

    indexes = [['']*(rows) for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            idx = i+j*cols
            if idx < 26:
                indexes[i][j] = order[idx]

    substitution = ''.join(sorted([''.join(i) for i in indexes], key=lambda x:x[0]))

    output = ''

    for c in cipher:
        if c != ' ':
            output += (alpha[substitution.index(c)])
        else:
            output += ' '

    print(output)
```

# Medium

## PRNG Sequence Guessing

```python
```

# Hard

## Basic Cryptanalysis

```python
```