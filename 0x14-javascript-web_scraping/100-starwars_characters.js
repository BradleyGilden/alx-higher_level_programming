#!/usr/bin/node

/**
 * prints characters in a specified movie in random order
 * Author: Bradley Dillion Gilden
 * Date: 24-10-2023
 */

request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
