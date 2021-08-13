## Day 0: Mean, Median, and Mode

```python
size = int(input())
numbers = list(map(int, input().split()))
ordered = sorted(numbers)

mean = sum(numbers) / size

index = int(size/2)

if index == size/2:
    median = (ordered[index] + ordered[index-1]) / 2 
else:
    median = ordered[index]

highest = 0

for num in sorted(set(numbers)):
    if (numbers.count(num) > highest):
        highest = numbers.count(num)
        mode = num

print(mean)
print(median)
print(mode)
```

## Day 0: Weighted Mean

```python
def weightedMean(X, W):
    XW = [X[i] * W[i] for i in range(len(X))]
    output = round(sum(XW)/sum(W), 1)
    print(output)
```

## Day 1:Interquartile Range

```python
```

## Day 1: Standard Deviation

```python
def stdDev(arr):
    mean = sum(arr) / len(arr)
    total = [((num - mean) ** 2) for num in arr]
    output = math.sqrt(sum(total) / len(total))
    print(output)
```

## Day 1: Quartiles

```python
```

## Day 2: Basic Probability

```python
```

## Day 2: More Dice

```python
```

## Day 2: Compound Event Probability

```python
```

## Day 3: Conditional Probability

```python
```

## Day 3: Cards of the Same Suit

```python
```

## Day 3: Drawing Marbles

```python
```

## Day 4: Binomial Distribution I

```python
```

## Day 4: Binomial Distribution II

```python
```

## Day 4: Geometric Distribution I

```python
```

## Day 4: Geometric Distribution II

```python
```

## Day 5: Poisson Distribution I

```python
```

## Day 5: Poisson Distribution II

```python
```

## Day 5: Normal Distribution I

```python
```

## Day 5: Normal Distribution II

```python
```

## Day 6: The Central Limit Theorem I

```python
```

## Day 6: The Central Limit Theorem II

```python
```

## Day 6: The Central Limit Theorem III

```python
```

## Day 7: Pearson Correlation Coefficient I

```python
```

## Day 7: Spearman's Rank Correlation Coefficient

```python
```

## Day 8: Least Square Regression Line

```python
```

## Day 8: Pearson Correlation Coefficient II

```python
```

## Day 9: Multiple Linear Regression

```python
```