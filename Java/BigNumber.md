# Easy

## Java BigInteger

```java
import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sa = sc.nextLine();
        String sb = sc.nextLine();
        
        BigInteger bia = new BigInteger(sa);
        BigInteger bib = new BigInteger(sb);
        
        BigInteger add = bia.add(bib);
        BigInteger mult = bia.multiply(bib);
        
        System.out.println(add);
        System.out.println(mult);
    }
}
```

## Java Primality Test

```java
import java.io.*;
import java.math.BigInteger;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String n = bufferedReader.readLine();
        
        BigInteger num = new BigInteger(n);
        String isPrime = (num.isProbablePrime(100)) ? "prime" : "not prime";
        System.out.println(isPrime);
        
        bufferedReader.close();
    }
}
```

# Medium

## Java BigDecimal

```java
import java.math.BigDecimal;
import java.util.*;

class Solution {
    public static void main(String []args) {
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();

        Arrays.sort(s, new Comparator<String>() {
            @Override
            public int compare(String val1, String val2) {
                if (val1 == null || val2 == null) {
                    return 0;
                }
                BigDecimal a = new BigDecimal(val1);
                BigDecimal b = new BigDecimal(val2);
                return -a.compareTo(b);
            }
        });

        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}
```