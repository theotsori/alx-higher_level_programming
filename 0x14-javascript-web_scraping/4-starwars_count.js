#!/usr/bin/node
'use strict';

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const moviesWithWedge = body.results.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(moviesWithWedge.length);
});
