# Easy

## Security Bijective Functions

```python
n = int(input())
arr = list(map(int, input().split()))
print('YES' if (n*(n+1))/2 == sum(arr) else 'NO')
```

## Security Functions

```python
def calculate(x):
    return x % 11
```

## Security Functions II

```python
def function(x):
   return x * x 
```

## Security Function Inverses

```python
```

## Security Involution

```python
```

## Security Permutations

```python
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    print(arr[(arr[i]-1)])
```