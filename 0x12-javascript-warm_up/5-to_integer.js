#!/usr/bin/node

const custom = parseInt(process.argv[2], 10);

if (!custom) {
  console.log('Not a number');
} else {
  console.log('My number:', custom);
}
