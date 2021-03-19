# Easy

## A Chessboard Game

```python
def chessboardGame(x, y):
    return 'Second' if x % 4 in [1, 2] and y % 4 in [1,2] else 'First'
```

## Game of Stones

```python
def gameOfStones(n):
    return "Second" if n % 7 < 2 else "First"
```

## Introduction to Nim Game

```python
def nimGame(pile):
    for i in range(1,len(pile)):
        pile[0] ^= pile[i]
    return 'Second' if pile[0] == 0 else 'First'

```

## Misère Nim

```python
def misereNim(s):
    bool = list(set(s)) == [1]
    for i in range(1,len(s)):
        s[0] ^= s[i]
    return 'Second' if s[0] == 0 ^ bool else 'First'
```

## Nimble Game

```python
def nimbleGame(s):
    xor = 0
    for i in range(len(s)):
        if s[i] % 2 == 1:
            xor ^= i
    return 'Second' if xor == 0 else 'First'
```

## Poker Nim

```python
def pokerNim(k, c):
    for i in range(1,len(c)):
        c[0] ^= c[i]
    return 'Second' if c[0] == 0 else 'First'
```

## Tower Breakers

```python
def towerBreakers(n, m):
    return 2 if (m == 1 or n % 2 == 0) else 1
```

# Medium

## A stones game

```python

```

## Alice and Bob's Silly Game

```python

```

## Bob and Ben

```python

```

## Chessboard Game, Again!

```python

```

## Chocolate in Box

```python

```

## Deforestation

```python

```

## Digits Square Board

```python

```

## Fun Game

```python

```

## Kitty and Katty

```python

```

## New Year Game

```python

```

## Permutation game

```python

```

## Play on benders

```python

```

## Powers Game

```python

```

## Tower Breakers - The Final Battle

```python

```

## Tower Breakers, Again!

```python

```

## Tower Breakers, Revisited!

```python

```

## Vertical Rooks

```python

```

## Zero-Move Nim

```python

```

# Hard

## Chocolate Game

```python

```

## Move the Coins

```python

```

## Simple Game

```python

```

## Stone Division

```python

```

## Stone Piles

```python

```

## The Prime Game

```python

```

# Expert

## Tastes Like Winning

```python

```