#!/usr/bin/node

/**
 * a script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 */
const num = process.argv[2];
console.log(factorial(num));

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}
