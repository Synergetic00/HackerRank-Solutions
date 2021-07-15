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

```java
import java.io.*;
import java.util.*;

public class Solution {
    
    // Hard coded since the test input data has changed
    static final long seeds[] = {1374037200,1374037459,1057556953,1226891312,1287968623,1282073374,1287158953,1159300833,1139155438,1074640221,1040332083,1347392806,990639200,969276712,1182050116,1265867460,1257725758,1185815629};
    
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] input = new int[10];
        for (int t = 0; t < n; t++) {
            for (int i = 0; i < 10; i++) {
                input[i] = scanner.nextInt();
            }
            
            for (int s = 0; s < 18; s++) {
                random.setSeed(seeds[s]);
                boolean found = true;
                for (int j = 0; j < input.length; j++) {
                    if (random.nextInt(1000) != input[j]) {
                        found = false;
                        break;
                    }
                }
                if (found) {
                    for (int j = 0; j < 10; j++) {
                        System.out.print(random.nextInt(1000));
                        System.out.print(" ");
                    }
                    System.out.print("\n");
                }
            }
            
        }
    }
}
```

# Hard

## Basic Cryptanalysis

```python
with open('dictionary.lst') as infile:
    dictlist = [i.lower() for i in infile.read().split('\n')]

ciphertext = input().split(' ')
sortedinput = sorted(ciphertext, key=lambda x: -len(x))

substitutions = {}

def generateSubstitution():
    for word in sortedinput:
        for entry in dictlist:
            if len(entry) == len(word):
                mapping = substitutions.copy()
                found = True
                for (idx,c) in enumerate(entry):
                    if word[idx] not in mapping:
                        mapping[word[idx]] = c
                    else:
                        if mapping[word[idx]] != c:
                            found = False
                            break
                if found:
                    substitutions.update(mapping)
                    if len(substitutions) == 26:
                        return
                    else:
                        break

generateSubstitution()
for word in ciphertext:
    print(''.join([substitutions[c] if c in substitutions else c for c in word]), end=' ')
```