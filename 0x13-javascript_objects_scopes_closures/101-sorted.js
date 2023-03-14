#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = Object.entries(dict).reduce((acc, [userId, numOccurrences]) => {
  if (numOccurrences in acc) {
    acc[numOccurrences].push(userId);
  } else {
    acc[numOccurrences] = [userId];
  }
  return acc;
}, {});

console.log(newDict);
