#!/usr/bin/node
'use script';

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const moviesWithWedge = body.results.filter(movie =>
    movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  console.log(moviesWithWedge.length);
});
