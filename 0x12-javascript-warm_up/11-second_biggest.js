#!/usr/bin/node

const x = parseInt(process.argv.length);
let first = parseInt(process.argv[2]);
let second = parseInt(proces)

function secondBig(x) {

  for(let i = 0; i <= x.length; i++){
    if(x[i] > first){
      second = first;
      first = x[i];
    }
    else if (x[i] > second && x[i] != first) {
      second = x[i];
    }
  }
  console.log(second);
}

secondBig(x);
