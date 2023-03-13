#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // convert arguments to array of numbers
if (args.length < 2) {
  console.log(0); // print 0 if there are less than 2 arguments
} else {
  const max = Math.max(...args); // find the maximum value in the array
  const secondMax = Math.max(...args.filter(num => num !== max)); // find the second maximum value in the array
  console.log(secondMax); // print the second maximum value
}
