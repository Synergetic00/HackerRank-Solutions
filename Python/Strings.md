# Easy

## Alphabet Rangoli

```python
from string import ascii_lowercase as alpha

def print_rangoli(size):
    a = alpha[:size][::-1]
    for i in range((size - 1) * 2 + 1):
        dnum = abs(size - 1 - i)
        val = abs(dnum - size + 1)
        f = a[:val + 1]
        b = f[::-1][1:]
        s = '-'.join(f + b)
        dash = '-' * dnum * 2
        out = dash + s + dash
        print(out)
```

## Capitalize!

```python
def solve(s):
    arr = s.split(' ')
    return ' '.join([i.capitalize() for i in arr])
```

## Designer Door Mat

```python
s = input().split()
N = int(s[0])
M = int(s[1])

for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))
```

## Find a string

```python
def count_substring(string, sub_string):
    return sum(1 for i in range(len(string) - len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string)
```

```python
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string)+1):
        s = string[i:i+len(sub_string)]
        if s == sub_string:
            count += 1
    return count
```

## Mutations

```python
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
```

## String Formatting

```python
def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1, number+1):
        d = str(i).rjust(w,' ')
        o = str(oct(i)[2:]).rjust(w,' ')
        h = str(hex(i)[2:].upper()).rjust(w,' ')
        b = str(bin(i)[2:]).rjust(w,' ')
        print(' '.join([d, o, h, b]))
```

## String Split and Join

```python
def split_and_join(line):
    return '-'.join(line.split(' '))
```

## String Validators

```python
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
```

## sWAP cASE

```python
def swap_case(s):
    return s.swapcase()
```

```python
def swap_case(s):
    return ''.join(i.lower() if i.isupper() else i.upper() for i in s)
```

## Text Alignment

```python
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
```

## Text Wrap

```python
def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
```

```python
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))
```

## What's Your Name?

```python
def print_full_name(first, last):
    print('Hello %s %s! You just delved into python.' % (first, last))
```

# Medium

## Merge the Tools!

```python
def merge_the_tools(string, k):
    for i in range(0, len(string), k):    
        print(''.join(dict.fromkeys(string[i:i+k])))
```

## The Minion Game

```python
vowels = 'AEIOU'

def minion_game(string):
    s = k = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            k += (len(string)-i)
        else:
            s += (len(string)-i)
    
    if s > k:
        print('Stuart '+str(s))
    elif k > s:
        print('Kevin '+str(k))
    else:
        print('Draw')
```