# Easy

## Covariant Return Types

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//Complete the classes below
class Flower {
    String whatsYourName() {
        return "I have many names and types.";
    }
}

class Jasmine extends Flower {
    @Override
    String whatsYourName() {
        return "Jasmine";
    }
}

class Lily extends Flower {
    @Override
    String whatsYourName() {
        return "Lily";
    }
}

class Lotus extends Flower {
    @Override
    String whatsYourName() {
        return "Lotus";
    }
}

class Region {
    Flower yourNationalFlower() {
        return new Flower();
    }
}

class WestBengal extends Region {
    @Override
    Jasmine yourNationalFlower() {
        return new Jasmine();
    }
}

class Karnataka extends Region {
    @Override
    Lotus yourNationalFlower() {
        return new Lotus();
    }
}

class AndhraPradesh extends Region {
    @Override
    Lily yourNationalFlower() {
        return new Lily();
    }
}


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s = reader.readLine().trim();
        Region region = null;
        switch (s) {
            case "WestBengal":
                region = new WestBengal();
                break;
            case "AndhraPradesh":
                region = new AndhraPradesh();
                break;
        }
        Flower flower = region.yourNationalFlower();
        System.out.println(flower.whatsYourName());
    }
}
```

## Java Factory Pattern

```java
import java.util.*;
import java.security.*;

interface Food {
	public String getType();
}

class Pizza implements Food {
	public String getType() {
	    return "Someone ordered a Fast Food!";
	}
}

class Cake implements Food {
	public String getType() {
	    return "Someone ordered a Dessert!";
	}
}

class FoodFactory {
	public Food getFood(String order) {
        switch (order.toLowerCase()) {
            case "pizza": return new Pizza();
            case "cake" : return new Cake();
            default : return null;
        }          
    }
}

public class Solution {

	public static void main(String[] args) {
		Do_Not_Terminate.forbidExit();

		try {
			Scanner sc = new Scanner(System.in);
			FoodFactory foodFactory = new FoodFactory();
			Food food = foodFactory.getFood(sc.nextLine());		
			System.out.println("The factory returned " + food.getClass());
			System.out.println(food.getType());
		} catch (Do_Not_Terminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	}
}

class Do_Not_Terminate {
	public static class ExitTrappedException extends SecurityException {
        private static final long serialVersionUID = 1L;
	}
	 
	public static void forbidExit() {
	    final SecurityManager securityManager = new SecurityManager() {
	        @Override
	        public void checkPermission(Permission permission) {
	            if (permission.getName().contains("exitVM")) {
	                throw new ExitTrappedException();
	            }
	        }
	    };
	    System.setSecurityManager(securityManager);
	}
}
```

## Java Reflection - Attributes

```java
public class Solution {

        public static void main(String[] args) {
            Class student = Student.class;
            Method[] methods = student.getDeclaredMethods();
            ArrayList<String> methodList = new ArrayList<>();
            for(Method m : methods) {
                methodList.add(m.getName());
            }
            Collections.sort(methodList);
            for(String name: methodList) {
                System.out.println(name);
            }
        }
    }
```

## Java Singleton Pattern

```java
import java.util.Scanner;
import java.lang.reflect.Constructor;

class Singleton {
    private volatile static Singleton instance;
    public static String str;
    private Singleton() {}
    
    static Singleton getSingleInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

## Java Varargs - Simple Addition

```java
import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Add {

    public void add(int... args) {
        String output = "", operator = "";
        int sum = 0;
        for (int i : args) {
            output += operator + i;
            operator = "+";
            sum += i;
        }
        output += "=" + sum;
        System.out.println(output);
    }
}


public class Solution {

    public static void main(String[] args) {
        try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int n1 = Integer.parseInt(br.readLine());
			int n2 = Integer.parseInt(br.readLine());
			int n3 = Integer.parseInt(br.readLine());
			int n4 = Integer.parseInt(br.readLine());
			int n5 = Integer.parseInt(br.readLine());
			int n6 = Integer.parseInt(br.readLine());
			Add ob = new Add();
			ob.add(n1,n2);
			ob.add(n1,n2,n3);
			ob.add(n1,n2,n3,n4,n5);	
			ob.add(n1,n2,n3,n4,n5,n6);
			Method[] methods = Add.class.getDeclaredMethods();
			Set<String> set = new HashSet<>();
			boolean overload=false;
			for (int i = 0; i < methods.length; i++) {
				if(set.contains(methods[i].getName())) {
					overload = true;
					break;
				}
				set.add(methods[i].getName());
			}
			if (overload) {
				throw new Exception("Overloading not allowed");
			}
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}
```

# Medium

## Can You Access?

```java
import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.util.regex.*;
import java.security.*;


public class Solution {

	public static void main(String[] args) throws Exception {
		DoNotTerminate.forbidExit();	

		try{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int num = Integer.parseInt(br.readLine().trim());
			Object o;// Must be used to hold the reference of the instance of the class Solution.Inner.Private
        o = new Inner().new Private();
        System.out.println(num + " is " + ((Inner.Private)(o)).powerof2(num));
		System.out.println("An instance of class: " + o.getClass().getCanonicalName() + " has been created");
		
		}//end of try
		
		catch (DoNotTerminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	}//end of main
	static class Inner{
		private class Private{
			private String powerof2(int num){
				return ((num&num-1)==0)?"power of 2":"not a power of 2";
			}
		}
	}//end of Inner
	
}//end of Solution

class DoNotTerminate { //This class prevents exit(0)
	 
    public static class ExitTrappedException extends SecurityException {

		private static final long serialVersionUID = 1L;
    }
 
    public static void forbidExit() {
        final SecurityManager securityManager = new SecurityManager() {
            @Override
            public void checkPermission(Permission permission) {
                if (permission.getName().contains("exitVM")) {
                    throw new ExitTrappedException();
                }
            }
        };
        System.setSecurityManager(securityManager);
    }
}
```

## Java Annotations

```java
import java.lang.annotation.*;
import java.lang.reflect.*;
import java.util.*;

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface FamilyBudget {
   String userRole() default "GUEST";
   int budgetLimit() default 0;
    
}

class FamilyMember {
   @FamilyBudget(userRole = "SENIOR", budgetLimit = 100)
   public void seniorMember(int budget, int moneySpend) {
      System.out.println("Senior Member");
      System.out.println("Spend: " + moneySpend);
      System.out.println("Budget Left: " + (budget - moneySpend));
   }
 
   @FamilyBudget(userRole = "JUNIOR", budgetLimit = 50)
   public void juniorUser(int budget, int moneySpend) {
      System.out.println("Junior Member");
      System.out.println("Spend: " + moneySpend);
      System.out.println("Budget Left: " + (budget - moneySpend));
   }
}

public class Solution {
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while (testCases > 0) {
         String role = in.next();
         int spend = in.nextInt();
         try {
            Class annotatedClass = FamilyMember.class;
            Method[] methods = annotatedClass.getMethods();
            for (Method method : methods) {
               if (method.isAnnotationPresent(FamilyBudget.class)) {
                  FamilyBudget family = method
                        .getAnnotation(FamilyBudget.class);
                  String userRole = family.userRole();
                  int budgetLimit = family.budgetLimit();
                  if (userRole.equals(role)) {
                     if(budgetLimit >= spend){
                        method.invoke(FamilyMember.class.newInstance(),
                              budgetLimit, spend);
                     }else{
                        System.out.println("Budget Limit Over");
                     }
                  }
               }
            }
         } catch (Exception e) {
            e.printStackTrace();
         }
         testCases--;
      }
   }
}
```

## Java Lambda Expressions

```java
import java.io.*;
import java.util.*;
interface PerformOperation {
 boolean check(int a);
}
class MyMath {
 public static boolean checker(PerformOperation p, int num) {
  return p.check(num);
 }

    public PerformOperation isOdd(){
        return (int a) -> a % 2 != 0;
    }
    
    public PerformOperation isPrime(){
        return (int a) -> java.math.BigInteger.valueOf(a).isProbablePrime(100);
    }
    
    public PerformOperation isPalindrome(){
        return (int a) ->  Integer.toString(a).equals(new StringBuilder(Integer.toString(a)).reverse().toString());
    }
    
}

public class Solution {

 public static void main(String[] args) throws IOException {
  MyMath ob = new MyMath();
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  int T = Integer.parseInt(br.readLine());
  PerformOperation op;
  boolean ret = false;
  String ans = null;
  while (T--> 0) {
   String s = br.readLine().trim();
   StringTokenizer st = new StringTokenizer(s);
   int ch = Integer.parseInt(st.nextToken());
   int num = Integer.parseInt(st.nextToken());
   if (ch == 1) {
    op = ob.isOdd();
    ret = ob.checker(op, num);
    ans = (ret) ? "ODD" : "EVEN";
   } else if (ch == 2) {
    op = ob.isPrime();
    ret = ob.checker(op, num);
    ans = (ret) ? "PRIME" : "COMPOSITE";
   } else if (ch == 3) {
    op = ob.isPalindrome();
    ret = ob.checker(op, num);
    ans = (ret) ? "PALINDROME" : "NOT PALINDROME";

   }
   System.out.println(ans);
  }
 }
}
```

## Java MD5

```java
import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Solution {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        /* Read and save the input String */
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        scan.close();
        
        /* Encode the String using MD5 */
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(str.getBytes());
        byte[] digest = md.digest();
        
        /* Print the encoded value in hexadecimal */
        for (byte b : digest) {
            System.out.format("%02x", b);
        }
    }
}
```

## Java SHA-256

```java
import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Solution {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        /* Read and save the input String */
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        scan.close();
        
        /* Encode the String using SHA-256 */
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(str.getBytes());
        byte[] digest = md.digest();
        
        /* Print the encoded value in hexadecimal */
        for (byte b : digest) {
            System.out.format("%02x", b);
        }
    }
}
```

## Java Visitor Pattern

```java
import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.util.ArrayList;
import java.util.Scanner;

enum Color {
    RED, GREEN
}

abstract class Tree {

    private int value;
    private Color color;
    private int depth;

    public Tree(int value, Color color, int depth) {
        this.value = value;
        this.color = color;
        this.depth = depth;
    }

    public int getValue() {
        return value;
    }

    public Color getColor() {
        return color;
    }

    public int getDepth() {
        return depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree {

    private ArrayList<Tree> children = new ArrayList<>();

    public TreeNode(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitNode(this);

        for (Tree child : children) {
            child.accept(visitor);
        }
    }

    public void addChild(Tree child) {
        children.add(child);
    }
}

class TreeLeaf extends Tree {

    public TreeLeaf(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis
{
    public abstract int getResult();
    public abstract void visitNode(TreeNode node);
    public abstract void visitLeaf(TreeLeaf leaf);

}

class SumInLeavesVisitor extends TreeVis {
    private int result = 0;

    public int getResult() {
        return result;
    }

    public void visitNode(TreeNode node) {
        // do nothing
    }

    public void visitLeaf(TreeLeaf leaf) {
        result += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private long result = 1;
    private final int M = 1000000007;

    public int getResult() {
        return (int) result;
    }

    public void visitNode(TreeNode node) {
        if (node.getColor() == Color.RED) {
            result = (result * node.getValue()) % M;
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor() == Color.RED) {
            result = (result * leaf.getValue()) % M;
        }
    }
}

class FancyVisitor extends TreeVis {
    private int nonLeafEvenDepthSum = 0;
    private int greenLeavesSum = 0;

    public int getResult() {
        return Math.abs(nonLeafEvenDepthSum - greenLeavesSum);
    }

    public void visitNode(TreeNode node) {
        if (node.getDepth() % 2 == 0) {
            nonLeafEvenDepthSum += node.getValue();
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor() == Color.GREEN) {
            greenLeavesSum += leaf.getValue();
        }
    }
}

public class Solution {
    private static int [] values;
    private static Color [] colors;
    private static HashMap<Integer, HashSet<Integer>> map;
    
    public static Tree solve() {
        Scanner scan = new Scanner(System.in);
        int numNodes = scan.nextInt();
        
        /* Read and save nodes and colors */
        values = new int[numNodes];
        colors = new Color[numNodes];
        map = new HashMap<>(numNodes);
        for (int i = 0; i < numNodes; i++) {
            values[i] = scan.nextInt();
        }
        for (int i = 0; i < numNodes; i++) {
            colors[i] = scan.nextInt() == 0 ? Color.RED : Color.GREEN;
        }
        
        /* Save edges */
        for (int i = 0; i < numNodes - 1; i++) {
            int u = scan.nextInt();
            int v = scan.nextInt();
            
            /* Edges are undirected: Add 1st direction */
            HashSet<Integer> uNeighbors = map.get(u);
            if (uNeighbors == null) {                
                uNeighbors = new HashSet<>();
                map.put(u, uNeighbors);
            }
            uNeighbors.add(v);
            
            /* Edges are undirected: Add 2nd direction */
            HashSet<Integer> vNeighbors = map.get(v);
            if (vNeighbors == null) {
                vNeighbors = new HashSet<>();
                map.put(v, vNeighbors);
            }
            vNeighbors.add(u);
        }
        scan.close();
        
        /* Handle 1-node tree */
        if (numNodes == 1) {
            return new TreeLeaf(values[0], colors[0], 0);
        }
        
        /* Create Tree */
        TreeNode root = new TreeNode(values[0], colors[0], 0);
        addChildren(root, 1);
        return root;
    }

    /* Recursively adds children of a TreeNode */
    private static void addChildren(TreeNode parent, Integer parentNum) {
        /* Get HashSet of children and loop through them */
        for (Integer treeNum : map.get(parentNum)) {
            map.get(treeNum).remove(parentNum); // removes the opposite arrow direction
            
            /* Add child */
            HashSet<Integer> grandChildren = map.get(treeNum);
            boolean childHasChild = (grandChildren != null && !grandChildren.isEmpty());
            Tree tree;
            if (childHasChild) {
                tree = new TreeNode(values[treeNum - 1], colors[treeNum - 1], parent.getDepth() + 1);
            } else {
                tree = new TreeLeaf(values[treeNum - 1], colors[treeNum - 1], parent.getDepth() + 1);
            }
            parent.addChild(tree);

            /* Recurse if necessary */
            if (tree instanceof TreeNode) {
                addChildren((TreeNode) tree, treeNum);
            }
        }
    }


    public static void main(String[] args) {
      	Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	System.out.println(res3);
	}
}
```

## Prime Checker

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;
import static java.lang.System.in;

class Prime {
    void checkPrime(int... numbers) {
        for (int num : numbers) {
            if (isPrime(num)) {
                System.out.print(num + " ");
            }
        }
        System.out.println();
    }
    
    boolean isPrime(int n) {
        if (n < 2) return false;
        boolean flag = true;
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}

public class Solution {

	public static void main(String[] args) {
		try{
		BufferedReader br=new BufferedReader(new InputStreamReader(in));
		int n1=Integer.parseInt(br.readLine());
		int n2=Integer.parseInt(br.readLine());
		int n3=Integer.parseInt(br.readLine());
		int n4=Integer.parseInt(br.readLine());
		int n5=Integer.parseInt(br.readLine());
		Prime ob=new Prime();
		ob.checkPrime(n1);
		ob.checkPrime(n1,n2);
		ob.checkPrime(n1,n2,n3);
		ob.checkPrime(n1,n2,n3,n4,n5);	
		Method[] methods=Prime.class.getDeclaredMethods();
		Set<String> set=new HashSet<>();
		boolean overload=false;
		for(int i=0;i<methods.length;i++)
		{
			if(set.contains(methods[i].getName()))
			{
				overload=true;
				break;
			}
			set.add(methods[i].getName());
			
		}
		if(overload)
		{
			throw new Exception("Overloading not allowed");
		}
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
	
}


```