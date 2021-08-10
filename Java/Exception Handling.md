# Easy

## Java Exception Handling

```java
import java.util.Scanner;

class MyCalculator {
    public long power(int n, int p) throws Exception {
        if (n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        } else if (n < 0 || p < 0) {
            throw new Exception("n or p should not be negative.");
        } else {
            return (long) Math.pow(n, p);
        }
    }
}

public class Solution {
    public static final MyCalculator calc = new MyCalculator();
    public static final Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args) {
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int p = sc.nextInt();
            
            try {
                System.out.println(calc.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }

        sc.close();
    }
}
```

## Java Exception Handling (Try-catch)

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int x = sc.nextInt();
            int y = sc.nextInt();
            System.out.println(x / y);
        } catch (ArithmeticException ae) {
            System.out.println(ae);
        } catch (InputMismatchException ime) {
            System.out.println(ime.getClass().getName());
        }
    }
}
```