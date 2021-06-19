# Day 0: Hello, World.

## Java

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	public static void main(String[] args) {
        // Create a Scanner object to read input from stdin.
		Scanner scan = new Scanner(System.in);

		// Read a full line of input from stdin and save it to our variable, inputString.
		String inputString = scan.nextLine();

		// Close the scanner object, because we've finished reading
        // all of the input from stdin needed for this challenge.
		scan.close();

		// Print a string literal saying "Hello, World." to stdout.
		System.out.println("Hello, World.");

	    // TODO: Write a line of code here that prints the contents of inputString to stdout.
        System.out.println(inputString);
	}
}
```

## C++

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    // Declare a variable named 'input_string' to hold our input.
    string input_string;

    // Read a full line of input from stdin (cin) and save it to our variable, input_string.
    getline(cin, input_string);

    // Print a string literal saying "Hello, World." to stdout using cout.
    cout << "Hello, World." << endl;

    // TODO: Write a line of code here that prints the contents of input_string to stdout.
    cout << input_string;

    return 0;
}
```

## Python 2

```python
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
inputString = raw_input()

# Print a string literal saying "Hello, World." to stdout.
print 'Hello, World.'

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print inputString
```

## Python 3

```python
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)
```

# C

```cpp
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    // Declare a variable named 'input_string' to hold our input.
    char input_string[105];

    // Read a full line of input from stdin and save it to our variable, input_string.
    scanf("%[^\n]", input_string);

    // Print a string literal saying "Hello, World." to stdout using printf.
    printf("Hello, World.\n");

    // TODO: Write a line of code here that prints the contents of input_string to stdout.
    printf("%s", input_string);

    return 0;
}
```

## C#

```cs
using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        // Declare a variable named 'inputString' to hold our input.
        String inputString;

        // Read a full line of input from stdin (cin) and save it to our variable, input_string.
        inputString = Console.ReadLine();

        // Print a string literal saying "Hello, World." to stdout using cout.
        Console.WriteLine("Hello, World.");

        // TODO: Write a line of code here that prints the contents of input_string to stdout.
        Console.WriteLine(inputString);
    }
}
```

## PHP

```php
<?php
$_fp = fopen("php://stdin", "r");

$inputString = fgets($_fp); // get a line of input from stdin and save it to our variable

// Your first line of output goes here
print("Hello, World.\n");

// Write the second line of output
print($inputString);

fclose($_fp);
?>
```

## Ruby

```ruby
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = gets

# Print a string literal saying "Hello, World." to stdout.
puts 'Hello, World.'

# TODO: Write a line of code here that prints the contents of input_string to stdout.
puts input_string
```

## Perl

```perl
my $inputString = <STDIN>; # get a line of input from stdin and save it to our variable

# Your first line of output goes here
print "Hello, World.\n";

# Write the second line of output
print "${inputString}"
```

## Haskell

```
-- Enter your code here. Read input from STDIN. Print output to STDOUT
import System.IO

main = do
    inputStr <- getLine
    putStrLn "Hello, World."
    putStrLn inputStr
```

# Day 1: Data Types
# Day 2: Operators
# Day 3: Intro to Conditional Statements
# Day 4: Class vs. Instance
# Day 5: Loops
# Day 6: Let's Review
# Day 7: Arrays
# Day 8: Dictionaries and Maps
# Day 9: Recursion 3
# Day 10: Binary Numbers
# Day 11: 2D Arrays
# Day 12: Inheritance
# Day 13: Abstract Classes
# Day 14: Scope
# Day 15: Linked List
# Day 16: Exceptions - String to Integer
# Day 17: More Exceptions
# Day 18: Queues and Stacks
# Day 19: Interfaces
# Day 20: Sorting
# Day 21: Generics
# Day 22: Binary Search Trees
# Day 23: BST Level-Order Traversal
# Day 24: More Linked Lists
# Day 25: Running Time and Complexity
# Day 26: Nested Logic
# Day 27: Testing
# Day 28: RegEx, Patterns, and Intro to Databases
# Day 29: Bitwise AND