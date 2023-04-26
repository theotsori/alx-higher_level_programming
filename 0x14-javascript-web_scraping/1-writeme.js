#!/usr/bin/node
'use strict';

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  }
});
