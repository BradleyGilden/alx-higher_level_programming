#!/usr/bin/node

/**
 * Write a script that reads and prints the content of a file.
 *    The first argument is the file path
 *    The content of the file must be read in utf-8
 *    If an error occurred during the reading, print the error object
 *
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

const fs = require('fs');

const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, contents) => {
  if (err) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
