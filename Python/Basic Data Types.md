# Easy

## Find the Runner-Up Score!

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
```

## Finding the percentage

```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    arr = student_marks[query_name]
    print("%.2f" % (sum(arr) / len(arr)))
```

## List Comprehensions

```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n])
```

## Lists

```python
if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        
        if cmd == 'insert':
            arr.insert(int(args[0]), int(args[1]))
        elif cmd == 'print':
            print(arr)
        elif cmd == 'remove':
            arr.remove(int(args[0]))
        elif cmd == 'append':
            arr.append(int(args[0]))
        elif cmd == 'sort':
            arr.sort()
        elif cmd == 'pop':
            arr.pop()
        elif cmd == 'reverse':
            arr.reverse()
```

## Nested Lists

```python
if __name__ == '__main__':
    n = int(input())
    arr = [[input(), float(input())] for _ in range(n)]
    mark = sorted(set(row[1] for row in arr))[1]
    res = sorted([i[0] for i in arr if i[1] == mark])
    for name in res:
        print(name)
```

## Tuples

```python
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
```