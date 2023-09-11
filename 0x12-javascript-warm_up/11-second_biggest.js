#!/usr/bin/node

/**
 * a script that searches the second biggest integer in the list of arguments.
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */

let args = process.argv;
const arglen = args.length;

if (arglen <= 3) {
  console.log(0);
} else {
  args = args.slice(2).map(item => parseInt(item)).sort();
  console.log(args[arglen - 4]);
}
