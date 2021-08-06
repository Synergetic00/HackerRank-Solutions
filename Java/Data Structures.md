# Easy

## Java 1D Array

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
	   
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        sc.close();

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
        
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        
        for (int i = 0; i < h; i++) {
            int w = sc.nextInt();
            arr.add(new ArrayList<Integer>());
            for (int j = 0; j < w; j++) {
                arr.get(i).add(sc.nextInt());
            }
        }
        
        int tests = sc.nextInt();
        for (int i = 0; i < tests; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            try {
                System.out.println(arr.get(x-1).get(y-1));
            } catch (Exception e) {
                System.out.println("ERROR!");
            }
        }

        sc.close();
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

        sc.close();
    }
}
```

## Java Generics

```java
import java.io.IOException;
import java.lang.reflect.Method;

class Printer {
    public <T> void printArray(T[] arr) {
        for (T item : arr) {
            System.out.println(item);
        }
    }
}

public class Solution {

    public static void main( String args[] ) {
        Printer myPrinter = new Printer();
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = {"Hello", "World"};
        myPrinter.printArray(intArray);
        myPrinter.printArray(stringArray);
        int count = 0;

        for (Method method : Printer.class.getDeclaredMethods()) {
            String name = method.getName();
            if(name.equals("printArray")) count++;
        }

        if(count > 1) {
            System.out.println("Method overloading is not allowed!");
        }
    }
}
```

## Java Hashset

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        HashSet<String> hashSet = new HashSet<String>();
        
        for (int i = 0; i < T; i++) {
            String left = sc.next();
            String right = sc.next();
            hashSet.add(left+" "+right);
            System.out.println(hashSet.size());
        }
        
        sc.close();
    }
}
```

## Java List

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        List<Integer> list = new ArrayList<Integer>(N);
        for (int i = 0; i < N; i++) {
            list.add(sc.nextInt());
        }
        
        int Q = sc.nextInt();
        for (int i = 0; i < Q; i++) {
            String command = sc.next();
            switch (command) {
                case "Insert": {
                    int index = sc.nextInt();
                    int value = sc.nextInt();
                    list.add(index, value);
                    break;
                }
                case "Delete": {
                    int index = sc.nextInt();
                    list.remove(index);
                    break;
                }
            }
        }
        
        sc.close();
        
        for (Integer i : list) {
            System.out.print(i + " ");
        }
    }
}
```

## Java Map

```java
import java.util.*;
import java.io.*;

class Solution {
    
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            int phone   = Integer.valueOf(br.readLine());
            map.put(name, phone);
        }
        
        String s;
        while((s = br.readLine()) != null) {
            if (map.containsKey(s)) {
                System.out.println(s + "=" + map.get(s));
            } else {
                System.out.println("Not found");
            }
        }
        
        br.close();
	}
}
```

## Java Sort

```java
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        List<Student> students = new ArrayList<Student>();
    
        for (int i = 0; i < N; i++) {
            int id = sc.nextInt();
            String name = sc.next();
            double cgpa = sc.nextDouble();
            Student student = new Student(id, name, cgpa);
            students.add(student);
        }
        
        Collections.sort(students);
        
        for (Student student : students) {
            System.out.println(student.getName());
        }
    
        sc.close();
    }
}

class Student implements Comparable<Student> {
    
    int id;
    String name;
    double cgpa;
    
    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }
    
    public String getName() {
        return name;
    }
    
    public int compareTo(Student other) {
        if (this.cgpa == other.cgpa) {
            if (this.name.equals(other.name)) {
                return this.id - other.id;
            } else {
                return this.name.compareTo(other.name);
            }
        } else {
            return (this.cgpa < other.cgpa) ? 1 : -1;
        }
    }
    
}
```

## Java Subarray

```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] output = new int[n];
        for (int i = 0; i < n; i++) {
            output[i] = sc.nextInt();
        }
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (negSub(output, i, j)) count++;
            }
        }
        
        System.out.println(count);
        sc.close();
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
import java.util.*;
    
public class Solution {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<Integer>();
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        for (int i = 0; i < M-1; i++) {
            int num = sc.nextInt();
            deque.addLast(num);
        }

        long max = 0;

        for (int i = 0; i < N-M+1; i++) {
            int num = sc.nextInt();
            deque.addLast(num);
            long unique = deque.stream().distinct().count();
            if (unique > max) max = unique;
            deque.removeFirst();
        }

        System.out.println(max);
        sc.close();
    }
}
```

## Java Priority Queue

```java

```

## Java Stack

```java
import java.util.*;

class Solution {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNext()) {
            String input = sc.next();
            System.out.println(isBalanced(input));
        }    
        
        sc.close();
    }
    
    public static boolean isBalanced(String input) {
            Stack<Character> stack = new Stack<Character>();

            for (char c : input.toCharArray()) {
                if (c == '{' || c == '[' || c == '(') {
                    stack.push(c);
                } else {
                    if (stack.isEmpty()) return false;
                    if (stack.peek() != getOther(c)) return false;
                    else stack.pop();
                }
            }
        
            return stack.isEmpty();
    }
    
    public static char getOther(char input) {
        switch (input) {
            case '{': return '}';
            case '[': return ']';
            case '(': return ')';
            case '}': return '{';
            case ']': return '[';
            case ')': return '(';
            default: return input;
        }
    }
}
```