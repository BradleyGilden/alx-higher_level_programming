<h1 align="center">JavaScript Warm UP</h1>

<p align="center"><img src="images/logo.svg.png" width=200px></p>

## Directory Files:

* [0-javascript_is_amazing.js](0-javascript_is_amazing.js) - a script that prints “JavaScript is amazing”
* [1-multi_languages.js](1-multi_languages.js) - a script that prints 3 lines
* [2-arguments.js](2-arguments.js) - a script that prints a message depending of the number of arguments passed:
  * If no arguments are passed to the script, print “No argument”
  * If only one argument is passed to the script, print “Argument found”
  * Otherwise, print “Arguments found”
* [3-value_argument.js](3-value_argument.js) - a script that prints the first argument passed to it:
  * If no arguments are passed to the script, print “No argument”
  * You must use console.log(...) to print all output
  * You are not allowed to use var
  * You are not allowed to use length
* [4-concat.js](4-concat.js) - a script that prints two arguments passed to it, in the following format: <arg1\> is <arg2\>
* [5-to_integer.js](5-to_integer.js) -  a script that prints My number: `<first argument converted in integer>` if the first argument can be converted to an integer:
* [6-multi_languages_loop.js](6-multi_languages_loop.js) - a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
* [7-multi_c.js](7-multi_c.js) - a script that prints `x` times “C is fun”
  * Where `x` is the first argument of the script
  * If the first argument can’t be converted to an integer, print:
  * “Missing number of occurrences”
* [8-square.js](8-square.js) - a script that prints a square
  * The first argument is the size of the square
  * If the first argument can’t be converted to an integer, print “Missing size”
  * You must use the character X to print the square
  * You must use console.log(...) to print all output
* [9-add.js](9-add.js) - a script that prints the addition of 2 integers
  * The first argument is the first integer
  * The second argument is the second integer
  * You have to define a function with this prototype: function add(a, b)
* [10-factorial.js](10-factorial.js) - a script that computes and prints a factorial
  * The first argument is integer (argument can be cast as integer) used for computing the factorial
  * Factorial of NaN is 1
  * You must do it recursively
  * You must use a function
* [11-second_biggest.js](11-second_biggest.js) - a script that searches the second biggest integer in the list of arguments.
  * You can assume all arguments can be converted to integer
  * If no argument passed, print 0
  * If the number of arguments is 1, print 0
* [12-object.js](12-object.js) - Update script to replace the value from 12 to 89
  * script:
  * ```javascript
    #!/usr/bin/node
    const myObject = {
      type: 'object',
      value: 12
    };
    console.log(myObject);
    /*
    YOUR CODE HERE
    */
    console.log(myObject);
    ```
* [13-add.js](13-add.js) - Write a function that returns the addition of 2 integers.
  * The function must be visible from outside
  * The name of the function must be add
  * main file: [mains/13-main.js](mains/13-main.js)
* [100-let_me_const.js](100-let_me_const.js) - a file that modifies the value of myVar to 333
  * main file: [mains/100-main.js](mains/100-main.js)
* [101-call_me_moby.js](101-call_me_moby.js) - a function that executes x times a function
  * main file: [mains/101-main.js](mains/101-main.js)
* [102-add_me_maybe.js](102-add_me_maybe.js) - a function that increments and calls a function
  * main file: [mains/102-main.js](mains/102-main.js)
* [103-object_fct.js](103-object_fct.js) - Update this script by adding a new function incr that increments the integer value
  * script:
  * ```javascript
    const myObject = {
      type: 'object',
      value: 12
    };
    console.log(myObject);
    /*
    YOUR CODE HERE
    */
    myObject.incr();
    console.log(myObject);
    myObject.incr();
    console.log(myObject);
    myObject.incr();
    console.log(myObject);
    ```


## Fun Facts:

JavaScript is a versatile and widely-used programming language, and it has many interesting and cool facts associated with it. Here are some:

1. **Brendan Eich**: JavaScript was created by Brendan Eich in just 10 days while he was working at Netscape Communications Corporation in 1995. It was initially called "Mocha" and later renamed to "LiveScript" before settling on "JavaScript."

2. **Not related to Java**: Despite its name, JavaScript is not related to the Java programming language. The name was chosen for marketing purposes to capitalize on Java's popularity in the mid-1990s.

3. **Multi-paradigm Language**: JavaScript is a multi-paradigm programming language, which means it supports different programming styles, including procedural, object-oriented, and functional programming.

4. **Interpreted Language**: JavaScript is an interpreted language, which means it doesn't need to be compiled before running. This makes development faster but can lead to potential runtime errors.

5. **First-Class Functions**: Functions in JavaScript are first-class citizens, which means they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.

6. **Closures**: JavaScript supports closures, which are functions that can remember and access variables from their containing (enclosing) scope even after that scope has exited. Closures are a powerful and unique feature of JavaScript.

7. **Dynamic Typing**: JavaScript is dynamically typed, meaning that variable types are determined at runtime rather than at compile time. This flexibility can be both an advantage and a source of bugs if not used carefully.

8. **Event-Driven Programming**: JavaScript is commonly used for event-driven programming, making it a popular choice for building interactive web applications. It can respond to user actions like clicks and input in real-time.

9. **Asynchronous Programming**: JavaScript supports asynchronous programming using callbacks, promises, and async/await. This is crucial for handling tasks like fetching data from servers without blocking the main thread.

10. **Huge Ecosystem**: JavaScript has a vast and vibrant ecosystem with a plethora of libraries and frameworks, including jQuery, React, Angular, and Vue.js for front-end development, and Node.js for server-side development.

11. **Cross-Browser Compatibility**: JavaScript is designed to work across different web browsers, and many libraries and tools have been created to help developers address cross-browser compatibility issues.

12. **JSON**: JavaScript Object Notation (JSON) is a lightweight data interchange format that is native to JavaScript. It's widely used for data storage and exchange in web applications.

13. **ECMAScript**: ECMAScript is the standardized specification for JavaScript. JavaScript engines in different web browsers implement this specification. ES6 (ECMAScript 2015) introduced significant improvements to the language, including arrow functions, classes, and let/const for variable declarations.

14. **Dynamic DOM Manipulation**: JavaScript is commonly used for dynamically manipulating the Document Object Model (DOM) of web pages, allowing developers to create interactive web applications.

15. **Growing Popularity**: JavaScript consistently ranks as one of the most popular programming languages according to various surveys and indices like the TIOBE Index and Stack Overflow Developer Survey.
