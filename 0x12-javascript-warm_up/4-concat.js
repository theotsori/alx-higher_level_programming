#!/usr/bin/node

const custom1 = (process.argv[2] || 'undefined');
const custom2 = (process.argv[3] || 'undefined');

console.log(custom1 + ' is ' + custom2);
