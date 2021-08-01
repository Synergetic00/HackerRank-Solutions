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

## Day 1: Standard Deviation
## Day 2: Basic Probability
## Day 2: More Dice
## Day 2: Compound Event Probability
## Day 3: Conditional Probability
## Day 3: Cards of the Same Suit
## Day 3: Drawing Marbles
## Day 4: Binomial Distribution I
## Day 4: Binomial Distribution II
## Day 4: Geometric Distribution I
## Day 4: Geometric Distribution II
## Day 5: Poisson Distribution I
## Day 5: Poisson Distribution II
## Day 5: Normal Distribution I
## Day 5: Normal Distribution II
## Day 6: The Central Limit Theorem I
## Day 6: The Central Limit Theorem II
## Day 6: The Central Limit Theorem III
## Day 7: Pearson Correlation Coefficient I
## Day 7: Spearman's Rank Correlation Coefficient
## Day 8: Least Square Regression Line
## Day 8: Pearson Correlation Coefficient II
## Day 9: Multiple Linear Regression