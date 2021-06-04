# Easy

## Java Anagrams

```java
import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;

        String la = a.toLowerCase();
        String lb = b.toLowerCase();

        for (char ch = 'a'; ch <= 'z'; ch++) {
            int count = 0;
            for (char ca : la.toCharArray()) {
                if (ca == ch) count++;
            }
            for (char cb : lb.toCharArray()) {
                if (cb == ch) count--;
            }
            if (count != 0) return false;
        }
        return true;
    }

  public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
```

## Java String Reverse

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();

        boolean palindrome = true;
        for (int i = 0; i < A.length()/2+1; i++) {
            char first = A.charAt(i);
            char last = A.charAt(A.length()-i-1);
            if (first != last) palindrome = false;
        }

        System.out.println((palindrome) ? "Yes" : "No");
    }
}
```

## Java String Tokens

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        if (s.length() != 0) {
            String[] arr = s.split("[!,?._'@ ]+");
            System.out.println(arr.length);
            for (int i = 0; i < arr.length; i++) {
                System.out.println(arr[i]);
            }
        } else {
            System.out.println("0");
        }
        scan.close();
    }
}
```

## Java Strings Introduction

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();

        System.out.println(A.length() + B.length());
        System.out.println((A.compareTo(B) > 0 ? "Yes" : "No"));

        String upcA = A.substring(0, 1).toUpperCase() + A.substring(1);
        String upcB = B.substring(0, 1).toUpperCase() + B.substring(1);

        System.out.println(upcA + " " + upcB);
    }
}
```

## Java Substring

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();

        System.out.println(S.substring(start, end));
    }
}
```

## Java Substring Comparisons

```java
import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = "";

        for (int i = 0; i < s.length()-k+1; i++) {
            String substr = s.substring(i, i+k);

            if (substr.compareTo(smallest) < 0) smallest = substr;
            if (substr.compareTo(largest) > 0) largest = substr;
        }

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'

        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
```

## Pattern Syntax Checker

```java
import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
            try {
                Pattern.compile(pattern);
                System.out.println("Valid");
            } catch(PatternSyntaxException e) {
                System.out.println("Invalid");
            }
          	testCases--;
		}
	}
}
```

## Valid Username Regular Expression

```java
import java.util.Scanner;

class UsernameValidator {
    public static final String regularExpression = "^[a-zA-Z]\\w{7,29}$";
}


public class Solution {
    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
}
```

# Medium

## Java Regex

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class Solution{

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}

class MyRegex {
    String value = "([0-9]|[0-9][0-9]|(0|1)[0-9][0-9]|2[0-4][0-9]|25[0-5])";
    public String pattern = value + "." + value + "." + value + "." + value;
}
```

## Java Regex 2 - Duplicate Words

```java
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DuplicateWords {

    public static void main(String[] args) {

        String regex = "\\b([a-z]|[A-Z]+)(\\s+\\1\\b)+";
        Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);

        Scanner in = new Scanner(System.in);
        int numSentences = Integer.parseInt(in.nextLine());

        while (numSentences-- > 0) {
            String input = in.nextLine();

            Matcher m = p.matcher(input);

            // Check for subsequences of input that match the compiled pattern
            while (m.find()) {
                input = input.replaceAll(m.group(), m.group(1));
            }

            // Prints the modified sentence.
            System.out.println(input);
        }

        in.close();
    }
}
```

## Tag Content Extractor

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{

	public static void main(String[] args){

		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String line = in.nextLine();

            boolean matchFound = false;
            Pattern r = Pattern.compile("<(.+)>([^<]+)</\\1>");
            Matcher m = r.matcher(line);

            while (m.find()) {
                System.out.println(m.group(2));
                matchFound = true;
            }

            if (!matchFound) System.out.println("None");

			testCases--;
		}
	}
}
```