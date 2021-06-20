# Day 0: Hello, World.

## Java 7
## Java 8
## Java 15

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

## C++
## C++14

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

## Python 2
## Pypy 2

```python
inputString = raw_input()
print 'Hello, World.'
print inputString
```

## Python 3
## Pypy 3

```python
input_string = input()
print('Hello, World.')
print(input_string)
```

## C

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

## C#

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

## PHP

```php
<?php
    $_fp = fopen("php://stdin", "r");
    $inputString = fgets($_fp);
    print("Hello, World.\n");
    print($inputString);
    fclose($_fp);
?>
```

## Ruby

```ruby
input_string = gets
puts 'Hello, World.'
puts input_string
```

## Perl

```perl
my $inputString = <STDIN>;
print "Hello, World.\n";
print "${inputString}"
```

## Haskell

```haskell
import System.IO

main = do
    inputStr <- getLine
    putStrLn "Hello, World."
    putStrLn inputStr
```

## Clojure

```clojure
(def inputStr (read-line))
(println "Hello, World.")
(println inputStr)
```

## Scala

```scala
object Solution {
    def main(args: Array[String]) {
        println("Hello, World.")
        val inputStr = scala.io.StdIn.readLine()
        println(inputStr)
    }
}
```

## BASH

```bash
read inputString
echo 'Hello, World.'
echo $inputString
```

## Lua

```lua
inputStr = io.read("*l")
print('Hello, World.')
print(inputStr)
```

## Erlang

```erlang
-module(solution).
-export([main/0]).

main() ->
    io:put_chars("Hello, World.\n"),
    io:put_chars(io:get_line("")).
```

## JavaScript (Node.js)

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

## Go

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

## D

```d
import std.stdio;

void main() {
    string inputStr = readln();
    writeln("Hello, World.");
    writeln(inputStr);
}
```

## OCaml

```ocaml
let inputStr = read_line () in
print_string "Hello, World.\n";
print_string inputStr;
```

## Pascal

```pascal
var inputStr : String;

begin
    writeln('Hello, World.');
    readln(inputStr);
    writeln(inputStr);
end.
```

## Common Lisp (SBCL)

```lisp
(format t "Hello, World.~%")
(let ((s (read-line)))
    (format t s))
```

## Groovy

```groovy
def inputStr = System.in.newReader().readLine()
println "Hello, World."
println "${inputStr}"
```

## Objective-C

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

## F#

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

## COBOL

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

## VB.NET

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

## Tcl

```tcl
set str [gets stdin]
puts "Hello, World."
puts $str
```

## Racket

```racket
#lang racket
(printf "Hello, World.\n")
(define inputStr (read-line))
(printf "~a\n" inputStr)
```

## Rust

```rust
use std::io::{self, Read};

fn main() {
    let mut guess = String::new();

    io::stdin().read_line(&mut guess);
    println!("Hello, World.");
    println!("{}", guess);
}
```

## Fortran

```fortran
program hello  

    character (len = 35) :: input_string

    write(*, '(A)') "Hello, World."
    read (*, '(A)'), input_string
    write(*, '(A)') input_string

end program hello
```

## Ada

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

## CoffeeScript

```coffee
stdin = process.openStdin()
stdin.setEncoding 'utf8'

stdin.on 'data', (input) ->
    console.log 'Hello, World.'
    console.log input
```

## Elixir

```elixir
defmodule Solution do
    inputStr = IO.gets("")
    IO.puts "Hello, World."
    IO.puts "#{inputStr}"
end
```

## Swift

```swift
let inputString = readLine()!
print("Hello, World.")
print(inputString)
```

## Kotlin

```kotlin
import java.io.*
import java.util.*

fun main(args: Array<String>) {
    val inputStr = readLine()!!
    println("Hello, World.")
    println(inputStr)
}
```

## Julia

```julia
inputStr = readline()
println("Hello, World.")
println(inputStr)
```

## TypeScript

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
