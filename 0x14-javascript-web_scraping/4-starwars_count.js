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

  const moviesWithWedge = body.results.filter(movie => {
    const hasWedge = movie.characters.some(characterUrl => {
      const containsWedge = characterUrl.includes(`/${characterId}/`);
      return containsWedge;
    });
    return hasWedge;
  });

  console.log(moviesWithWedge.length);
});
