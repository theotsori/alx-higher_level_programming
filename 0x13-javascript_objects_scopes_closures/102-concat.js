#!/usr/bin/node

const fs = require('fs');
// const path = require('path');

const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

const cont1 = fs.readFileSync(file1, 'utf8');
const cont2 = fs.readFileSync(file2, 'utf8');
const cont3 = cont1 + cont2;

fs.writeFileSync(dest, cont3);
