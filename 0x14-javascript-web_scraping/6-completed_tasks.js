#!/usr/bin/node

/**
 * a script that display the status code of a GET request.
 *    The first argument is the URL to request (GET)
 *    The status code must be printed like this: code: <status code>
 *    You must use the module request
 *
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  const results = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    for (const task of todos) {
      if (task.completed) {
        results[task.userId] += 1;
      }
    }
    console.log(results);
  }
});
