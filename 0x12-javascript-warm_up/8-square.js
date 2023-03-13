#!/usr/bin/node

const x = parseInt(process.argv[2]);
let string = '';

if (!x) {
  console.log('Missing size');
}

for (let i = 0; i < x; ++i) {
  for (let j = 0; j < x; ++j) {
    string += 'x';
  }
  string += '\n';
}
console.log(string);
