#!/usr/bin/node
'use script';

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    fs.writeFile(filePath, body, 'utf8', (error) => {
        if (error) {
            console.error(error);
            return;
        }
    });
});
