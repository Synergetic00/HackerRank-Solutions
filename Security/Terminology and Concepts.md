# Easy

## Security - Message Space and Ciphertext Space

```python
print(''.join(str((int(i)+1)%10) for i in input()))
```

## Security Encryption Scheme

```python
def factorial(num):
    return 1 if num < 2 else num * factorial(num-1)
print(factorial(int(input())))
```

## Security Key Spaces

```python
num = input()
shift = int(input()) 
print(''.join(str((int(i)+shift)%10) for i in num))
```