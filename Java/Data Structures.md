# Easy

## Java 1D Array

```java

```

## Java 2D Array

```java

```

## Java Arraylist

```java

```

## Java BitSet

```java

```

## Java Generics

```java

```

## Java Hashset

```java

```

## Java List

```java

```

## Java Map

```java

```

## Java Sort

```java

```

## Java Subarray

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static boolean negTotal(int[] input) {
        int total = 0;
        for (int i : input) total += i;
        return total <= 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int output = 0;
        // i: len of sub array
        // j: start index of sub array
        // k: index within sub array
        for (int i = 1; i < n; i++) {
            int[] subarray = new int[n];
            for (int j = 0; j < n-i+1; j++) {
                for (int k = 0; k < i; k++) {
                    subarray[k] = arr[j+k];
                }
                if (negTotal(subarray)) output++;
            }
        }
        System.out.println(output);
    }
}
```

# Medium

## Java 1D Array (Part 2)

```java

```

## Java Comparator

```java

```

## Java Dequeue

```java

```

## Java Priority Queue

```java

```

## Java Stack

```java

```