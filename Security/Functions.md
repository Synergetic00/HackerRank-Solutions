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
n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n+1):
    print(arr.index(i)+1)
```

## Security Involution

```python
n = int(input())
arr = list(map(int, input().split()))
print('YES' if all(arr[i-1] is arr.index(i)+1 for i in arr) else 'NO')
```

## Security Permutations

```python
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    print(arr[(arr[i]-1)])
```