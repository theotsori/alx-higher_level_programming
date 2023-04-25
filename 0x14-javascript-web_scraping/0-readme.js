#!/usr/bin/node
'use strict';

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
