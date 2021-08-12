# Day 0: Hello, World.

### Ada

```rust
with Ada.Text_IO, Ada.Integer_Text_IO;
use Ada.Text_IO;

procedure Solution is
begin
    declare 
        S:String := Ada.Text_IO.Get_Line;
    begin
        Put_Line("Hello, World.");
        Put_Line(S);
    end;

end Solution;
```

### BASH

```bash
read inputString
echo 'Hello, World.'
echo $inputString
```

### C

```cpp
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char input_string[105];
    scanf("%[^\n]", input_string);
    printf("Hello, World.\n");
    printf("%s", input_string);

    return 0;
}
```

### Clojure

```clojure
(def inputStr (read-line))
(println "Hello, World.")
(println inputStr)
```

### COBOL

```cobol
IDENTIFICATION DIVISION. 
PROGRAM-ID. SOLUTION.
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION. 
FILE-CONTROL. 
SELECT SYSIN ASSIGN TO KEYBOARD ORGANIZATION LINE SEQUENTIAL.

DATA DIVISION. 
    FILE SECTION. 
    FD SYSIN. 
    01 INPUTSTRING PIC X(255).

PROCEDURE DIVISION. 
    OPEN INPUT SYSIN.
    READ SYSIN 
    CLOSE SYSIN
    DISPLAY "Hello, World.". 
    DISPLAY INPUTSTRING.
    
STOP RUN.
```

### CoffeeScript

```coffee
stdin = process.openStdin()
stdin.setEncoding 'utf8'

stdin.on 'data', (input) ->
    console.log 'Hello, World.'
    console.log input
```

### C++ / C++14 / C++20

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string input_string;
    getline(cin, input_string);
    cout << "Hello, World." << endl;
    cout << input_string;
    return 0;
}
```

### C#

```cs
using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        String inputString;
        inputString = Console.ReadLine();
        Console.WriteLine("Hello, World.");
        Console.WriteLine(inputString);
    }
}
```

### D

```d
import std.stdio;

void main() {
    string inputStr = readln();
    writeln("Hello, World.");
    writeln(inputStr);
}
```

### Elixir

```elixir
defmodule Solution do
    inputStr = IO.gets("")
    IO.puts "Hello, World."
    IO.puts "#{inputStr}"
end
```

### Erlang

```erlang
-module(solution).
-export([main/0]).

main() ->
    io:put_chars("Hello, World.\n"),
    io:put_chars(io:get_line("")).
```

### Fortran

```fortran
program hello  

    character (len = 35) :: input_string

    write(*, '(A)') "Hello, World."
    read (*, '(A)'), input_string
    write(*, '(A)') input_string

end program hello
```

### F#

```fsharp
open System

let printStr name =
    printfn "%s" name

let inputStr = Console.ReadLine()

[<EntryPoint>]
let main argv =
    printStr "Hello, World."
    printStr inputStr
    0
```

### Go

```golang
package main

import (
    "fmt"
    "bufio"
    "os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    input, _ := reader.ReadString('\n')        
    fmt.Println("Hello, World.")
    fmt.Println(input)
}
```

### Groovy

```groovy
def inputStr = System.in.newReader().readLine()
println "Hello, World."
println "${inputStr}"
```

### Haskell

```haskell
import System.IO

main = do
    inputStr <- getLine
    putStrLn "Hello, World."
    putStrLn inputStr
```

### Java 7 / 8 / 15

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String inputString = scan.nextLine();
        scan.close();
        System.out.println("Hello, World.");
        System.out.println(inputString);
    }
}
```

### JavaScript (Node.js)

```js
function processData(inputString) {
    console.log("Hello, World.");
    console.log(inputString);
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) { _input += input;});
process.stdin.on("end", function () { processData(_input); });
```

### Julia

```julia
inputStr = readline()
println("Hello, World.")
println(inputStr)
```

### Kotlin

```kotlin
import java.io.*
import java.util.*

fun main(args: Array<String>) {
    val inputStr = readLine()!!
    println("Hello, World.")
    println(inputStr)
}
```

### Lua

```lua
inputStr = io.read("*l")
print('Hello, World.')
print(inputStr)
```

### Objective-C

```c
#import <Foundation/Foundation.h>

int main (int argc, const char * argv[]) {
    @autoreleasepool {
        char inputStr[105];
        scanf("%[^\n]s", inputStr);
        printf("Hello, World.\n%s", inputStr);
    }
    return 0;
}
```

### OCaml

```ocaml
let inputStr = read_line () in
print_string "Hello, World.\n";
print_string inputStr;
```

### Pascal

```pascal
var inputStr : String;

begin
    writeln('Hello, World.');
    readln(inputStr);
    writeln(inputStr);
end.
```

### Perl

```perl
my $inputString = <STDIN>;
print "Hello, World.\n";
print "${inputString}"
```

### PHP

```php
<?php
    $_fp = fopen("php://stdin", "r");
    $inputString = fgets($_fp);
    print("Hello, World.\n");
    print($inputString);
    fclose($_fp);
?>
```

### Python 2 / Pypy 2

```python
inputString = raw_input()
print 'Hello, World.'
print inputString
```

### Python 3 / Pypy 3

```python
input_string = input()
print('Hello, World.')
print(input_string)
```

### Racket

```racket
#lang racket
(printf "Hello, World.\n")
(define inputStr (read-line))
(printf "~a\n" inputStr)
```

### Ruby

```ruby
input_string = gets
puts 'Hello, World.'
puts input_string
```

### Rust

```rust
use std::io::{self, Read};

fn main() {
    let mut guess = String::new();

    io::stdin().read_line(&mut guess);
    println!("Hello, World.");
    println!("{}", guess);
}
```

### Common Lisp (SBCL)

```lisp
(format t "Hello, World.~%")
(let ((s (read-line)))
    (format t s))
```

### Scala

```scala
object Solution {
    def main(args: Array[String]) {
        println("Hello, World.")
        val inputStr = scala.io.StdIn.readLine()
        println(inputStr)
    }
}
```

### Swift

```swift
let inputString = readLine()!
print("Hello, World.")
print(inputString)
```

### Tcl

```tcl
set str [gets stdin]
puts "Hello, World."
puts $str
```

### TypeScript

```ts
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

function main() {
    console.log("Hello, World.");
    console.log(readLine());
}
```

### VB.NET

```vb
Imports System

Module Solution
    Public Shared Sub Main()
        Dim greeting As String 
        greeting = Console.ReadLine()
        Console.WriteLine("Hello, World.")
        Console.WriteLine(greeting)
    End Sub
End Module
```

# Day 1: Data Types

### C

```cpp
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";
    
    int i2;
    double d2;
    char s2[100];
    
    scanf("%d", &i2);
    scanf("%lf", &d2);
    scanf("%*[\n] %[^\n]", s2); 

    printf("%d\n", i + i2);
    printf("%.01lf\n", d + d2);
    printf("%s%s", s, s2);

    return 0;
}
```

### C++ / C++14 / C++20

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    int i2;
    double d2;
    string s2;
    
    cin >> i2;
    cin >> d2;
    getline(cin >> ws, s2);

    cout << i + i2 << endl;
    cout << fixed << setprecision(1) << d + d2 << endl;
    cout << s + s2 << endl;

    return 0;
}
```

### C#

```cs
using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int i = 4;
        double d = 4.0;
        string s = "HackerRank ";
        
        int i2 = Convert.ToInt32(Console.ReadLine());
        double d2 = Convert.ToDouble(Console.ReadLine());
        string s2 = Console.ReadLine();
        
        Console.WriteLine(i + i2);
        Console.WriteLine("{0:.0}", d + d2);
        Console.WriteLine(s + s2);
    }
}
```

### Go

```golang
package main


import (
  "fmt"
  "os"
  "bufio"
  "strconv"
)

func main() {
  	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".
  
    var i uint64 = 4
    var d float64 = 4.0
    var s string = "HackerRank "

    scanner := bufio.NewScanner(os.Stdin)

    scanner.Scan()
    i2, _ := strconv.ParseUint(scanner.Text(),10,64)
    scanner.Scan()
    d2, _ := strconv.ParseFloat(scanner.Text(), 64)
    scanner.Scan()
    s2 := scanner.Text()

    fmt.Println(i + i2)
    fmt.Printf("%.1f\n", d + d2)
    fmt.Print(s + s2)

}
```

### Java 7 / 8 / 15

```java
```

### JavaScript (Node.js)

```js
```

### Julia

```julia
```

### Perl

```perl
```

### PHP

```php
```

### Python 2 / Pypy 2

```python
i = 4
d = 4.0
s = 'HackerRank '

i2 = int(raw_input())
d2 = float(raw_input())
s2 = raw_input()

print i + i2
print d + d2
print s + s2
```

### Python 3 / Pypy 3

```python
i = 4
d = 4.0
s = 'HackerRank '

i2 = int(input())
d2 = float(input())
s2 = input()

print(i + i2)
print(d + d2)
print(s + s2)
```

### Ruby

```ruby
```

### Scala

```scala
```

### Swift

```swift
```

### TypeScript

```ts
```

### VB.NET

```vb
```

# Day 2: Operators

### Ada

```rust
```

### BASH

```bash
```

### C

```cpp
```

### Clojure

```clojure
```

### COBOL

```cobol
```

### CoffeeScript

```coffee
```

### C++ / C++14 / C++20

```cpp
```

### C#

```cs
```

### D

```d
```

### Elixir

```elixir
```

### Fortran

```fortran
```

### F#

```fsharp
```

### Go

```golang
```

### Groovy

```groovy
```

### Haskell

```haskell
```

### Java 7 / 8 / 15

```java
```

### JavaScript (Node.js)

```js
```

### Julia

```julia
```

### Kotlin

```kotlin
```

### Lua

```lua
```

### Objective-C

```c
```

### OCaml

```ocaml
```

### Pascal

```pascal
```

### Perl

```perl
```

### PHP

```php
```

### Python 2 / Pypy 2

```python
```

### Python 3 / Pypy 3

```python
```

### Racket

```racket
```

### Ruby

```ruby
```

### Rust

```rust
```

### Common Lisp (SBCL)

```lisp
```

### Scala

```scala
```

### Swift

```swift
```

### Tcl

```tcl
```

### TypeScript

```ts
```

### VB.NET

```vb
```

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
