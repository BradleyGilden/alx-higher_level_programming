#!/usr/bin/node

/**
 * a script that prints the title of a Star Wars movie where the episode number
 * matches a given integer.
 *    The first argument is the movie ID
 *    You must use the Star wars API with the endpoint
 *        https://swapi-api.alx-tools.com/api/films/:id
 *    You must use the module request
 *
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
