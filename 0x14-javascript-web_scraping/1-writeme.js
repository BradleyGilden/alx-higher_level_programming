#!/usr/bin/node

/**
 * Write a script writes a string to a file.
 *    The first argument is the file path
 *    The second argument is the string
 *    If an error occurred during the writing, print the error object
 *
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

const fs = require('fs');

const filename = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filename, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
