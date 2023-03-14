#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!x) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let string = "";
    for (let j = 0; j < x; j++) {
      string += 'x';
    }
    console.log(string);
  }
}
