#!/usr/bin/node

/**
 * a script that gets the contents of a webpage and stores it in a file.
 *    The first argument is the URL to request
 *    The second argument the file path to store the body response
 *    The file must be UTF-8 encoded
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
