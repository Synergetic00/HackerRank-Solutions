# Easy

## Java 1D Array

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
	   
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scan.nextInt();
        }

        scan.close();

        // Prints each sequential element in array a
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
```

## Java 2D Array

```java
import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        
        System.out.println(hourglassSum(arr));
    }
    
    public static int hourglassSum(List<List<Integer>> arr) {
        int output = getHourglass(arr, 1, 1);
        for (int y = 1; y < arr.size()-1; y++) {
            int width = arr.get(y).size();
            for (int x = 1; x < width-1; x++) {
                int sum = getHourglass(arr, x, y);
                if (sum > output) output = sum;
            }
        }
        return output;
    }
    
    public static int getHourglass(List<List<Integer>> arr, int x, int y) {
        int total = arr.get(y).get(x);
        for (int i = 0; i < 3; i++) {
            total += arr.get(y-1).get(x-1+i);
            total += arr.get(y+1).get(x-1+i);
        }
        return total;
    }
}
```

## Java Arraylist

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        ArrayList<ArrayList<Integer>> arr;
        arr = new ArrayList<ArrayList<Integer>>();
        
        Scanner scan = new Scanner(System.in);
        int h = scan.nextInt();
        
        for (int i = 0; i < h; i++) {
            int w = scan.nextInt();
            arr.add(new ArrayList<Integer>());
            for (int j = 0; j < w; j++) {
                arr.get(i).add(scan.nextInt());
            }
        }
        
        int tests = scan.nextInt();
        for (int i = 0; i < tests; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            
            try {
                System.out.println(arr.get(x-1).get(y-1));
            } catch (Exception e) {
                System.out.println("ERROR!");
            }
        } 
    }
}
```

## Java BitSet

```java
import java.util.BitSet;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        BitSet[] sets = new BitSet[2];
        for (int i = 0; i < sets.length; i++) {
            sets[i] = new BitSet(n);
        }
        
        for (int i = 0; i < m; i++) {
            String operator = sc.next();
            int x = sc.nextInt() - 1;
            int y = sc.nextInt() - 1;
            
            switch (operator) {
                case "AND":
                    sets[x].and(sets[y]);
                    break;
                case "OR":
                    sets[x].or(sets[y]);
                    break;
                case "XOR":
                    sets[x].xor(sets[y]);
                    break;
                case "FLIP":
                    sets[x].flip(y+1);
                    break;
                case "SET":
                    sets[x].set(y+1);
                    break;
            }
            
            System.out.println(sets[0].cardinality() + " " + sets[1].cardinality());
        }
    }
}
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

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] output = new int[n];
        for (int i = 0; i < n; i++) {
            output[i] = scan.nextInt();
        }
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (negSub(output, i, j)) count++;
            }
        }
        
        System.out.println(count);
    }
    
    public static boolean negSub(int[] arr, int start, int end) {
        int total = 0;
        for (int i = start; i <= end; i++) {
            total += arr[i];
        }
        return total < 0;
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