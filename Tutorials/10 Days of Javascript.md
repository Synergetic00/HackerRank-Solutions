# Day 0: Hello, World!

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   A line of code that prints "Hello, World!" on a new line is provided in the editor.
*   Write a second line of code that prints the contents of 'parameterVariable' on a new line.
*
*	Parameter:
*   parameterVariable - A string of text.
**/
function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log('Hello, World!');

    // Write a line of code that prints parameterVariable to stdout using console.log:
    console.log(parameterVariable);

}

function main() {
    const parameterVariable = readLine();

    greeting(parameterVariable);
}
```

# Day 0: Data Types

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   The variables 'firstInteger', 'firstDecimal', and 'firstString' are declared for you -- do not modify them.
*   Print three lines:
*   1. The sum of 'firstInteger' and the Number representation of 'secondInteger'.
*   2. The sum of 'firstDecimal' and the Number representation of 'secondDecimal'.
*   3. The concatenation of 'firstString' and 'secondString' ('firstString' must be first).
*
*	Parameter(s):
*   secondInteger - The string representation of an integer.
*   secondDecimal - The string representation of a floating-point number.
*   secondString - A string consisting of one or more space-separated words.
**/
function performOperation(secondInteger, secondDecimal, secondString) {
    // Declare a variable named 'firstInteger' and initialize with integer value 4.
    const firstInteger = 4;

    // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
    const firstDecimal = 4.0;

    // Declare a variable named 'firstString' and initialize with the string "HackerRank".
    const firstString = 'HackerRank ';

    // Write code that uses console.log to print the sum of the 'firstInteger' and 'secondInteger' (converted to a Number        type) on a new line.
    console.log(firstInteger + parseInt(secondInteger));

    // Write code that uses console.log to print the sum of 'firstDecimal' and 'secondDecimal' (converted to a Number            type) on a new line.
    console.log(firstDecimal + parseFloat(secondDecimal));

    // Write code that uses console.log to print the concatenation of 'firstString' and 'secondString' on a new line. The        variable 'firstString' must be printed first.
    console.log(firstString + secondString);
}

function main() {
    const secondInteger = readLine();
    const secondDecimal = readLine();
    const secondString = readLine();

    performOperation(secondInteger, secondDecimal, secondString);
}
```

# Day 1: Arithmetic Operators

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;
    area = length * width;
    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;
    perimeter = (2 * length) + (2 * width);
    return perimeter;
}

function main() {
    const length = +(readLine());
    const width = +(readLine());

    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}
```

# Day 1: Functions

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Create the function factorial here
 */
function factorial(n) {
    let res = 1;
    for (let i = 2; i <= n; i++) {
        res *= i;
    }
    return res;
}

function main() {
    const n = +(readLine());

    console.log(factorial(n));
}
```

# Day 1: Let and Const

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    const PI = Math.PI;
    let r = readLine();

    // Print the area of the circle:
    let area = PI * (r * r);
    console.log(area);

    // Print the perimeter of the circle:
    let perimeter = 2 * PI * r;
    console.log(perimeter);

    try {
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
```

# Day 2: Conditional Statements: If-Else

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
    // Write your code here
    if (25 < score && score <= 30) {
        grade = 'A';
    } else if (20 < score && score <= 25) {
        grade = 'B';
    } else if (15 < score && score <= 20) {
        grade = 'C';
    } else if (10 < score && score <= 15) {
        grade = 'D';
    } else if (5 < score && score <= 10) {
        grade = 'E';
    } else if (0 <= score && score <= 5) {
        grade = 'F';
    }

    return grade;
}


function main() {
    const score = +(readLine());

    console.log(getGrade(score));
}
```

# Day 2: Conditional Statements: Switch

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    // Write your code here
    switch (true) {
        case 'aeiou'.includes(s.charAt(0)):
            letter = 'A';
            break;
        case 'bcdfg'.includes(s.charAt(0)):
            letter = 'B';
            break;
        case 'hjklm'.includes(s.charAt(0)):
            letter = 'C';
            break;
        default:
            letter = 'D';
            break;
    }

    return letter;
}


function main() {
    const s = readLine();

    console.log(getLetter(s));
}
```

# Day 2: Loops

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vow = '', con = '';
    let vows = 'aeiou';
    for (let l of s) {
        if (vows.includes(l)) {
            vow += l + '\n';
        } else {
            con += l + '\n';
        }
    }
    console.log((vow+con).trim());
}


function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
```

# Day 3: Arrays

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let firstLargest = nums[0];
    let secondLargest = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > firstLargest) {
            secondLargest = firstLargest;
            firstLargest = nums[i];
        }
        
        if (nums[i] > secondLargest) {
            if (nums[i] < firstLargest) {
                secondLargest = nums[i];
            }
        }
    }
    
    return secondLargest;
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
```

# Day 3: Try, Catch, and Finally

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try {
        s = s.split('').reverse().join('');
    } catch(e) {
        console.log(e.message);
    } finally {
        console.log(s);
    }
}


function main() {
    const s = eval(readLine());

    reverseString(s);
}
```

# Day 3: Throw

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
function isPositive(a) {
    if (a < 0) {
        throw new Error("Negative Error");
    } else if (a == 0) {
        throw new Error("Zero Error");
    } else {
        return "YES";
    }
}


function main() {
    const n = +(readLine());

    for (let i = 0; i < n; i++) {
        const a = +(readLine());

        try {
            console.log(isPositive(a));
        } catch (e) {
            console.log(e.message);
        }
    }
}
```

# Day 4: Create a Rectangle Object

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = 2 * (a + b);
    this.area = a * b;
}


function main() {
    const a = +(readLine());
    const b = +(readLine());

    const rec = new Rectangle(a, b);

    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}
```

# Day 4: Count Objects

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    let count = 0;
    for (let object of objects) {
        if (object.x == object.y) {
            count++;
        }
    }
    return count;
}


function main() {
    const n = +(readLine());
    let objects = [];
    
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');
        
        objects.push({x: +(a), y: +(b)});
    }
    
    console.log(getCount(objects));
}
```

# Day 4: Classes

```js
/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
class Polygon {
    constructor(sides) {
        this.sides = sides;
    }
    
    perimeter() {
        return this.sides.reduce((total, side) => total + side);
    }
}


const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
```

# Day 5: Inheritance

```js
class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}

/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */
Rectangle.prototype.area = function() {
    return this.w * this.h;
}

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
class Square extends Rectangle {
    constructor(s) {
        super(s,s);
    }
}


if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify([ 'constructor' ])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);

    console.log(rec.area());
    console.log(sqr.area());
} else {
    console.log(-1);
    console.log(-1);
}
```

# Day 5: Template Literals

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) {
    const [a, p] = expressions;
    
    let root = Math.sqrt((p*p) - (16*a));
    
    let s1 = (p + root) / 4;
    let s2 = (p - root) / 4;
    
    return ([s1, s2].sort());
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}
```

# Day 5: Arrow Functions

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    return nums.map(s => (s % 2 == 0) ? s * 2 : s * 3);
}


function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);
    
    console.log(modifyArray(a).toString().split(',').join(' '));
}
```

# Day 6: Bitwise Operators

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getMaxLessThanK(n, k) {
    let max = 0;
    for (let b = n; b > 0; b--){
        for (let a = b - 1; a > 0; a--){
            const and = a & b;
            if ((and < k) && (and > max)) { 
                max = and;
            }            
        }
    }
    return max;
}


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}
```

# Day 6: JavaScript Dates

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    let dayName;
    // Write your code here
    let dayNumber = new Date(dateString).getUTCDay();
    let dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    dayName = dayNames[dayNumber];    
    return dayName;
}


function main() {
    const d = +(readLine());
    
    for (let i = 0; i < d; i++) {
        const date = readLine();
        
        console.log(getDayName(date));
    }
}
```

# Day 7: Regular Expressions I

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    let re = /^([aeiou])[a-z].+\1$/;

    /*
     * Do not remove the return statement
     */
    return re;
}


function main() {
    const re = regexVar();
    const s = readLine();

    console.log(re.test(s));
}
```

# Day 7: Regular Expressions II

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.', 
     * followed by one or more letters.
     */
    let re = /^(Dr|Mr|Mrs|Ms|Er)\.[A-Za-z]+$/;
    
    /*
     * Do not remove the return statement
     */
    return re;
}


function main() {
    const re = regexVar();
    const s = readLine();
    
    console.log(!!s.match(re));
}
```

# Day 7: Regular Expressions III

```js
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match ALL occurrences of numbers in a string.
     */
    let re = /\d+/g;
    
    /*
     * Do not remove the return statement
     */
    return re;
}


function main() {
    const re = regexVar();
    const s = readLine();
    
    const r = s.match(re);
    
    for (const e of r) {
        console.log(e);
    }
}
```

# Day 8: Create a Button

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Button</title>
    <link rel="stylesheet" href="css/button.css" type="text/css">
</head>
<body>
    <button id="btn" onclick="increment()">0</button>
</body>
<script src="js/button.js" type="text/javascript"></script>
</html>
```

`css/button.css`

```css
button {
    width: 96px;
    height: 48px;
    font-size: 24px;
}
```

`js/button.js`

```js
function increment() {
    var count = parseInt(document.getElementById("btn").innerHTML);
    document.getElementById("btn").innerHTML = (count+1);
}
```

# Day 8: Buttons Container

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Buttons Grid</title>
    <link rel="stylesheet" href="css/buttonsGrid.css" type="text/css">
</head>
<body>
    <div id="btns">
        <div>
            <button id="btn1">1</button>
            <button id="btn2">2</button>
            <button id="btn3">3</button>
        </div>
        <div>
            <button id="btn4">4</button>
            <button id="btn5" onclick="rotate()">5</button>
            <button id="btn6">6</button>
        </div>
        <div>
            <button id="btn7">7</button>
            <button id="btn8">8</button>
            <button id="btn9">9</button>
        </div>
    </div>
</body>
<script src="js/buttonsGrid.js" type="text/javascript"></script>
</html>
```

`css/buttonsGrid.css`

```css
#btns {
    width: 75%;
}

button {
    width: 30%;
    height: 48px;
    font-size: 24px;
}
```

`js/buttonsGrid.js`

```js
let values = [1,2,3,6,9,8,7,4];
const ids = [1,2,3,6,9,8,7,4];

function rotate() {
    values.unshift(values.pop());
    for (let i = 0; i < 8; i++) {
        document.getElementById("btn"+ids[i]).innerHTML = values[i];
    }
}
```

# Day 9: Binary Calculator

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Binary Calculator</title>
    <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
</head>
<body>
    <div id="container">
      <div id="res"></div>
      <div id="btns">
        <button id="btn0" onclick="addNumber(0)">0</button>
        <button id="btn1" onclick="addNumber(1)">1</button>
        <button id="btnClr" onclick="setEmpty()">C</button>
        <button id="btnEql" onclick="getResult()">=</button>
        <button id="btnSum" onclick="setOperator('+')">+</button>
        <button id="btnSub" onclick="setOperator('-')">-</button>
        <button id="btnMul" onclick="setOperator('*')">*</button>
        <button id="btnDiv" onclick="setOperator('/')">/</button>
      </div>        
    </div> 
</body>
<script src="js/binaryCalculator.js" type="text/javascript"></script>
</html>
```

`css/binaryCalculator.css`

```css
body {
    width: 33%;
}
  
#res {
    background-color: lightgray;
    border: solid;
    height: 48px;
    font-size: 20px;
}
  
#btns button {
    width: 25%;
    height: 36px;
    font-size: 18px;
    margin:0;
    float: left;
}
  
#btn0, #btn1 {
    background-color: lightgreen;
    color: brown;
}

#btnClr, #btnEql {
    background-color: darkgreen;
    color: white;
}
  
#btnSum, #btnSub, #btnMul, #btnDiv {
    background-color: black;
    color: red;
}
```

`js/binaryCalculator.js`

```js
const operators = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => Math.floor(a / b)
}

const result = document.getElementById("res");

function addNumber(num) {
    result.innerHTML += num;
}

function setEmpty() {
    result.innerHTML = "";
}

function getResult() {
    let [n1, op, n2] = res.innerText.split(/\b/);
    n1 = parseInt(n1, 2);
    n2 = parseInt(n2, 2);
    let answer = operators[op](n1, n2);
    result.innerHTML = answer.toString(2);
}

function setOperator(op) {
    result.innerHTML += op;
}
```