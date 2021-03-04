# Easy

## Flipping bits

```python
def flippingBits(n):
    flip = (2**32)-1
    return n ^ flip
```

## Lonely Integer

```python
def lonelyinteger(a):
    output = 0
    for i in a:
        output ^= i
    return output
```

## Maximizing XOR

```python
def maximizingXor(l, r):
    return max(a ^ b for a in range(l,r+1) for b in range(a,r+1))
```

## Sum vs XOR

```python
def sumXor(n):
    return 2 ** bin(n)[2:].count('0') if n else 1
```

# Medium

## A or B

```python

```

## AND Product

```python

```

## Cipher

```python

```

## Counter game

```python

```

## Sansa and XOR

```python

```

## The Great XOR

```python

```

## What's Next?

```python

```

## Winning Lottery Ticket

```python

```

## Xor-sequence

```python

```

## Yet Another Minimax Problem

```python

```

# Hard

## Manipulative Numbers

```python

```

## Maximizing the Function

```python

```

## Mixing proteins

```python

```

## Stone Game

```python

```

## String Transmission

```python

```

## XOR Matrix

```python

```

## Xoring Ninja

```python

```

# Advanced

## 2's complement

```python

```

## Changing Bits

```python

```

## XOR key

```python

```

## XOR Subsequences

```python

```

# Expert

## Hamming Distance

```python

```

## Iterate It

```python

```