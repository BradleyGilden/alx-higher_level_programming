#!/usr/bin/node

/**
 * a script that computes the number of tasks completed by user id.
 *    + The first argument is the API URL:
 *      https://jsonplaceholder.typicode.com/todos
 *    + Only print users with completed task
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

    // delete keys with no complete tasks
    for (const key in results) {
      if (results[key] === 0) {
        delete results[key];
      }
    }
    console.log(results);
  }
});
