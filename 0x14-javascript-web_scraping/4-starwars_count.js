#!/usr/bin/node

/**
 * a script that prints the number of movies where the character
 * “Wedge Antilles” is present.
 *     The first argument is the API URL of the Star wars API:
 *         https://swapi-api.alx-tools.com/api/films/
 *     Wedge Antilles is character ID 18 - your script must use this ID for
 *         filtering the result of the API
 *     You must use the module request
 *
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

const request = require('request');

const url = process.argv[2];

request(url, async (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
