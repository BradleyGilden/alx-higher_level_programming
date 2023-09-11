#!/usr/bin/node
/**
 * a script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 */

const icon = 'X';
let sides = process.argv[2];

if (isNaN(sides)) {
  console.log('Missing size');
} else {
  sides = parseInt(sides);
  for (let i = 0; i < sides; i++) {
    console.log(icon.repeat(sides));
  }
}
