#!/usr/bin/node

/**
 * a class Square that defines a square and inherits from Square of 5-square.js:
 * You must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints the rectangle
 * using the character c
 * If c is undefined, use the character X
 */
const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  charPrint (c) {
    c = c === undefined ? 'X' : c;
    for (let h = 0; h < this.height; h++) {
      console.log(c.repeat(this.width));
    }
  }
};
