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
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);

        int i2;
        double d2;
        String s2;
        
        i2 = scan.nextInt();
        d2 = scan.nextDouble();
        scan.nextLine();
        s2 = scan.nextLine();
        
        System.out.println(i+i2);
        System.out.println(d+d2);
        System.out.println(s+s2);

        scan.close();
    }
}
```

### JavaScript (Node.js)

```js
process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

// Reads complete line from STDIN
function readLine() {
    return input_stdin_array[input_currentline++];
}

function main() {
    var i = 4
    var d = 4.0
    var s = "HackerRank "
    
    var i2 = +(readLine());
    var d2 = +(readLine());
    var s2 = readLine();
    
    console.log(i + i2);
    console.log((d + d2).toFixed(1));
    console.log(s + s2);

}
```

### Julia

```julia
i =  4
d = 4.0
s = "HackerRank"

i2 = parse(Int64, readline())
d2 = parse(Float64, readline())
s2 = readline()

println(i + i2)
println(d + d2)
println(s," ",s2)
```

### Perl

```perl
$i = 4;
$d = 4.0;
$s = 'HackerRank ';

$i2 = <STDIN>;
$d2 = <STDIN>;
$s2 = <STDIN>;

print($i + $i2);
print("\n");
printf("%.1f\n",$d + $d2);
print($s, $s2);
```

### PHP

```php
<?php
$handle = fopen ("php://stdin","r");
$i = 4;
$d = 4.0;
$s = "HackerRank ";

$i2 = fgets($handle);
$d2 = fgets($handle);
$s2 = fgets($handle);

printf("%d\n", $i + $i2);
printf("%.1f\n", $d + $d2);
printf("%s%s\n", $s, $s2);

fclose($handle);
?>
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
i = 4
d = 4.0
s = 'HackerRank '

i2 = gets.strip.to_i
d2 = gets.strip.to_f
s2 = gets.strip

puts (i2 + i), (d2 + d), (s + s2)
```

### Scala

```scala
object Solution {
    def main(args: Array[String]) {
        val i = 4
        val d = 4.0
        val s = "HackerRank "

		val i2 = scala.io.StdIn.readInt()
        val d2 = scala.io.StdIn.readDouble()
        val s2 = scala.io.StdIn.readLine()
        
        println(i + i2)
        println(d + d2)
        println(s + s2)
    }
}
```

### Swift

```swift
var i = 4
var d = 4.0
var s = "HackerRank "

let i2 = Int(readLine()!)
let d2 = Double(readLine()!)
let s2 = readLine()!

print(i + i2!)
print(d + d2!)
print(s + s2)
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
    let i:number = 4;
    let d:number = 4;
    let s: string = 'HackerRank ';
    
    let i2 = parseInt(inputLines[0]);
    let d2 = parseFloat(inputLines[1]);
    let s2 = inputLines[2];
    
    console.log(i + i2);
    console.log((d + d2).toFixed(1));
    console.log(s + s2);
}
```

### VB.NET

```vb
Imports System

Module Solution
    
    Public Shared Sub Main()
        Dim i As Integer = 4
        Dim d As Decimal = 4.0
        Dim s As String = "HackerRank "
        
        Dim i2 As Integer
        Dim d2 as Decimal
        Dim s2 as String
        
        i2 = Console.ReadLine()
        d2 = Console.ReadLine()
        s2 = Console.ReadLine()

        Console.WriteLine(i + i2)
        Console.WriteLine(d + d2)
        Console.WriteLine(s + s2)

    End Sub
End Module
```

# Day 2: Operators

### C

```cpp
#include <stdio.h>
#include <math.h>

void solve(double meal_cost, int tip_percent, int tax_percent) {
    double tip = (tip_percent / 100.0) * meal_cost;
    double tax = (tax_percent / 100.0) * meal_cost;
    int total_cost = (int) round(meal_cost + tip + tax);
    printf("%d", total_cost);
}

int main() {
    double meal_cost;
    int tip_percent;
    int tax_percent;
    
    scanf("%lf", &meal_cost);
    scanf("%d", &tip_percent);
    scanf("%d", &tax_percent);
    
    solve(meal_cost, tip_percent, tax_percent);
    
    return 0;
}
```

### Clojure

```clojure
(def meal_cost (Double.(read-line)))
(def tip (* (/ meal_cost 100) (Double.(read-line))))
(def tax (* (/ meal_cost 100) (Double.(read-line))))
(def total_cost (int (Math/round (+ meal_cost tip tax))))
(println total_cost)
```

### C++ / C++14 / C++20

```cpp
#include <cmath>
#include <iostream>

using namespace std;

int main() {  
    int tip_percent;
    int tax_percent;
    double meal_cost;
    
    cin >> meal_cost;
    cin >> tip_percent;
    cin >> tax_percent;
    
    double tip = meal_cost * tip_percent / 100;
    double tax = meal_cost * tax_percent / 100;
    int total_cost = round(meal_cost + tip + tax);
    
    printf("%d", total_cost);
    
    return 0;
}
```

### C#

```cs
using System;
using System.Collections.Generic;
using System.IO;

class Solution
{
    public static void Main(string[] args)
    {
        double meal_cost = Convert.ToDouble(Console.ReadLine());
        int tip_percent = Convert.ToInt32(Console.ReadLine());
        int tax_percent = Convert.ToInt32(Console.ReadLine());

        solve(meal_cost, tip_percent, tax_percent);
    }
    
    public static void solve(double meal_cost, int tip_percent, int tax_percent)
    {
        double tip = meal_cost * tip_percent * 0.01;
        double tax = meal_cost * tax_percent * 0.01;
        int total_cost = Convert.ToInt32(Math.Round(meal_cost + tip + tax));
        Console.Write(total_cost);
    }
}
```

### Erlang

```erlang
-module(solution).
-export([main/0]).

% Complete the solve function below.
solve(Meal_cost, Tip_percent, Tax_percent) ->
    Tip = (Tip_percent / 100) * Meal_cost,
    Tax = (Tax_percent / 100) * Meal_cost,
    Total_cost =  round(Meal_cost + Tip + Tax),
    io:fwrite("~w~n", [round(Total_cost)]).

main() ->
    {Meal_cost, _} = string:to_float(io:get_line("")),
    {Tip_percent, _} = string:to_integer(io:get_line("")),
    {Tax_percent, _} = string:to_integer(io:get_line("")),
    solve(Meal_cost, Tip_percent, Tax_percent),
    ok.
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
    var _ = strconv.Itoa
    scanner := bufio.NewScanner(os.Stdin)

    scanner.Scan()
    meal_cost, _ := strconv.ParseFloat(scanner.Text(), 64)
    scanner.Scan()
    tip_percent, _ := strconv.ParseUint(scanner.Text(), 10, 64)
    scanner.Scan()
    tax_percent, _ := strconv.ParseUint(scanner.Text(), 10, 64)
    
    tip := (float64(tip_percent) / 100) * meal_cost
    tax := (float64(tax_percent) / 100) * meal_cost
    
    total_cost := int64(meal_cost + tip + tax + 0.5)
    
    fmt.Printf("%d", total_cost)
}
```

### Haskell

```haskell
main = do
    mec_input <- getLine
    tip_input <- getLine
    tax_input <- getLine

    let meal_cost = read mec_input :: Double
    let tip_percent = read tip_input :: Double
    let tax_percent = read tax_input :: Double
    
    let tip = (0.01 * tip_percent * meal_cost)
    let tax = (0.01 * tax_percent * meal_cost)
    let total_cost = meal_cost + tip + tax
    putStrLn $ show (round total_cost)
```

### Java 7 / 8 / 15

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double meal_cost = scan.nextDouble();
        int tip_percent = scan.nextInt();
        int tax_percent = scan.nextInt();
        scan.close();

        double tip = tip_percent * (meal_cost / 100);
        double tax = tax_percent * (meal_cost / 100);
        int total_cost = (int) Math.round(meal_cost + tip + tax);
        
        System.out.println(total_cost);
    }
}
```

### JavaScript (Node.js)

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
    return inputString[currentLine++];
}

function solve(meal_cost, tip_percent, tax_percent) {
    let tip = meal_cost * tip_percent / 100;
    let tax = meal_cost * tax_percent / 100;
    let total_cost = Math.round(meal_cost + tax + tip); 
    console.log(total_cost);
}

function main() {
    const meal_cost = parseFloat(readLine().trim());
    const tip_percent = parseInt(readLine().trim(), 10);
    const tax_percent = parseInt(readLine().trim(), 10);

    solve(meal_cost, tip_percent, tax_percent);
}
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

### Scala

```scala
```

### Swift

```swift
```

### TypeScript

```ts
```

# Day 3: Intro to Conditional Statements

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

### Erlang

```erlang
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

# Day 4: Class vs. Instance

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

### Erlang

```erlang
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

# Day 5: Loops

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

### Erlang

```erlang
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

# Day 6: Let's Review

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

### Erlang

```erlang
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

# Day 7: Arrays

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

### Erlang

```erlang
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

# Day 8: Dictionaries and Maps

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

### Erlang

```erlang
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

# Day 9: Recursion 3

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

### Erlang

```erlang
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

# Day 10: Binary Numbers

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

### Erlang

```erlang
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

# Day 11: 2D Arrays

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

### Erlang

```erlang
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

# Day 12: Inheritance

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

### Erlang

```erlang
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

# Day 13: Abstract Classes

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

### Erlang

```erlang
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

# Day 14: Scope

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

### Erlang

```erlang
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

# Day 15: Linked List

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

### Erlang

```erlang
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

# Day 16: Exceptions - String to Integer

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

### Erlang

```erlang
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

# Day 17: More Exceptions

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

### Erlang

```erlang
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

# Day 18: Queues and Stacks

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

### Erlang

```erlang
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

# Day 19: Interfaces

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

### Erlang

```erlang
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

# Day 20: Sorting

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

### Erlang

```erlang
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

# Day 21: Generics

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

### Erlang

```erlang
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

# Day 22: Binary Search Trees

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

### Erlang

```erlang
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

# Day 23: BST Level-Order Traversal

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

### Erlang

```erlang
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

# Day 24: More Linked Lists

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

### Erlang

```erlang
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

# Day 25: Running Time and Complexity

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

### Erlang

```erlang
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

# Day 26: Nested Logic

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

### Erlang

```erlang
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

# Day 27: Testing

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

### Erlang

```erlang
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

# Day 28: RegEx, Patterns, and Intro to Databases

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

### Erlang

```erlang
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

# Day 29: Bitwise AND

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

### Erlang

```erlang
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